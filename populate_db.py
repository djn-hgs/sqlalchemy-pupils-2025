import sqlalchemy
import sqlalchemy.orm as orm
import model

engine = sqlalchemy.create_engine("sqlite+pysqlite:///pupils.sqlite", echo=False)


with orm.Session(engine) as session:
    # Create some houses

    tl = model.House(name="The Lodge")
    qq = model.House(name="Queensgate")
    session.add(tl)
    session.add(qq)

    # Create some subjects

    sub_cs = model.Subject(name="Computer Science")
    sub_m = model.Subject(name="Mathematics")
    sub_p = model.Subject(name="Physics")
    sub_ec = model.Subject(name="Economics")
    session.add_all([sub_cs, sub_m, sub_p, sub_ec])

    # Create some pupils

    pupil_aa = model.Pupil(first_name="Aadith", last_name="Ajay", house=tl)
    pupil_aa.subjects = [sub_m, sub_cs]
    pupil_cs = model.Pupil(first_name="Charlie", last_name="Suss", house=qq)
    pupil_cs.subjects = [sub_m, sub_cs, sub_ec]
    pupil_lw = model.Pupil(first_name="Lindy", last_name="Wang", house=qq)
    pupil_lw.subjects = [sub_m, sub_cs, sub_p]

    session.add_all([pupil_aa, pupil_cs, pupil_lw])

    session.commit()
