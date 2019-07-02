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

import argparse
import os
import sys

import psycopg2

from repologyexport import Export
from repologyexport.moduleutils import enumerate_subclasses


def parse_arguments() -> argparse.Namespace:
    config = {
        'DSN': 'dbname=repology user=repology password=repology',
    }

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--dsn', default=config['DSN'], help='database connection params')
    parser.add_argument('--target-dir', type=str, required=True, help='max number of connections to the database')

    return parser.parse_args()


def main() -> int:
    options = parse_arguments()

    db = psycopg2.connect(options.dsn, application_name='repology-export')
    db.set_session(readonly=True)

    for exportclass in enumerate_subclasses('repologyexport.exports', Export):
        export = exportclass()

        outfile = os.path.join(options.target_dir, export.get_name())
        tmpfile = outfile + '.tmp'

        print('Exporting {} to {}'.format(export.get_name(), outfile), file=sys.stderr)

        with open(tmpfile, 'w') as outfd:
            export.run(db, outfd)
            outfd.flush()
            os.fsync(outfd.fileno())

        os.replace(tmpfile, outfile)

    return 0


if __name__ == '__main__':
    sys.exit(main())
