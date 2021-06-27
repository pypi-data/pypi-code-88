from sqlalchemy.orm import Session
from .. import schemas, models


def add_media_type(db: Session, media_type: schemas.MediaTypeIn):
    db.add(
        models.MediaType(
            media_type=media_type.media_type, description=media_type.description
        )
    )
    db.commit()


def get_media_types(db: Session):
    return db.query(models.MediaType).all()


def get_media_type_by_name(db: Session, name: str):
    return db.query(models.MediaType).filter_by(media_type=name).first()


def delete_media_type(db: Session, media_type: str):
    res = db.query(models.MediaType).filter_by(media_type=media_type).delete()
    db.commit()
    return res
