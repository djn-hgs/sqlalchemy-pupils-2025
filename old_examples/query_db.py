import sqlalchemy
import sqlalchemy.orm as orm
from old_examples import model

engine = sqlalchemy.create_engine("sqlite+pysqlite:///pupils.sqlite", echo=False)


with (orm.Session(engine) as s):

    # The print statements should describe what we're doing

    print('Get all houses\n')

    # houses = session.query(model.House).all()
    qry = sqlalchemy.select(model.House)
    houses = s.scalars(qry).all()

    print(houses)

    # This needs a bit of thought - this is a query
    # but we are describing the query using the ORM

    print('\nGet the ORM object for maths\n')

    qry = (
        sqlalchemy
        .select(model.Subject)
        .where(model.Subject.name == "Mathematics")
        )
    maths = s.scalar(qry)

    print(maths)

    # Now we can see how the relationships are managed

    print('\nList all students of maths\n')

    print(maths.pupils)

    print('\nGet the ORM object for Queensgate\n')

    # house_qg = session.query(model.House).where(model.House.name == "Queensgate").one()

    query = (
        sqlalchemy
        .select(model.House)
        .where(model.House.name == "Queensgate")
        )

    house_qg = s.scalar(query)

    print(house_qg)

    print('\nList all students in Queensgate\n')

    print(house_qg.pupils)

    print('\nFind all students who study maths\n')

    # This is a huge query - how to separate... ?

    qry = (
        sqlalchemy
        .select(model.Pupil)
        .join(model.PupilSubject)
        .join(model.Subject)
        .filter(model.Subject.name == "Mathematics")
        )
    maths_pupils = s.scalars(qry).all()


    print(maths_pupils)