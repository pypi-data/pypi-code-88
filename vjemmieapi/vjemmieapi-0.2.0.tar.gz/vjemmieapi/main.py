from typing import List, Optional, Union
from vjemmieapi.schemas.goodmorning import GoodmorningOut
from vjemmieapi.schemas.skribbl import SkribblStats
from .schemas.mediatype import MediaTypeIn

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .db import engine, get_db
from .exceptions import (
    add_exception_handlers,
    HTTPNotFoundException,
    ResourceExistsException,
)

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
add_exception_handlers(app)


@app.get("/gamingmoments", response_model=List[schemas.GamingMomentsOut])
async def get_all_gamingmoments(
    limit: Optional[int] = None, db: Session = Depends(get_db)
):
    return crud.get_gamingmoments(db, limit)


@app.get("/gamingmoments/{user_id}", response_model=schemas.GamingMomentsOut)
async def get_user_gamingmoments(user_id: str, db: Session = Depends(get_db)):
    r = crud.get_gamingmoments_by_id(db, user_id)
    if not r:
        raise HTTPNotFoundException("User")
    return r


@app.post(
    "/gamingmoments/{user_id}", response_model=schemas.GamingMomentsOut, status_code=201
)
async def add_or_decrease_gamingmoments(
    user_id: str, decrease: bool = False, db: Session = Depends(get_db)
):
    if decrease:
        return crud.decrease_gamingmoments(db, user_id)
    return crud.add_gamingmoment(db, user_id)


@app.delete("/gamingmoments/{user_id}", status_code=204)
async def delete_gamingmoments(user_id: str, db: Session = Depends(get_db)):
    res = crud.delete_gamingmoments(db, user_id)
    if not res:
        raise HTTPNotFoundException("User")


