# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


from .. import table_fetch_rows_with_order_by


def test_table_delete_all_rows(capsys, table_id):
    table_fetch_rows_with_order_by.fetch_rows_with_order_by(table_id)

    out, err = capsys.readouterr()
    assert "The order by result is:" in out
