from pyramid.response import Response
from pyramid.view import view_defaults
from random import randint

from geru.wrapper.helpers import QuoteHelper
from geru.models import QuoteModelHelper


@view_defaults(attr='get_quote', route_name='quote', renderer='geru:templates/quote.pt')
class QuoteView:
    """ Class to render the quote view.
        This view show a single element from quote json. """

    def __init__(self, request):
        self.request = request

    def get_quote(self):
        if 'geru' in self.request.session:
            helper = QuoteHelper.QuoteHelper()

            pos = self.request.matchdict['id']

            if pos == 'random':
                size = helper.quotes_size()
                pos = randint(0, size)

            quote = helper.get_quote(pos)

            QuoteModelHelper.QuoteModelHelper().add_in_table('geru', 'quote')
            return {'id': pos,
                    'description': quote}
        else:
            self.request.session['geru'] = 'OK'
            return Response('Geru was not in the session.')

