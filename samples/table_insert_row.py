# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


def insert_row(table):
    """Insert row in the table"""

    # TODO(developer): Create the table
    # table = Table(
    #    table_id,
    #    metadata,
    #    Column("user_id", Integer, primary_key=True),
    #    Column("user_name", String(16), nullable=False),
    # )
    # table.create()

    # [START sqlalchemy_spanner_insert_row]
    table.insert().execute({"user_id": 1, "user_name": 'ABC'})

    result = [row for row in table.select().execute()]

    print("Total rows:", result)
    # [END sqlalchemy_spanner_insert_row]
    return result
