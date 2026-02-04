import sqlalchemy
import sqlalchemy.orm as orm
from old_examples import model as m

engine = sqlalchemy.create_engine("sqlite+pysqlite:///pupils.sqlite", echo=False)


with (orm.Session(engine) as s):
    # Create some houses

    tl = m.House(name="The Lodge")
    qg = m.House(name="Queensgate")

    # Add houses to the session one at a time

    s.add(tl)
    s.add(qg)

    # Create some subjects

    sub_cs = m.Subject(name="Computer Science")
    sub_m = m.Subject(name="Mathematics")
    sub_p = m.Subject(name="Physics")
    sub_ec = m.Subject(name="Economics")

    # Add subjects all at once

    s.add_all(
        [
            sub_cs,
            sub_m,
            sub_p,
            sub_ec
        ]
    )

    # Create some pupils

    pupil_aa = m.Pupil(first_name="Aadith", last_name="Ajay")
    pupil_cs = m.Pupil(first_name="Charlie", last_name="Suss", house=qg)
    pupil_lw = m.Pupil(first_name="Lindy", last_name="Wang")

    print(pupil_aa)
    print(pupil_cs)

    pupil_aa.house = tl
    pupil_lw.house = qg

    print(pupil_aa)

    # Now assign some subjects to the pupils

    pupil_aa.subjects.append(sub_m)
    pupil_aa.subjects.append(sub_cs)
    pupil_cs.subjects = [sub_m, sub_cs, sub_ec]
    pupil_lw.subjects = [sub_m, sub_cs, sub_p]

    # Notice how we describe the many-to-many relationship
    # by working with lists

    s.add_all(
        [
            pupil_aa,
            pupil_cs,
            pupil_lw
        ]
    )

    s.commit()

    # We can do this more often if we like