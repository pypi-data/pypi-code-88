from typing import List, Optional

from sqlalchemy import distinct, select
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import count, random

from .. import models, schemas


def skribbl_get_word(db: Session, word: str):
    return db.query(models.Skribbl).filter_by(word=word).first()


def skribbl_get_words(
    db: Session, limit: Optional[int] = None, user: Optional[int] = None
):
    r = db.query(models.Skribbl)
    if user:
        r = r.filter_by(user=user)
    else:
        r = r.order_by(random())
    if limit:
        r = r.limit(limit)
    return r.all()


def skribbl_add_word(db: Session, word: str, user: str) -> models.Skribbl:
    w = models.Skribbl(word=word, user=user)
    db.add(w)
    db.commit()
    db.refresh(w)
    return w


def skribbl_bulk_add_word(
    db: Session, words: schemas.SkribblIn
) -> List[models.Skribbl]:
    w = [models.Skribbl(word=word, user=words.user) for word in words.words]
    db.bulk_save_objects(w)
    db.commit()
    return w


def skribbl_delete_word(db: Session, word: str) -> int:
    r = db.query(models.Skribbl).filter_by(word=word).delete()
    db.commit()
    return r


def skribbl_get_stats_aggregate(db: Session):
    statement = select(
        count(distinct(models.Skribbl.user.label("authors"))),
        count(models.Skribbl.word.label("words")),
    )
    r = db.execute(statement).first()
    # FIXME: Why don't my labels work?
    return {"authors": r[0], "words": r[1]}


def skribbl_get_stats(db: Session):
    statement = select(
        models.Skribbl.user.label("user"),
        count(models.Skribbl.word).label("words"),
    ).group_by("user")
    return db.execute(statement).all()


def skribbl_get_user_stats(db: Session, user: str):
    return db.execute(
        select(
            models.Skribbl.user.label("user"),
            count(models.Skribbl.word).label("words"),
        ).where(
            models.Skribbl.user == user
        )  # TODO: verify that this works
    )
