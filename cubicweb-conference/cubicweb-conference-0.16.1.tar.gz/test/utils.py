# -*- encoding: utf-8 -*-

from cubicweb.devtools.testlib import CubicWebTC


class ConferenceTC(CubicWebTC):
    def setup_database(self):
        with self.admin_access.repo_cnx() as cnx:
            self.location = cnx.create_entity(
                u"PostalAddress",
                street=u"1, rue du chat qui pêche",
                postalcode=u"75005",
                city=u"Paris",
            ).eid
            cnx.commit()
