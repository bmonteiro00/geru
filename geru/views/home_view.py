from pyramid.view import view_defaults
from pyramid.response import Response
from geru.models import QuoteModelHelper


@view_defaults(attr='get_home', route_name='home', renderer='geru:templates/home.pt')
class HomeView:
    """ Class to render the home view.
        This view show the first page of the application. """

    def __init__(self, request):
        self.request = request

    def get_home(self):
        session = self.request.session
        if 'geru' in session:
            QuoteModelHelper.QuoteModelHelper().add_in_table('geru', 'home')
            return {'id': 'OK'}
        else:
            session['geru'] = 'OK'
            return Response('Geru was not in the session.')
