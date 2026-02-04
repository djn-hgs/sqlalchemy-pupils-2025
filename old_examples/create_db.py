import sqlalchemy
import model

engine = sqlalchemy.create_engine("sqlite+pysqlite:///pupils.sqlite", echo=True)

model.Base.metadata.create_all(engine)