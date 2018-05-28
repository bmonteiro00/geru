import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home_view_not_in_session(self):
        from geru.views.home_view import HomeView
        request = testing.DummyRequest()
        info = HomeView(request).get_home()
        self.assertEqual(info.text, 'Geru was not in the session.')

    def test_quote_view_not_in_session(self):
        from geru.views.quote_view import QuoteView
        request = testing.DummyRequest()
        info = QuoteView(request).get_quote()
        self.assertEqual(info.text, 'Geru was not in the session.')

    def test_quotes_view_not_in_session(self):
        from geru.views.quotes_view import QuotesView
        request = testing.DummyRequest()
        info = QuotesView(request).get_quotes()
        self.assertEqual(info.text, 'Geru was not in the session.')

    def test_home_view_in_session(self):
        from geru.views.home_view import HomeView
        request = testing.DummyRequest()
        HomeView(request).get_home()
        info = HomeView(request).get_home()
        self.assertEqual(info['id'], 'OK')

    def test_quote_pos2_view_in_session(self):
        from geru.views.quotes_view import QuotesView
        request = testing.DummyRequest(path='/quotes/{id}', params=2)
        QuotesView(request).get_quotes()
        info = QuotesView(request).get_quotes()
        self.assertEqual(len(info.json_body), 1)

    def test_quotes_view_in_session(self):
        from geru.views.quotes_view import QuotesView
        request = testing.DummyRequest()
        QuotesView(request).get_quotes()
        info = QuotesView(request).get_quotes()
        self.assertEqual(len(info.json_body), 18)

