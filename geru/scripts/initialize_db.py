import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from geru.models.model_quote import (
    DBSession,
    Session,
    Base,
    )


if __name__ == '__main__':
    setup_logging("C:/Users/Bruno/PycharmProjects/GERU/development.ini")
    settings = get_appsettings("C:/Users/Bruno/PycharmProjects/GERU/development.ini")
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        model = Session(uid="text", page="Root")
        DBSession.add(model)
