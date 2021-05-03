# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd


from .. import autocommit


def test_enable_autocommit_mode(capsys, db_url):

    conn = autocommit.enable_autocommit_mode(db_url)
    out, err = capsys.readouterr()
    assert "Connection autocommit default mode is " in out
    assert "Spanner DBAPI default autocommit mode is False" in out

    assert conn.connection.connection.autocommit is True
    assert "Connection autocommit mode is " in out
    assert "Spanner DBAPI autocommit mode is True" in out
