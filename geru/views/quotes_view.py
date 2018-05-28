from pyramid.response import Response
from pyramid.view import view_defaults

from geru.wrapper.helpers import QuoteHelper
from geru.models import QuoteModelHelper
import json


@view_defaults(attr='get_quotes', route_name='quotes', renderer='json')
class QuotesView:
        """ Class to render the quotes view.
            This view shows the whole quote json. """

        def __init__(self, request):
            self.request = request

        def get_quotes(self):

            if 'geru' in self.request.session:
                helper = QuoteHelper.QuoteHelper()
                data = helper.get_quotes()
                data = json.dumps(data)

                QuoteModelHelper.QuoteModelHelper().add_in_table('geru', 'quotes')
                return Response(body=data, content_type='application/json', charset='UTF-8')
            else:
                self.request.session['geru'] = 'OK'
                return Response('Geru was not in the session.')
