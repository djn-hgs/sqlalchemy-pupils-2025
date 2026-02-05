import datetime
from typing import Optional

import sqlalchemy
from sqlalchemy import orm as orm


class Base(orm.DeclarativeBase, orm.MappedAsDataclass):
    pass


class Pupil(Base):
    __tablename__ = 'pupil'

    pupil_id: orm.Mapped[int] = orm.mapped_column(
        primary_key=True,
        init=False,
        repr=False,
    )
    first_name: orm.Mapped[str] = orm.mapped_column()
    second_name: orm.Mapped[str] = orm.mapped_column()
    date_of_birth: orm.Mapped[datetime.date] = orm.mapped_column()
    house_id: orm.Mapped[Optional[int]] = orm.mapped_column(
        sqlalchemy.ForeignKey('house.house_id'),
        init=False,
    )

    house: orm.Mapped[House] = orm.relationship(
        default=None,
        back_populates='pupils',
        init=False,
    )

    subjects: orm.Mapped[list['Subject']] = orm.relationship(
        secondary='pupil_subject',
        back_populates='pupils',
        default_factory=list,
    )

class House(Base):
    __tablename__ = 'house'

    house_id: orm.Mapped[int] = orm.mapped_column(
        primary_key=True, init=False)
    house_name: orm.Mapped[str] = orm.mapped_column()

    pupils: orm.Mapped[list[Pupil]] = orm.relationship(
        back_populates='house',
        init=False,
    )

class Subject(Base):
    __tablename__ = 'subject'

    subject_id: orm.Mapped[int] = orm.mapped_column(
        primary_key=True,
        init=False,
    )

    name: orm.Mapped[str] = orm.mapped_column()

    pupils: orm.Mapped[list[Pupil]] = orm.relationship(
        secondary='pupil_subject',
        back_populates='subjects',
        default_factory=list,
    )

class PupilSubject(Base):

    __tablename__ = 'pupil_subject'

    pupil_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey('pupil.pupil_id'),
        primary_key=True,
    )

    subject_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey('subject.subject_id'),
        primary_key=True,
    )
