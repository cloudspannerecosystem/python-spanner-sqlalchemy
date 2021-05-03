# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


from .. import table_filter_data_with_contains


def test_table_filter_data_with_contains(capsys, table_id):
    rows = table_filter_data_with_contains.filter_data_with_contains(table_id)

    out, err = capsys.readouterr()
    assert "Filtered data:" in out
    assert len(rows) is 4
