import datetime
from typing import Optional

import sqlalchemy
import sqlalchemy.orm as orm



class Base(orm.DeclarativeBase, orm.MappedAsDataclass):
    pass


class Pupil(Base):
    __tablename__ = 'pupil'

    pupil_id: orm.Mapped[int] = orm.mapped_column(
        primary_key=True,
        init=False,
    )
    first_name: orm.Mapped[str] = orm.mapped_column()
    second_name: orm.Mapped[str] = orm.mapped_column()
    date_of_birth: orm.Mapped[datetime.date] = orm.mapped_column()
    house_id: orm.Mapped[Optional[int]] = orm.mapped_column(
        sqlalchemy.ForeignKey('house.house_id'),
        init=False,
    )

    house: orm.Mapped['House'] = orm.relationship(
        default=None,
        back_populates='pupils',
    )

    subjects: orm.Mapped[list['Subject']] = orm.relationship(
        default_factory=list,
        back_populates='pupils',
        secondary='subject_pupil',
    )

class House(Base):
    __tablename__ = 'house'

    house_id: orm.Mapped[int] = orm.mapped_column(
        primary_key=True,
        init=False
    )
    house_name: orm.Mapped[str] = orm.mapped_column()

    pupils: orm.Mapped[list[Pupil]] = orm.relationship(
        default_factory=list,
        back_populates='house',
    )

class Subject(Base):
    __tablename__ = 'subject'

    subject_id: orm.Mapped[int] = orm.mapped_column(
        primary_key=True,
        init=False
    )
    name: orm.Mapped[str] = orm.mapped_column()

    pupils: orm.Mapped[list[Pupil]] = orm.relationship(
        default_factory=list,
        back_populates='subjects',
        secondary='subject_pupil',
    )


class SubjectPupil(Base):
    __tablename__ = 'subject_pupil'

    subject_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey("subject.subject_id"),
        primary_key=True,
    )
    pupil_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey("pupil.pupil_id"),
        primary_key=True,
    )