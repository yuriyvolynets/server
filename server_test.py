# !/usr/bin/python

class TestServer(object):
    def test_1(self, server_app):
        server_app.get_connected_switches()

    def test_2(self, server_app):
        server_app.get_value_from_db()
