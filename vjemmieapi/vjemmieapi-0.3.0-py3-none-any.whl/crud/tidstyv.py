from sqlalchemy.sql.expression import desc
from .. import schemas, models
from sqlalchemy.orm import Session

# TODO: Refactor add/remove methods. Very similar.


def get_all_tidstyv(db: Session):
    return db.query(models.Tidstyv).order_by(desc(models.Tidstyv.stolen)).all()


def get_tidstyv_by_id(db: Session, user: str):
    return db.query(models.Tidstyv).filter_by(user=user).first()


def add_tidstyveri(db: Session, tidstyv: schemas.TidstyvIn):
    res = db.query(models.Tidstyv).filter_by(user=tidstyv.user).first()
    if res:
        res.stolen += tidstyv.stolen
    else:
        db.add(models.Tidstyv(user=tidstyv.user, stolen=tidstyv.stolen))
    db.commit()
    # NOTE: There has to be a better way?
    return db.query(models.Tidstyv).filter_by(user=tidstyv.user).first()


def remove_tidstyveri(db: Session, tidstyv: schemas.TidstyvIn):
    res = db.query(models.Tidstyv).filter_by(user=tidstyv.user).first()
    if not res:
        return
    res.stolen -= tidstyv.stolen
    if res.stolen < 0:
        res.stolen = 0
    db.commit()
    db.refresh(res)
    return res


def delete_tidstyv(db: Session, user: str):
    res = db.query(models.Tidstyv).filter_by(user=user).delete()
    db.commit()
    return res
