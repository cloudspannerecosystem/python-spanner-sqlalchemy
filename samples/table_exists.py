# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


def table_exists(table):
    """Check the table exists"""
    # [START sqlalchemy_spanner_table_exists]

    # TODO(developer): Create the table
    # table = Table(
    #    table_id,
    #    metadata,
    #    Column("user_id", Integer, primary_key=True),
    #    Column("user_name", String(16), nullable=False),
    # )
    # table.create()

    result = table.exists()
    print("Table exists:", result)
    # [END sqlalchemy_spanner_table_exists]
