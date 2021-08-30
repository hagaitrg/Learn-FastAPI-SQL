import sqlalchemy as sql
import sqlalchemy.orm as orm
from sqlalchemy.sql.functions import user
import database as database
import datetime as dt

class User(database.Base):
    __tablename__ = "users"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    email =sql.Column(sql.String, unique=True, index=True)
    hashed_password = sql.Column(sql.String)
    is_active = sql.Column(sql.Boolean, default=True)

    posts = orm.relationship("Post", back_populates='owner')

class Post(database.Base):
    __tablename__ = "posts"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    title = sql.Column(sql.String, index=True)
    content = sql.Column(sql.String, index=True)
    owner_id = sql.Column(sql.Integer, sql.ForeignKey("users.id"))
    date_created = sql.Column(sql.DateTime, default=dt.datetime.now)
    date_updated = sql.Column(sql.DateTime, default=dt.datetime.now)

    owner = orm.relationship("User", back_populates="posts")