# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


from .. import table_delete_all_rows


def test_table_delete_all_rows(capsys, table_id):
    table_delete_all_rows.delete_all_rows(table_id)

    out, err = capsys.readouterr()
    assert "Total inserted rows: 2" in out
    assert "Total rows: 0" in out
