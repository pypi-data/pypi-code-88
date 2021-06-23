from datetime import date

from logilab.common.testlib import unittest_main
from logilab.common.date import ustrftime

from utils import ConferenceTC


class ConferenceHooksTC(ConferenceTC):
    def test_url_identifier(self):
        with self.admin_access.repo_cnx() as cnx:
            conf1 = cnx.create_entity(
                u"Conference",
                title=u"conference test",
                url_id=u"conf",
                start_on=ustrftime(date(2010, 3, 1), "%Y/%m/%d"),
                end_on=ustrftime(date(2010, 3, 5), "%Y/%m/%d"),
                take_place_at=self.location,
                description=u"short description",
            )
            cnx.commit()
            self.assertEqual(conf1.url_id, u"conf")
            conf2 = cnx.create_entity(
                u"Conference",
                title=u"conference test2",
                start_on=ustrftime(date(2010, 3, 1), "%Y/%m/%d"),
                end_on=ustrftime(date(2010, 3, 5), "%Y/%m/%d"),
                take_place_at=self.location,
                description=u"short description",
            )
            cnx.commit()
            self.assertEqual(conf2.url_id, "conference_test2")

    def test_url_identifier_with_several_conferences(self):
        with self.admin_access.repo_cnx() as cnx:
            conf1 = cnx.create_entity(
                u"Conference",
                title=u"conFerence test",
                start_on=ustrftime(date(2010, 3, 1), "%Y/%m/%d"),
                end_on=ustrftime(date(2010, 3, 5), "%Y/%m/%d"),
                take_place_at=self.location,
                description=u"short description",
            )
            conf2 = cnx.create_entity(
                u"Conference",
                title=u"conference test2",
                start_on=ustrftime(date(2010, 3, 1), "%Y/%m/%d"),
                end_on=ustrftime(date(2010, 3, 5), "%Y/%m/%d"),
                take_place_at=self.location,
                description=u"short description",
            )
            cnx.commit()
            self.assertEqual(conf1.url_id, u"conference_test")
            self.assertEqual(conf2.url_id, "conference_test2")

    def test_url_identifier_with_same_url_id(self):
        with self.admin_access.repo_cnx() as cnx:
            conf1 = cnx.create_entity(
                u"Conference",
                title=u"conFerence test",
                start_on=ustrftime(date(2010, 3, 1), "%Y/%m/%d"),
                end_on=ustrftime(date(2010, 3, 5), "%Y/%m/%d"),
                take_place_at=self.location,
                description=u"short description",
            )
            conf2 = cnx.create_entity(
                u"Conference",
                title=u"conference test",
                start_on=ustrftime(date(2010, 3, 1), "%Y/%m/%d"),
                end_on=ustrftime(date(2010, 3, 5), "%Y/%m/%d"),
                take_place_at=self.location,
                description=u"short description",
            )
            cnx.commit()
            self.assertEqual(conf1.url_id, u"conference_test")
            self.assertEqual(conf2.url_id, "conference_test_1")


if __name__ == "__main__":
    unittest_main()
