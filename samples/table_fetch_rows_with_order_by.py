# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


def fetch_rows_with_order_by(table):
    """fetch all rows from the table in order"""

    # TODO(developer): Create the table
    # table = Table(
    #    table_id,
    #    metadata,
    #    Column("user_id", Integer, primary_key=True),
    #    Column("user_name", String(16), nullable=False),
    # )
    # table.create()

    table.insert().execute([
        {"user_id": 1, "user_name": 'GEH'},
        {"user_id": 2, "user_name": 'DEF'},
        {"user_id": 3, "user_name": 'HIJ'},
        {"user_id": 4, "user_name": 'ABC'}
    ])

    # [START sqlalchemy_spanner_fetch_rows_with_order_by]
    result = list(table.select().order_by(table.c.user_name).execute().fetchall())
    print("The order by result is:", result)
    # [END sqlalchemy_spanner_fetch_rows_with_order_by]
