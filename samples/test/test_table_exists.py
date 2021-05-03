# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


from .. import table_exists


def test_create_table(capsys, table_id):
    table_exists.table_exists(table_id)
    out, err = capsys.readouterr()
    assert "Table exists" in out
