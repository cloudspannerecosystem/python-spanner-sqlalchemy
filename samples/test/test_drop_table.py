# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


from .. import drop_table


def test_drop_table(capsys, db_url, random_table_id):

    table = drop_table.drop_table(db_url, random_table_id)
    out, err = capsys.readouterr()
    assert "dropped successfully" in out
    assert table.name == random_table_id
    assert table.exists() is False

