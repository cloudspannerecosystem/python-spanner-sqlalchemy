# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


def filter_data_endswith(table):
    """filter data with endswith from the table"""

    # TODO(developer): Create the table
    # table = Table(
    #    table_id,
    #    metadata,
    #    Column("user_id", Integer, primary_key=True),
    #    Column("user_name", String(16), nullable=False),
    # )
    # table.create()

    table.insert().execute([
        {"user_id": 1, "user_name": "abcdefg"},
        {"user_id": 2, "user_name": "ab/cdefg"},
        {"user_id": 3, "user_name": "ab%cdefg"},
        {"user_id": 4, "user_name": "ab_cdefg"},
        {"user_id": 5, "user_name": "abcde/fg"},
        {"user_id": 6, "user_name": "abcde%fg"},
    ])

    # [START sqlalchemy_spanner_filter_data_endswith]
    result = list(table.select().where(table.c.user_name.endswith("%efg")).execute())
    print("Filtered data:", result)
    # [END sqlalchemy_spanner_filter_data_endswith]
    return result
