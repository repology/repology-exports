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

import csv
from typing import Any, IO

from repologyexport import Export


class WikidataExport(Export):
    def get_name(self) -> str:
        return 'wikidata.csv'

    def run(self, db: Any, outfile: IO[str]) -> None:
        writer = csv.writer(outfile)

        with db.cursor() as cur:
            cur.execute(
                """
                SELECT DISTINCT
                    effname,
                    extrafields->>'entity'
                FROM packages
                WHERE repo='wikidata'
                ORDER BY effname
                """
            )

            writer.writerows(cur.fetchall())
