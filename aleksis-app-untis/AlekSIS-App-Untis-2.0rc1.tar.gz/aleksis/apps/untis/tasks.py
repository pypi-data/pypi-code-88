from aleksis.apps.untis.util.mysql.importers.terms import (
    get_future_terms_for_date,
    get_terms_for_date,
)
from aleksis.core.celery import app

from .util.mysql.main import untis_import_mysql as _untis_import_mysql


@app.task
def untis_import_mysql_current_term():
    """Celery task for import of UNTIS data from MySQL (current term)."""
    terms = get_terms_for_date()
    _untis_import_mysql(terms)


@app.task
def untis_import_mysql_future_terms():
    """Celery task for import of UNTIS data from MySQL (all future terms)."""
    terms = get_future_terms_for_date()
    _untis_import_mysql(terms)


@app.task
def untis_import_mysql_all_terms():
    """Celery task for import of UNTIS data from MySQL (all terms in DB)."""
    _untis_import_mysql()


@app.task
def untis_import_mysql_current_next_term():
    """Celery task for import of UNTIS data from MySQL (current and next term)."""
    terms = get_terms_for_date()
    future_terms = get_future_terms_for_date()
    if future_terms.exists():
        terms = terms.union(future_terms[0:1])
    _untis_import_mysql(terms)


@app.task
def untis_import_mysql_current_future_terms():
    """Celery task for import of UNTIS data from MySQL (current and future terms)."""
    terms = get_terms_for_date()
    future_terms = get_future_terms_for_date()
    terms = terms.union(future_terms)
    _untis_import_mysql(terms)
