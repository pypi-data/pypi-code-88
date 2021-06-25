from __future__ import with_statement
from cubicweb.devtools.testlib import CubicWebTC

from cubicweb import ValidationError


class KeywordHooksTC(CubicWebTC):

    def setup_database(self):
        with self.admin_access.cnx() as cnx:
            cwgroup = cnx.execute('Any U WHERE U is ET, U name "CWGroup"').one()
            self.classif1_eid = cnx.create_entity('Classification', name=u"classif1", classifies=cwgroup).eid
            cnx.commit()

    def test_keyword_add1(self):
        with self.admin_access.cnx() as cnx:
            ce = cnx.create_entity
            kw1_eid = ce('Keyword', name=u'kw1', included_in=self.classif1_eid).eid
            kw2_eid = ce('Keyword', name=u'kw2', subkeyword_of=kw1_eid, included_in=self.classif1_eid).eid
            kw3_eid = ce('Keyword', name=u'kw3', subkeyword_of=kw2_eid, included_in=self.classif1_eid).eid
            kw4_eid = ce('Keyword', name=u'kw4', subkeyword_of=kw3_eid, included_in=self.classif1_eid).eid
            kw5_eid = ce('Keyword', name=u'kw5', subkeyword_of=kw4_eid, included_in=self.classif1_eid).eid
            cnx.commit()
            parent = cnx.find('Keyword', eid=kw1_eid).one()
            child = cnx.find('Keyword', eid=kw5_eid).one()
            self.assertCountEqual([kw.name for kw in child.cw_adapt_to('ITree').iterparents()],
                                  ['kw4', 'kw3', 'kw2', 'kw1'])
            self.assertCountEqual([kw.name for kw in child.descendant_of], ['kw4', 'kw3', 'kw2', 'kw1'])
            self.assertCountEqual([kw.name for kw in parent.reverse_descendant_of], ['kw5', 'kw4', 'kw3', 'kw2'])
            self.assertCountEqual([kw.name for kw in parent.cw_adapt_to('ITree').recurse_children()],
                                  ['kw5', 'kw4', 'kw3', 'kw2'])

    def test_keyword_add2(self):
        with self.admin_access.cnx() as cnx:
            ce = cnx.create_entity
            kw1_eid = ce('Keyword', name=u'kw1', included_in=self.classif1_eid).eid
            kw2_eid = ce('Keyword', name=u'kw2', subkeyword_of=kw1_eid, included_in=self.classif1_eid).eid
            kw3_eid = ce('Keyword', name=u'kw3', included_in=self.classif1_eid).eid
            kw4_eid = ce('Keyword', name=u'kw4', subkeyword_of=kw3_eid, included_in=self.classif1_eid).eid
            kw5_eid = ce('Keyword', name=u'kw5',  subkeyword_of=kw4_eid, included_in=self.classif1_eid).eid
            cnx.commit()
            cnx.execute('SET K3 subkeyword_of K2 WHERE K3 eid %(kw3)s, K2 eid %(kw2)s',
                        {'kw3': kw3_eid, 'kw2': kw2_eid})
            cnx.commit()
            parent = cnx.find('Keyword', eid=kw1_eid).one()
            child = cnx.find('Keyword', eid=kw5_eid).one()
            self.assertCountEqual([kw.name for kw in child.cw_adapt_to('ITree').iterparents()],
                                  ['kw4', 'kw3', 'kw2', 'kw1'])
            self.assertCountEqual([kw.name for kw in child.descendant_of], ['kw4', 'kw3', 'kw2', 'kw1'])
            self.assertCountEqual([kw.name for kw in parent.reverse_descendant_of], ['kw5', 'kw4', 'kw3', 'kw2'])
            self.assertCountEqual([kw.name for kw in parent.cw_adapt_to('ITree').recurse_children()],
                                  ['kw5', 'kw4', 'kw3', 'kw2'])

    def test_keyword_add3(self):
        with self.admin_access.cnx() as cnx:
            ce = cnx.create_entity
            kw1_eid = ce('Keyword', name=u'kw1', included_in=self.classif1_eid).eid
            kw2_eid = ce('Keyword', name=u'kw2', subkeyword_of=kw1_eid, included_in=self.classif1_eid).eid
            kw3_eid = ce('Keyword', name=u'kw3', included_in=self.classif1_eid).eid
            kw4_eid = ce('Keyword', name=u'kw4', included_in=self.classif1_eid).eid
            kw5_eid = ce('Keyword', name=u'kw5', subkeyword_of=kw4_eid, included_in=self.classif1_eid).eid
            cnx.commit()
            cnx.execute('SET K2 subkeyword_of K3 WHERE K2 eid %(k2)s, K3 eid %(k3)s',
                        {'k2': kw4_eid, 'k3': kw3_eid})
            cnx.execute('SET K3 subkeyword_of K4 WHERE K3 eid %(k3)s, K4 eid %(k4)s',
                        {'k3': kw3_eid, 'k4': kw2_eid})
            cnx.commit()
            child = cnx.find('Keyword', eid=kw5_eid).one()
            parent = cnx.find('Keyword', eid=kw1_eid).one()
            self.assertCountEqual([kw.name for kw in child.descendant_of], ['kw4', 'kw3', 'kw2', 'kw1'])
            # XXX check the order of iterparents
            self.assertCountEqual([kw.name for kw in child.cw_adapt_to('ITree').iterparents()],
                                  ['kw4', 'kw3', 'kw2', 'kw1'])
            self.assertCountEqual([kw.name for kw in parent.cw_adapt_to('ITree').recurse_children()],
                                  ['kw2', 'kw3', 'kw4', 'kw5'])
            self.assertCountEqual([kw.name for kw in parent.reverse_descendant_of], ['kw2', 'kw3', 'kw4', 'kw5'])

    def test_keyword_add4(self):
        with self.admin_access.cnx() as cnx:
            ce = cnx.create_entity
            kw0_eid = ce('Keyword', name=u'kw0', included_in=self.classif1_eid).eid
            kw1_eid = ce('Keyword', name=u'kw1', included_in=self.classif1_eid).eid
            kw2_eid = ce('Keyword', name=u'kw2', subkeyword_of=kw1_eid, included_in=self.classif1_eid).eid
            kw3_eid = ce('Keyword', name=u'kw3', included_in=self.classif1_eid).eid
            kw4_eid = ce('Keyword', name=u'kw4', included_in=self.classif1_eid).eid
            kw5_eid = ce('Keyword', name=u'kw5',  subkeyword_of=kw4_eid, included_in=self.classif1_eid).eid
            cnx.execute('SET K3 subkeyword_of K2 WHERE K3 eid %(kw3)s, K2 eid %(kw2)s',
                        {'kw2': kw2_eid, 'kw3': kw3_eid})
            cnx.commit()
            kw3 = cnx.find('Keyword', eid=kw3_eid).one()
            self.assertCountEqual([kw.name for kw in kw3.descendant_of], ['kw1', 'kw2'])
            cnx.execute('SET K3 descendant_of K0 WHERE K3 eid %(kw3)s, K0 eid %(kw0)s',
                        {'kw3': kw3_eid, 'kw0': kw0_eid})
            cnx.commit()
            kw3 = cnx.find('Keyword', eid=kw3_eid).one()
            self.assertCountEqual([kw.name for kw in kw3.descendant_of], ['kw0', 'kw1', 'kw2'])
            cnx.execute('SET K3 descendant_of K4 WHERE K3 eid %(kw3)s, K4 eid %(kw4)s',
                        {'kw3': kw3_eid, 'kw4': kw4_eid})
            cnx.commit()
            kw3 = cnx.find('Keyword', eid=kw3_eid).one()
            self.assertCountEqual([kw.name for kw in kw3.descendant_of], ['kw0', 'kw1', 'kw2', 'kw4'])
            cnx.execute('SET K3 descendant_of K5 WHERE K3 eid %(kw3)s, K5 eid %(kw5)s',
                        {'kw3': kw3_eid, 'kw5': kw5_eid})
            cnx.commit()
            kw3.cw_clear_all_caches()
            self.assertCountEqual([kw.name for kw in kw3.descendant_of], ['kw0', 'kw1', 'kw2', 'kw4', 'kw5'])

    def test_keyword_update1(self):
        with self.admin_access.cnx() as cnx:
            ce = cnx.create_entity
            kw1_eid = ce('Keyword', name=u'kw1', included_in=self.classif1_eid).eid
            kw2_eid = ce('Keyword', name=u'kw2', subkeyword_of=kw1_eid, included_in=self.classif1_eid).eid
            kw3_eid = ce('Keyword', name=u'kw3', included_in=self.classif1_eid).eid
            kw4_eid = ce('Keyword', name=u'kw4', included_in=self.classif1_eid).eid
            kw5_eid = ce('Keyword', name=u'kw5',  subkeyword_of=kw4_eid, included_in=self.classif1_eid).eid
            cnx.execute('SET K3 subkeyword_of K2 WHERE K3 eid %(kw3)s, K2 eid %(kw2)s',
                        {'kw3': kw3_eid, 'kw2': kw2_eid})
            cnx.commit()
            kw3 = cnx.find('Keyword', eid=kw3_eid).one()
            self.assertCountEqual([kw.name for kw in kw3.descendant_of], ['kw1', 'kw2'])
            cnx.execute('SET K3 subkeyword_of K4 WHERE K3 eid %(kw3)s, K4 eid %(kw4)s',
                        {'kw3': kw3_eid, 'kw4': kw4_eid})
            cnx.commit()
            kw3 = cnx.find('Keyword', eid=kw3_eid).one()
            self.assertCountEqual([kw.name for kw in kw3.descendant_of], ['kw4'])
            cnx.execute('SET K3 subkeyword_of K5 WHERE K3 eid %(kw3)s, K5 eid %(kw5)s',
                        {'kw3': kw3_eid, 'kw5': kw5_eid})
            cnx.commit()
            kw3 = cnx.find('Keyword', eid=kw3_eid).one()
            self.assertCountEqual([kw.name for kw in kw3.descendant_of], ['kw4', 'kw5'])

    def test_keyword_descendant_of(self):
        with self.admin_access.cnx() as cnx:
            ce = cnx.create_entity
            kw1_eid = ce('Keyword', name=u'kw1', included_in=self.classif1_eid).eid
            kw2_eid = ce('Keyword', name=u'kw2', subkeyword_of=kw1_eid, included_in=self.classif1_eid).eid
            kw3_eid = ce('Keyword', name=u'kw3', subkeyword_of=kw1_eid, included_in=self.classif1_eid).eid
            cnx.commit()

            kw1 = cnx.find('Keyword', eid=kw1_eid).one()
            kw2 = cnx.find('Keyword', eid=kw2_eid).one()
            kw3 = cnx.find('Keyword', eid=kw3_eid).one()
            self.assertCountEqual([kw.name for kw in kw2.descendant_of], ['kw1', ])
            self.assertCountEqual([kw.name for kw in kw3.descendant_of], ['kw1', ])
            self.assertCountEqual([kw.name for kw in kw1.reverse_descendant_of], ['kw3', 'kw2'])
            self.assertCountEqual([kw.name for kw in kw1.cw_adapt_to('ITree').recurse_children()], ['kw2', 'kw3'])
            kw0_eid = ce('Keyword', name=u'kw0', included_in=self.classif1_eid).eid

            cnx.execute('SET K1 subkeyword_of K0 WHERE K1 eid %(kw1)s, K0 eid %(kw0)s',
                        {'kw1': kw1_eid, 'kw0': kw0_eid})
            cnx.commit()

            kw0 = cnx.find('Keyword', eid=kw0_eid).one()
            kw1 = cnx.find('Keyword', eid=kw1_eid).one()
            kw2 = cnx.find('Keyword', eid=kw2_eid).one()
            kw3 = cnx.find('Keyword', eid=kw3_eid).one()
            self.assertCountEqual([kw.name for kw in kw0.cw_adapt_to('ITree').recurse_children()],
                                  ['kw1', 'kw2', 'kw3'])
            self.assertCountEqual([kw.name for kw in kw0.reverse_descendant_of], ['kw3', 'kw2', 'kw1'])
            self.assertCountEqual([kw.name for kw in kw1.descendant_of], ['kw0'])
            self.assertCountEqual([kw.name for kw in kw2.descendant_of], ['kw1', 'kw0'])
            self.assertCountEqual([kw.name for kw in kw3.descendant_of], ['kw1', 'kw0'])

    def test_keyword_delete(self):
        """*after_delete_relation* of ``subkeyword_of``
        """
        with self.admin_access.cnx() as cnx:
            ce = cnx.create_entity
            kw1_eid = ce('Keyword', name=u'kw1', included_in=self.classif1_eid).eid
            kw2_eid = ce('Keyword', name=u'kw2', subkeyword_of=kw1_eid, included_in=self.classif1_eid).eid
            kw3_eid = ce('Keyword', name=u'kw3', subkeyword_of=kw2_eid, included_in=self.classif1_eid).eid
            kw4_eid = ce('Keyword', name=u'kw4', subkeyword_of=kw3_eid, included_in=self.classif1_eid).eid
            ce('Keyword', name=u'kw5',  subkeyword_of=kw4_eid, included_in=self.classif1_eid).eid
            cnx.commit()
            cnx.execute('DELETE K subkeyword_of K3 WHERE K is Keyword, K eid %(kw3)s',
                        {'kw3': kw3_eid})
            cnx.commit()
            kw3 = cnx.find('Keyword', eid=kw3_eid).one()
            self.assertCountEqual([kw.name for kw in kw3.cw_adapt_to('ITree').iterparents()], [])
            self.assertCountEqual([kw.name for kw in kw3.descendant_of], [])
            self.assertCountEqual([kw.name for kw in kw3.reverse_descendant_of], ['kw5', 'kw4'])
            self.assertCountEqual([kw.name for kw in kw3.cw_adapt_to('ITree').recurse_children()], ['kw5', 'kw4'])

    def test_no_add_descendant_cycle(self):
        """no ``descendant_of`` cycle"""
        with self.admin_access.cnx() as cnx:
            ce = cnx.create_entity
            kw1 = ce('Keyword', name=u'kw1', included_in=self.classif1_eid)
            kw2 = ce('Keyword', name=u'kw2', subkeyword_of=kw1, included_in=self.classif1_eid)
            kw3 = ce('Keyword', name=u'kw3', subkeyword_of=kw2, included_in=self.classif1_eid)
            cnx.commit()
            rql = 'SET K1 descendant_of K3 WHERE K1 eid %(kw1)s, K3 eid %(kw3)s' % {'kw1': kw1.eid,  'kw3': kw3.eid}
            self.assertRaises(ValidationError, cnx.execute, rql)
            cnx.rollback()
            kw4 = ce('Keyword', name=u'kw4', included_in=self.classif1_eid)
            kw5 = ce('Keyword', name=u'kw4', subkeyword_of=kw4, included_in=self.classif1_eid)
            cnx.commit()
            with self.assertRaises(ValidationError):
                cnx.execute('SET K4 descendant_of K5 WHERE K4 eid %(kw4)s, K5 eid %(kw5)s',
                            {'kw4': kw4.eid,  'kw5': kw5.eid})


if __name__ == '__main__':
    from logilab.common.testlib import unittest_main
    unittest_main()
