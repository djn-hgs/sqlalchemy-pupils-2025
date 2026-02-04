import datetime

import sqlalchemy
from sqlalchemy import orm as orm
import describe_pupil_model as m

engine = sqlalchemy.create_engine('sqlite+pysqlite:///pupil_db.sqlite', echo=True)

with orm.Session(engine) as session:

    with session.begin():
        eg = m.House(
            house_name="Eastgate",
        )

        session.add(eg)

        hwe = m.Pupil(
            first_name='Henry',
            second_name='Miller Evans',
            date_of_birth=datetime.date(1999, 12, 31),
        )

        dj = m.Pupil(
            first_name='Dean',
            second_name='Jones',
            date_of_birth=datetime.date(1999, 12, 31),
        )

        session.add(hwe)
        session.add(dj)

