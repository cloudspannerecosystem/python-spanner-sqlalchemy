# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


from .. import table_update_row


def test_table_update_row(capsys, table_id):
    rows = table_update_row.update_row(table_id)

    out, err = capsys.readouterr()
    assert "Updated row is :" in out
    assert "GEH" == rows[0][1]
