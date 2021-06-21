from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from ..db import Base


class Subreddit(Base):
    __tablename__ = "RedditSubreddit"

    subreddit = Column(String, primary_key=True, index=True)
    is_text = Column(Boolean)
    submitter = Column(String)
    submitted = Column(DateTime, default=None)
    aliases = relationship("SubredditAlias")


class SubredditAlias(Base):
    __tablename__ = "RedditSubredditAlias"

    alias = Column(String, primary_key=True, index=True)
    subreddit = Column(String, ForeignKey("RedditSubreddit.subreddit"))
