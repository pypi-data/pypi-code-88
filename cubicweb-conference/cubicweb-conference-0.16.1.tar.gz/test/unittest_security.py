from __future__ import with_statement

from datetime import date

from logilab.common.testlib import unittest_main

from cubicweb import Unauthorized

from utils import ConferenceTC


class ConferenceSecurityTC(ConferenceTC):
    def setup_database(self):
        super(ConferenceSecurityTC, self).setup_database()
        with self.admin_access.repo_cnx() as cnx:
            chair = self.create_user(cnx, "chair")
            reviewer = self.create_user(cnx, "reviewer")
            self.create_user(cnx, "user")
            self.create_user(cnx, "guest", groups=("guests",))
            self.conf = cnx.create_entity(
                "Conference",
                title=u"my conf",
                url_id=u"conf",
                start_on=date(2010, 1, 27),
                end_on=date(2010, 1, 29),
                take_place_at=self.location,
                call_open=True,
                reverse_is_chair_at=chair,
                reverse_is_reviewer_at=reviewer,
            ).eid
            cnx.commit()

    def test_chair(self):
        with self.new_access("chair").repo_cnx() as cnx:
            conf = cnx.entity_from_eid(self.conf)
            conf.cw_set(description=u"one conference description")
            cnx.commit()

    def test_others(self):
        for login in ("reviewer", "user", "guest"):
            with self.new_access(login).repo_cnx() as cnx:
                conf = cnx.entity_from_eid(self.conf)
                conf.cw_set(description=u"one conference description")
                self.assertRaises(Unauthorized, cnx.commit)


class TrackSecurityTC(ConferenceSecurityTC):
    def setup_database(self):
        super(TrackSecurityTC, self).setup_database()
        with self.admin_access.repo_cnx() as cnx:
            self.track0 = cnx.create_entity(
                "Track", title=u"my_track0", in_conf=self.conf
            ).eid
            cnx.commit()

    def test_chair(self):
        with self.new_access("chair").repo_cnx() as cnx:
            cnx.create_entity("Track", title=u"my_track1", in_conf=self.conf)
            track0 = cnx.entity_from_eid(self.track0)
            track0.cw_set(description=u"one description")
            cnx.commit()
            track0.cw_clear_all_caches()
            self.assertEqual(track0.description, u"one description")
            track0.cw_delete()
            cnx.commit()

    def test_others(self):
        for login in ("reviewer", "user", "guest"):
            with self.new_access(login).repo_cnx() as cnx:
                self.assertRaises(
                    Unauthorized,
                    cnx.create_entity,
                    "Track",
                    title=u"my_track1",
                    in_conf=self.conf,
                )
                cnx.rollback()
                track0 = cnx.entity_from_eid(self.track0)
                track0.cw_set(description=u"one description")
                self.assertRaises(Unauthorized, cnx.commit)
                self.assertRaises(Unauthorized, track0.cw_delete)


class TalkSecurityTC(TrackSecurityTC):
    def setup_database(self):
        super(TalkSecurityTC, self).setup_database()
        with self.admin_access.repo_cnx() as cnx:
            self.talk0 = cnx.create_entity(
                "Talk", title=u"my_talk0", in_track=self.track0
            ).eid
            cnx.commit()

    def test_chair(self):
        with self.new_access("chair").repo_cnx() as cnx:
            track0 = cnx.entity_from_eid(self.track0)
            talk0 = cnx.entity_from_eid(self.talk0)
            cnx.create_entity("Talk", title=u"my_talk1", in_track=track0)
            cnx.commit()
            cnx.create_entity("Talk", title=u"my_talk2", in_conf=self.conf)
            cnx.commit()
            talk0.cw_set(description=u"a description")
            cnx.commit()
            talk0.cw_clear_all_caches()
            self.assertEqual(talk0.description, u"a description")
            talk0.cw_delete()
            cnx.commit()

    def test_user(self):
        for login in ("reviewer", "user"):
            with self.new_access(login).repo_cnx() as cnx:
                track0 = cnx.entity_from_eid(self.track0)
                talk0 = cnx.entity_from_eid(self.talk0)
                talk1 = cnx.create_entity("Talk", title=u"my_talk1", in_track=track0)
                cnx.commit()
                cnx.create_entity("Talk", title=u"my_talk2", in_conf=self.conf)
                cnx.commit()
                self.assertRaises(
                    Unauthorized, talk0.cw_set, description=u"a description"
                )
                cnx.rollback()
                talk1.cw_clear_all_caches()
                talk1.cw_set(description=u"new description")
                cnx.commit()
                self.assertEqual(talk1.description, u"new description")
                self.assertRaises(Unauthorized, talk0.cw_delete)

    def test_others(self):
        with self.new_access("guest").repo_cnx() as cnx:
            track0 = cnx.entity_from_eid(self.track0)
            talk0 = cnx.entity_from_eid(self.talk0)
            cnx.create_entity("Talk", title=u"my_talk1", in_track=track0)
            self.assertRaises(Unauthorized, cnx.commit)
            self.assertRaises(
                Unauthorized,
                cnx.create_entity,
                "Talk",
                title=u"my_talk2",
                in_conf=self.conf,
            )
            self.assertRaises(Unauthorized, talk0.cw_set, description=u"a description")
            self.assertRaises(Unauthorized, talk0.cw_delete)


if __name__ == "__main__":
    unittest_main()
