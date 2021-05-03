# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


def delete_row_with_where_condition(table):
    """Delete selected row from the table"""

    # TODO(developer): Create the table
    # table = Table(
    #    table_id,
    #    metadata,
    #    Column("user_id", Integer, primary_key=True),
    #    Column("user_name", String(16), nullable=False),
    # )
    # table.create()

    table.insert().execute(
        {"user_id": 1, "user_name": 'ABC'},
        {"user_id": 2, "user_name": 'DEF'}
    )

    result = table.select().execute().fetchall()
    print("Total inserted rows:", len(result))

    # [START sqlalchemy_spanner_delete_row_with_where_condition]
    table.delete().where(table.c.user_id == 1).execute()

    result = table.select().execute().fetchall()
    print("Total rows:", len(result))
    # [END sqlalchemy_spanner_delete_row_with_where_condition]
