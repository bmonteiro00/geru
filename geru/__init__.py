from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory
from geru.views.home_view import HomeView
from geru.views.quote_view import QuoteView
from geru.views.session_view import SessionView
from geru.views.quotes_view import QuotesView


def main(global_config, **settings):
    """ Main function.
        This function returns a Pyramid WSGI application.
    """

    my_session_factory = SignedCookieSessionFactory('GERU')
    config = Configurator(settings=settings)
    config.set_session_factory(my_session_factory)
    config.include('pyramid_chameleon')

    config.add_route('home', '/')
    config.add_view(HomeView, route_name='home', attr='get_home')

    config.add_route('quote', '/quotes/{id}')
    config.add_view(QuoteView, route_name='quote', attr='get_quote')

    config.add_route('session', '/sessions')
    config.add_view(SessionView, route_name='session', attr='get_sessions')

    config.add_route('quotes', '/quotes')
    config.add_view(QuotesView, route_name='quotes', attr='get_quotes')

    return config.make_wsgi_app()
