# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


from .. import table_delete_row_with_where_condition


def test_table_delete_row_with_where_condition(capsys, table_id):
    table_delete_row_with_where_condition.delete_row_with_where_condition(table_id)

    out, err = capsys.readouterr()
    assert "Total inserted rows: 2" in out
    assert "Total rows: 1" in out
