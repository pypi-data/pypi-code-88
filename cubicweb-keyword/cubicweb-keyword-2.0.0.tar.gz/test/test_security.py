from cubicweb.devtools.testlib import CubicWebTC


class SecurityTC(CubicWebTC):
    def setup_database(self):
        with self.admin_access.cnx() as cnx:
            cwgroup = cnx.execute('Any U WHERE U is ET, U name "CWGroup"').one()
            self.classif1_eid = cnx.create_entity('Classification', name=u"classif1", classifies=cwgroup).eid
            self.kw1_eid = cnx.create_entity('Keyword', name=u'kw1', included_in=self.classif1_eid).eid
            cnx.commit()

    def test_nonregr_keyword_selection_as_guest(self):
        with self.new_access("anon").cnx() as cnx:
            cnx.execute('Any X ORDERBY Z WHERE X modification_date Z, K eid %(k)s, K applied_to X', {'k': self.kw1_eid})


if __name__ == '__main__':
    from logilab.common.testlib import unittest_main
    unittest_main()
