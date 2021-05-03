# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

from sqlalchemy import (
        Column,
        Integer,
        MetaData,
        String,
        Table,
        create_engine,
)


def create_table(url, random_table_id):
    """Create the table"""
    # [START sqlalchemy_spanner_create_table]

    engine = create_engine(url)
    metadata = MetaData(bind=engine)

    table = Table(
        random_table_id,
        metadata,
        Column("user_id", Integer, primary_key=True),
        Column("user_name", String(16), nullable=False),
    )
    table.create()

    print("Table {} is created successfully".format(table.name))
    # [END sqlalchemy_spanner_create_table]
    return table
