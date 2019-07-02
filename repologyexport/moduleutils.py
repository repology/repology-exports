#!/usr/bin/env python3
#
# Copyright (C) 2019 Dmitry Marakasov <amdmi3@amdmi3.ru>
#
# This file is part of repology
#
# repology is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# repology is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with repology.  If not, see <http://www.gnu.org/licenses/>.

import importlib
import importlib.util
import inspect
import os
from typing import Any, Iterable


def enumerate_subclasses(module: str, superclass: Any) -> Iterable[Any]:
    spec = importlib.util.find_spec(module)
    if spec is None:
        raise RuntimeError('cannot find module {}'.format(module))
    if spec.submodule_search_locations is None:
        raise RuntimeError('module {} is not a package'.format(module))

    for location in spec.submodule_search_locations:
        for dirpath, dirnames, filenames in os.walk(location):
            for filename in filenames:
                fullpath = os.path.join(dirpath, filename)
                relpath = os.path.relpath(fullpath, location)

                if not filename.endswith('.py'):
                    continue

                submodulename = '.'.join([module] + relpath[:-3].split(os.sep))

                submodule = importlib.import_module(submodulename)

                for name, member in inspect.getmembers(submodule):
                    if inspect.isclass(member) and issubclass(member, superclass) and not member is superclass:
                        yield member

