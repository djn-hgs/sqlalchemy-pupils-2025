from typing import Optional

import sqlalchemy
import sqlalchemy.orm as orm


# `orm.DeclarativeBase` does all the magic for us
# `orm.MappedAsDataclass` enables us to use class
# declarations in the style of `@dataclass`

class Base(orm.DeclarativeBase, orm.MappedAsDataclass):
    pass


# Describe our classes

class Pupil(Base):
    __tablename__ = "pupil"

    pupil_id: orm.Mapped[int] = orm.mapped_column(
        init=False,
        primary_key=True,
        repr=False
    )
    first_name: orm.Mapped[str] = orm.mapped_column()
    last_name: orm.Mapped[str] = orm.mapped_column()
    house_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey('house.house_id'),
        repr=False,
        init=False
    )


    house: orm.Mapped['House'] = orm.relationship(
        default=None,   # This is enough to make the attribute optional
        back_populates="pupils",
        repr=True
    )

    subjects: orm.Mapped[list['Subject']] = orm.relationship(
        default_factory=list,
        secondary='pupil_subject',
        back_populates="pupils",
        repr=False
    )


class House(Base):
    __tablename__ = "house"

    house_id: orm.Mapped[int] = orm.mapped_column(
        init=False,
        primary_key=True,
        repr=False
    )
    name: orm.Mapped[str] = orm.mapped_column()

    pupils: orm.Mapped[list[Pupil]] = orm.relationship(
        default_factory=list,
        back_populates="house",
        repr=False
    )


class Subject(Base):
    __tablename__ = "subject"

    subject_id: orm.Mapped[int] = orm.mapped_column(
        init=False,
        primary_key=True,
        repr=False
    )
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
