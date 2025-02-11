import sqlalchemy
import sqlalchemy.orm as orm
import model

engine = sqlalchemy.create_engine("sqlite+pysqlite:///pupils.sqlite", echo=False)


with (orm.Session(engine) as session):
    print('Get all houses')
    houses = session.query(model.House)

    for house in houses:
        print(house)

    print('Get the ORM object for maths')

    maths = session.query(model.Subject).where(model.Subject.name == "Mathematics").one()

    print(maths)

    print('List all students of maths')

    print(maths.pupils)

    print('Get the ORM object for Queensgate')

    house_qg = session.query(model.House).where(model.House.name == "Queensgate").one()

    print(house_qg)

    print('List all students in Queensgate')

    print(house_qg.pupils)
