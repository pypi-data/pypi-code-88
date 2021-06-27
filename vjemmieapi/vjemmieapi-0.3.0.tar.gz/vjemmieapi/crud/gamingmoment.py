from typing import Optional
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from sqlalchemy import desc

from .. import models


def get_gamingmoments_by_id(db: Session, user: str):
    return (
        db.query(models.GamingMoment).filter(models.GamingMoment.user == user).first()
    )


def get_gamingmoments(db: Session, limit: Optional[int] = None):
    return (
        db.query(models.GamingMoment)
        .order_by(desc(models.GamingMoment.count))
        .filter(models.GamingMoment.count > 0)
        .limit(limit)
        .all()
    )


def add_gamingmoment(db: Session, user: str):
    res = db.query(models.GamingMoment).filter_by(user=user)
    if res.first() is None:
        db.add(models.GamingMoment(user=user, count=1))
    else:
        res.update({"count": models.GamingMoment.count + 1})
    db.commit()
    return db.query(models.GamingMoment).filter_by(user=user).first()


def decrease_gamingmoments(db: Session, user: str):
    res = db.query(models.GamingMoment).filter_by(user=user)
    r = res.first()
    if r is None:
        db.add(models.GamingMoment(user=user, count=0))
    elif r.count > 0:
        res.update({"count": models.GamingMoment.count - 1})
    # don't do anything if count is already at 0
    db.commit()
    return db.query(models.GamingMoment).filter_by(user=user).first()


def delete_gamingmoments(db: Session, user: str) -> int:
    res = db.query(models.GamingMoment).filter_by(user=user).delete()
    db.commit()
    return res
