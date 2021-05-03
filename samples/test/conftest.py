# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import uuid

import pytest

from sqlalchemy import (
        Column,
        Integer,
        MetaData,
        String,
        Table,
        create_engine,
)


@pytest.fixture
def db_url():
    return "spanner:///projects/appdev-soda-spanner-staging/instances/" \
           "sqlalchemy-dialect-test/databases/compliance-test"


@pytest.fixture
def random_table_id():
    now = datetime.datetime.now()
    random_table_id = "example_table_{}_{}".format(
        now.strftime("%Y%m%d%H%M%S"), uuid.uuid4().hex[:8]
    )
    return random_table_id


@pytest.fixture
def table_id(db_url, random_table_id):
    engine = create_engine(db_url)
    metadata = MetaData(bind=engine)

    table = Table(
        random_table_id,
        metadata,
        Column("user_id", Integer, primary_key=True),
        Column("user_name", String(16), nullable=False),
    )
    table.create()
    yield table
    table.drop()