@app.get("/skribbl/words", response_model=List[schemas.SkribblOut])
async def get_skribbl_all(
    limit: Optional[int] = None,
    user_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    return crud.skribbl_get_words(db, limit=limit, user_id=user_id)


@app.get("/skribbl/words/{word}", response_model=schemas.SkribblOut)
async def get_skribbl_word(word: str, db: Session = Depends(get_db)):
    w = crud.skribbl_get_word(db, word)
    if not w:
        raise HTTPNotFoundException("Word")
    return w


@app.post("/skribbl/words", response_model=schemas.SkribblAddOut, status_code=201)
async def add_skribbl(words: schemas.SkribblIn, db: Session = Depends(get_db)):
    # TODO: refactor. How can we bulk add while discarding duplicates?
    added = []
    failed = []
    for word in words.words:
        try:
            r = crud.skribbl_add_word(db, word, words.submitter)
            added.append(r.word)
        except IntegrityError:
            failed.append(word)
            db.rollback()
    return {"added": added, "failed": failed}


@app.delete("/skribbl/words/{word}", status_code=204)
async def delete_skribbl_word(word: str, db: Session = Depends(get_db)):
    r = crud.skribbl_delete_word(db, word)
    if not r:
        raise HTTPNotFoundException("Word")


@app.get("/skribbl/stats/{user_id}", response_model=schemas.SkribblAggregateStats)
async def get_skribbl_stats_user(user_id: str, db: Session = Depends(get_db)):
    r = crud.skribbl_get_user_stats(db, user_id)
    if not r:
        raise HTTPNotFoundException("Skribbl stats")
    return r


@app.get("/skribbl/stats", response_model=List[schemas.SkribblAuthorStats])
async def get_skribbl_stats(db: Session = Depends(get_db)):
    r = crud.skribbl_get_stats(db)
    if not r:
        raise HTTPNotFoundException("Skribbl stats")
    return r


@app.get("/skribbl/stats-aggregate", response_model=schemas.SkribblAggregateStats)
async def get_skribbl_stats_aggregate(db: Session = Depends(get_db)):
    r = crud.skribbl_get_stats_aggregate(db)
    if not r:
        raise HTTPNotFoundException("Skribbl stats")
    return r


@app.get("/reddit/subreddits", response_model=List[schemas.SubredditOut])
async def get_subreddits(text: bool = False, db: Session = Depends(get_db)):
    if text:
        return crud.get_text_subreddits(db)
    return crud.get_all_subreddits(db)


@app.post("/reddit/subreddits", status_code=201, response_model=schemas.SubredditOut)
async def add_subreddit(subreddit: schemas.SubredditIn, db: Session = Depends(get_db)):
    return crud.add_subreddit(db, subreddit)


@app.get("/reddit/subreddits/{subreddit}", response_model=schemas.SubredditOut)
async def get_subreddit(subreddit: str, db: Session = Depends(get_db)):
    return crud.get_subreddit_by_name(db, subreddit)


@app.delete("/reddit/subreddits/{subreddit}", status_code=204)
async def delete_subreddit(subreddit: str, db: Session = Depends(get_db)):
    return crud.delete_subreddit_by_name(db, subreddit)


@app.put("/reddit/subreddits/{subreddit}")
async def modify_subreddit(
    subreddit: str,
    body: schemas.SubredditUpdate,
    db: Session = Depends(get_db),
):
    return crud.modify_subreddit(db, subreddit, body)


@app.get("/tidstyveri", response_model=List[schemas.TidstyvOut])
async def get_all_tidstyv(db: Session = Depends(get_db)):
    return crud.get_all_tidstyv(db)


@app.get("/tidstyveri/{user_id}", response_model=schemas.TidstyvOut)
async def get_tidstyv_by_id(user_id: str, db: Session = Depends(get_db)):
    r = crud.get_tidstyv_by_id(db, user_id)
    if not r:
        raise HTTPNotFoundException("User")
    return r


@app.post("/tidstyveri", response_model=schemas.TidstyvOut, status_code=201)
async def change_tidstyveri(
    tidstyv: schemas.TidstyvIn, decrease: bool = False, db: Session = Depends(get_db)
):
    if decrease:
        return crud.remove_tidstyveri(db, tidstyv)
    else:
        return crud.add_tidstyveri(db, tidstyv)


@app.delete("/tidstyveri/{user_id}", status_code=204)
async def remove_tidstyveri(user_id: str, db: Session = Depends(get_db)):
    res = crud.delete_tidstyv(db, user_id)
    if not res:
        raise HTTPNotFoundException("User")


@app.get("/pfm/memes", response_model=List[schemas.PFMMemeOut])
async def get_pfm_memes(topic: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.get_pfm_memes(db, topic)


@app.get("/pfm/memes/{id}", response_model=schemas.PFMMemeOut)
async def get_pfm_meme_by_id(id: int, db: Session = Depends(get_db)):
    r = crud.get_pfm_meme_by_id(db, id)
    if not r:
        raise HTTPNotFoundException("Meme")
    return r


@app.post("/pfm/memes", status_code=201)
async def add_pfm_meme(meme: schemas.PFMMemeIn, db: Session = Depends(get_db)):
    return crud.add_pfm_meme(db, meme)


@app.get("/mediatypes", response_model=List[schemas.MediaTypeOut])
async def get_media_types(db: Session = Depends(get_db)):
    return crud.get_media_types(db)


@app.get("/mediatypes/{media_type}", response_model=schemas.MediaTypeOut)
async def get_media_type_by_name(media_type: str, db: Session = Depends(get_db)):
    return crud.get_media_type_by_name(db, media_type)


@app.post("/mediatypes", status_code=201)
async def add_media_type(
    media_type: schemas.MediaTypeIn, db: Session = Depends(get_db)
):
    return crud.add_media_type(db, media_type)


@app.delete("/mediatypes/{media_type}", status_code=204)
async def delete_media_type(media_type: str, db: Session = Depends(get_db)):
    return crud.delete_media_type(db, media_type)


@app.get("/goodmorning")
async def get_goodmorning_random(db: Session = Depends(get_db)):
    return crud.get_goodmorning_random(db)


@app.get("/goodmorning/all", response_model=List[GoodmorningOut])
async def get_goodmorning_all(db: Session = Depends(get_db)):
    return crud.get_goodmorning_all(db)


@app.post("/goodmorning", status_code=201, response_model=schemas.GoodmorningOut)
async def add_goodmorning_target(
    target: schemas.GoodmorningIn, db: Session = Depends(get_db)
):
    return crud.add_goodmorning_target(db, target)


@app.delete("/goodmorning", status_code=204)
async def remove_goodmorning_target(target: str, db: Session = Depends(get_db)):
    r = crud.remove_goodmorning_target(db, target)
    if not r:
        raise HTTPNotFoundException("Target")
