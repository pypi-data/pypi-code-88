from typing import List, Optional, Union
from vjemmieapi.schemas.reddit import SubredditUpdate
from sqlalchemy.orm import Session

from .. import models, schemas


def get_all_subreddits(db: Session):
    return db.query(models.Subreddit).all()


def get_subreddit_by_name(db: Session, subreddit: str):
    return db.query(models.Subreddit).filter_by(subreddit=subreddit).first()


def get_text_subreddits(db: Session):
    return db.query(models.Subreddit).filter_by(is_text=True).all()


def add_subreddit(db: Session, subreddit: schemas.SubredditIn) -> models.Subreddit:
    db.add(
        models.Subreddit(
            subreddit=subreddit.subreddit,
            is_text=subreddit.is_text,
            submitter=subreddit.submitter,
            aliases=[
                models.SubredditAlias(
                    alias=alias,
                    subreddit=subreddit.subreddit,
                )
                for alias in subreddit.aliases
            ],
        )
    )
    db.commit()
    return db.query(models.Subreddit).filter_by(subreddit=subreddit.subreddit).first()


def delete_subreddit_by_name(db: Session, subreddit: str):
    db.query(models.Subreddit).filter_by(subreddit=subreddit).delete()
    db.commit()


def modify_subreddit(
    db: Session,
    subreddit: str,
    body: schemas.SubredditUpdate,
):
    if body.aliases:
        _modify_subreddit_aliases(db, subreddit, body.aliases)
    elif body.is_text is not None:
        _modify_subreddit(db, subreddit, body)


def _modify_subreddit_aliases(
    db: Session, subreddit: str, aliases: List[schemas.SubredditAliasUpdate]
):
    res = db.query(models.Subreddit).filter_by(subreddit=subreddit).first()
    if not res:
        return
    for alias in aliases:
        if alias.remove:
            db.query(models.SubredditAlias).filter_by(
                subreddit=subreddit, alias=alias.alias
            ).delete()
        else:
            res.aliases.append(
                models.SubredditAlias(alias=alias.alias, subreddit=res.subreddit)
            )
    db.commit()


def _modify_subreddit(db: Session, subreddit: str, body: schemas.SubredditUpdate):
    res = db.query(models.Subreddit).filter_by(subreddit=subreddit).first()
    if not res:
        return
    res.is_text = body.is_text
    db.commit()
