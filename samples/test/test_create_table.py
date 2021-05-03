# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


from .. import create_table


def test_create_table(capsys, db_url, random_table_id):
    table = create_table.create_table(db_url, random_table_id)
    out, err = capsys.readouterr()
    assert "created successfully" in out
    assert table.name == random_table_id
    assert table.exists() is True

    table.drop()
