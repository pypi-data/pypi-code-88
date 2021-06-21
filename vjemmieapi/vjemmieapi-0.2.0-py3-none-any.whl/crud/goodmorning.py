from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import random

from .. import models, schemas


def get_goodmorning_random(db: Session):
    return db.query(models.Goodmorning.target).order_by(random()).limit(1).first()


def get_goodmorning_all(db: Session):
    return db.query(models.Goodmorning).all()


def add_goodmorning_target(db: Session, target: schemas.GoodmorningIn):
    g = models.Goodmorning(target=target.target, submitter=target.submitter)
    db.add(g)
    db.commit()
    db.refresh(g)
    return g


def remove_goodmorning_target(db: Session, target: str):
    return db.query(models.Goodmorning).filter_by(target=target).delete()
