from cubicweb.devtools.testlib import CubicWebTC

from cubicweb import ValidationError


class ClassificationHooksTC(CubicWebTC):

    def setup_database(self):
        with self.admin_access.cnx() as cnx:
            # classification for CWGroup
            cwgroup = cnx.execute('Any U WHERE U is ET, U name "CWGroup"').one()
            self.classif1_eid = cnx.create_entity('Classification', name=u"classif1", classifies=cwgroup).eid
            self.kwgroup_eid = cnx.create_entity('Keyword', name=u'kwgroup', included_in=self.classif1_eid).eid
            # classification for CWUser
            cwuser = cnx.execute('Any U WHERE U is ET, U name "CWUser"').one()
            self.classif2_eid = cnx.create_entity('Classification', name=u"classif2", classifies=cwuser).eid
            self.kwuser_eid = cnx.create_entity('Keyword', name=u'kwuser', included_in=self.classif2_eid).eid
            cnx.commit()

    def test_application_of_bad_keyword_fails(self):
        with self.admin_access.cnx() as cnx:
            cnx.execute('SET K applied_to G WHERE G is CWGroup, K eid %(k)s',
                        {'k': self.kwuser_eid})
            self.assertRaises(ValidationError, cnx.commit)

    def test_creating_a_new_subkeyword_sets_included_in(self):
        with self.admin_access.cnx() as cnx:
            kwgroup2_eid = cnx.create_entity('Keyword', name=u'kwgroup2', subkeyword_of=self.kwgroup_eid).eid
            cnx.commit()
            rset = cnx.execute('Any N WHERE C name N, K included_in C, K eid %(k)s', {'k': kwgroup2_eid})
            self.assertEqual(len(rset), 1)
            self.assertEqual(rset[0][0], 'classif1')

    def test_cannot_create_subkeyword_from_other_classification(self):
        with self.admin_access.cnx() as cnx:
            cnx.execute('SET K1 subkeyword_of K2 WHERE K1 eid %(k1)s, K2 eid %(k2)s',
                        {'k1': self.kwgroup_eid, 'k2': self.kwuser_eid})
            self.assertRaises(ValidationError, cnx.commit)

    def test_cannot_create_cycles(self):
        with self.admin_access.cnx() as cnx:
            # direct obvious cycle
            cnx.execute('SET K1 subkeyword_of K2 WHERE K1 eid %(k1)s, K2 eid %(k2)s',
                        {'k1': self.kwgroup_eid, 'k2': self.kwuser_eid})
            self.assertRaises(ValidationError, cnx.commit)
            # testing indirect cycles
            kwgroup2_eid = cnx.create_entity('Keyword', name=u'kwgroup2',
                                             included_in=self.classif1_eid,
                                             subkeyword_of=self.kwgroup_eid).eid
            cnx.execute('SET K subkeyword_of K2 WHERE K eid %(k)s, K2 eid %(k2)s',
                        {'k': self.kwgroup_eid, 'k2': kwgroup2_eid})
            self.assertRaises(ValidationError, cnx.commit)


if __name__ == '__main__':
    from logilab.common.testlib import unittest_main
    unittest_main()
