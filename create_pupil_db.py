import sqlalchemy

from describe_pupil_model import Base

engine = sqlalchemy.create_engine('sqlite+pysqlite:///pupil_db.sqlite', echo=True)

Base.metadata.create_all(engine)
