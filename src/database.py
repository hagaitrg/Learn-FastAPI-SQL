import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm
from sqlalchemy.sql.expression import false

SQLACLHEMY_DATABASE_URL = "sqlite:///./database.db"

engine = sql.create_engine(
    SQLACLHEMY_DATABASE_URL, connection_args={"check_same_thread":false}
)

Sessionlocal = orm.session(autocommit=false, autoflash=false, bind=engine)

Base = declarative.declarative_base()

