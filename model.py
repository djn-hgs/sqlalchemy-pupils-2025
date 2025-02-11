import sqlalchemy
import sqlalchemy.orm as orm

class Base(orm.DeclarativeBase, orm.MappedAsDataclass):
    pass


class Pupil(Base):
    __tablename__ = "pupil"
    pupil_id: orm.Mapped[int] = orm.mapped_column(init=False, primary_key=True, repr=False)
    first_name: orm.Mapped[str] = orm.mapped_column()
    last_name: orm.Mapped[str] = orm.mapped_column()
    house_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey('house.house_id'),
        init=False,
        repr=False
    )

    house: orm.Mapped['House'] = orm.relationship(default=None, back_populates="pupils", repr=False)
    subjects: orm.Mapped[list['Subject']] = orm.relationship(
        default_factory=list,
        secondary='pupil_subject',
        back_populates="pupils",
        repr=False
    )


class House(Base):
    __tablename__ = "house"
    house_id: orm.Mapped[int] = orm.mapped_column(init=False, primary_key=True, repr=False)
    name: orm.Mapped[str] = orm.mapped_column()

    pupils: orm.Mapped[list[Pupil]] = orm.relationship(default_factory=list, back_populates="house", repr=False)


class Subject(Base):
    __tablename__ = "subject"
    subject_id: orm.Mapped[int] = orm.mapped_column(init=False, primary_key=True, repr=False)
    name: orm.Mapped[str] = orm.mapped_column()

    pupils: orm.Mapped[list['Pupil']] = orm.relationship(
        default_factory=list,
        secondary='pupil_subject',
        back_populates="subjects",
        repr=False
    )


class PupilSubject(Base):
    __tablename__ = "pupil_subject"
    pupil_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey('pupil.pupil_id'),
        primary_key=True
    )
    subject_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey('subject.subject_id'),
        primary_key=True
    )
