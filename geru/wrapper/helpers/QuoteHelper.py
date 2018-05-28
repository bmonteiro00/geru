from geru.wrapper.conn import Connection


class QuoteHelper:
    """ Helper class to translate json to dict.
        Retrieve a single element from quote dict.
        Retrieve the length of quote json. """

    def __init__(self):
        self.__quotes = Connection.Connection().get_response()

    def get_quotes(self):
        return self.__quotes

    def get_quote(self, pos):
        quotes = self.get_quotes()
        quotes = quotes['quotes']
        quote = quotes[int(pos)]
        return quote

    def quotes_size(self):
        quotes = self.get_quotes()
        quotes = quotes['quotes']
        return len(quotes)




