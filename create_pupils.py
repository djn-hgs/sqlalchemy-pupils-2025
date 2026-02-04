import datetime

import sqlalchemy
import sqlalchemy.orm as orm
import describe_pupil_model as m

engine = sqlalchemy.create_engine('sqlite+pysqlite:///pupil_db.sqlite', echo=False)

with orm.Session(engine) as session:

    with session.begin():
        eg = m.House(
            house_name="Eastgate",
        )

        hme = m.Pupil(
            first_name='Henry',
            second_name='Miller Evans',
            date_of_birth=datetime.date(1999, 12, 31),
        )

        dj = m.Pupil(
            first_name='Dean',
            second_name='Jones',
            date_of_birth=datetime.date(1999, 12, 31),
        )

        session.add(hme)
        session.add(dj)

        dj.house = eg

        print(hme)
        print(dj)

        print(eg)

    # print(hme)
    # print(dj)
    #
    # print(eg)

    with session.begin():
        cs = m.Subject("Computer Science")
        fm = m.Subject("Further Maths")

        hme.subjects = [cs, fm]

        fm.pupils.append(dj)



    print(fm)
    print(cs)
