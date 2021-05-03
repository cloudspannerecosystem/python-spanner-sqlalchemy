# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


from .. import table_fetch_rows


def test_table_fetch_rows(capsys, table_id):
    rows = table_fetch_rows.fetch_rows(table_id)

    out, err = capsys.readouterr()
    assert "Total rows:" in out
    assert len(rows) is 2
