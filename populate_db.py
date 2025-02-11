import sqlalchemy
import sqlalchemy.orm as orm
import model

engine = sqlalchemy.create_engine("sqlite+pysqlite:///pupils.sqlite", echo=False)


with orm.Session(engine) as session:
    the_lodge = model.House(name="The Lodge")
    session.add(the_lodge)
    queensgate = model.House(name="Queensgate")

    pupil1 = model.Pupil(first_name="Aadith", last_name="Ajay", house=the_lodge)
    pupil2 = model.Pupil(first_name="Charlie", last_name="Suss", house=queensgate)
    pupil3 = model.Pupil(first_name="Lindy", last_name="Wang", house=queensgate)
    session.add(pupil1)
    session.add(pupil2)

    print(pupil1.house.name)
    print(queensgate.pupils)

    session.commit()
