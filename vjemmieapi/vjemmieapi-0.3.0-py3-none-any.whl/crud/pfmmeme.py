from typing import Optional
from sqlalchemy.orm.session import Session

from .. import models, schemas


def get_pfm_memes(db: Session, topic: Optional[str]):
    q = db.query(models.PFMMeme)
    if topic:
        q = q.filter_by(topic=topic)
    return q.all()


def get_pfm_meme_by_id(db: Session, id: int):
    return db.query(models.PFMMeme).filter_by(id=id).first()


def add_pfm_meme(db: Session, meme: schemas.PFMMemeIn):
    db.add(
        models.PFMMeme(
            topic=meme.topic,
            title=meme.title,
            description=meme.description,
            content=meme.content,
            media_type=meme.media_type,
        )
    )
    db.commit()
