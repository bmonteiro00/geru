from tzlocal import get_localzone

import datetime

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    )

from geru.models.model_quote import (
    DBSession,
    Session,
    Base,
    )

import transaction
import uuid
import json


class QuoteModelHelper:
    """ Class to help manipulate the BD queries.
        It does a insert in a database and retrieve all rows from the database. """
    def __init__(self):
        return

    def add_in_table(self, session, page):
        settings = get_appsettings("C:/Users/Bruno/PycharmProjects/GERU/development.ini")
        engine = engine_from_config(settings, 'sqlalchemy.')
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            model = Session(uid=str(uuid.uuid4()), session=session, date=str(datetime.date.today()),
                            time=str(datetime.datetime.now(get_localzone())), page=page)
            DBSession.add(model)

    def query_all_rows(self):
        settings = get_appsettings("C:/Users/Bruno/PycharmProjects/GERU/development.ini")
        engine = engine_from_config(settings, 'sqlalchemy.')
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            pages = DBSession.query(Session)

        msg = json.dumps([r.json for r in pages])
        return msg
