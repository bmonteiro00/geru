from pyramid.view import view_defaults, view_config
from pyramid.response import Response
from geru.models import QuoteModelHelper


@view_config(attr='get_sessions', route_name='session',  request_method='GET', renderer='json')
class SessionView:

    def __init__(self, request):
        self.request = request

    def get_sessions(self):
        msg = QuoteModelHelper.QuoteModelHelper().query_all_rows()
        return Response(msg, content_type='application/json', charset='utf-8')
