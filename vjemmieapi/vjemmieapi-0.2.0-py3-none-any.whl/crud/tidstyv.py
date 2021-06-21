from sqlalchemy.sql.expression import desc
from .. import schemas, models
from sqlalchemy.orm import Session

# TODO: Refactor add/remove methods. Very similar.


def get_all_tidstyv(db: Session):
    return db.query(models.Tidstyv).order_by(desc(models.Tidstyv.stolen)).all()


def get_tidstyv_by_id(db: Session, user_id: str):
    return db.query(models.Tidstyv).filter_by(user_id=user_id).first()


def add_tidstyveri(db: Session, tidstyv: schemas.TidstyvIn):
    res = db.query(models.Tidstyv).filter_by(user_id=tidstyv.user_id).first()
    if res:
        res.stolen += tidstyv.stolen
    else:
        db.add(models.Tidstyv(user_id=tidstyv.user_id, stolen=tidstyv.stolen))
    db.commit()
    # NOTE: There has to be a better way?
    return db.query(models.Tidstyv).filter_by(user_id=tidstyv.user_id).first()


def remove_tidstyveri(db: Session, tidstyv: schemas.TidstyvIn):
    res = db.query(models.Tidstyv).filter_by(user_id=tidstyv.user_id).first()
    if not res:
        return
    res.stolen -= tidstyv.stolen
    if res.stolen < 0:
        res.stolen = 0
    db.commit()
    db.refresh(res)
    return res


def delete_tidstyv(db: Session, user_id: str):
    res = db.query(models.Tidstyv).filter_by(user_id=user_id).delete()
    db.commit()
    return res
