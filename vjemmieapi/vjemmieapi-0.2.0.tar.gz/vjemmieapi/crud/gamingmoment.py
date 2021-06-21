from typing import Optional
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import desc

from .. import models


def get_gamingmoments_by_id(db: Session, user_id: str):
    return (
        db.query(models.GamingMoment)
        .filter(models.GamingMoment.user_id == user_id)
        .first()
    )


def get_gamingmoments(db: Session, limit: Optional[int] = None):
    return (
        db.query(models.GamingMoment)
        .order_by(desc(models.GamingMoment.count))
        .filter(models.GamingMoment.count > 0)
        .limit(limit)
        .all()
    )


def add_gamingmoment(db: Session, user_id: str):
    res = db.query(models.GamingMoment).filter_by(user_id=user_id)
    if res.first() is None:
        db.add(models.GamingMoment(user_id=user_id, count=1))
    else:
        res.update({"count": models.GamingMoment.count + 1})
    db.commit()
    return db.query(models.GamingMoment).filter_by(user_id=user_id).first()


def decrease_gamingmoments(db: Session, user_id: str):
    res = db.query(models.GamingMoment).filter_by(user_id=user_id)
    r = res.first()
    if r is None:
        db.add(models.GamingMoment(user_id=user_id, count=0))
    elif r.count > 0:
        res.update({"count": models.GamingMoment.count - 1})
    # don't do anything if count is already at 0
    db.commit()
    return db.query(models.GamingMoment).filter_by(user_id=user_id).first()


def delete_gamingmoments(db: Session, user_id: str) -> int:
    res = db.query(models.GamingMoment).filter_by(user_id=user_id).delete()
    db.commit()
    return res
