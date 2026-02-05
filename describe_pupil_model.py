import datetime

import sqlalchemy
from sqlalchemy import orm as orm


class Base(orm.DeclarativeBase, orm.MappedAsDataclass):
    pass


class Pupil(Base):
    __tablename__ = 'pupil'

    pupil_id: orm.Mapped[int] = orm.mapped_column(primary_key=True, init=False)
    first_name: orm.Mapped[str] = orm.mapped_column()
    second_name: orm.Mapped[str] = orm.mapped_column()
    date_of_birth: orm.Mapped[datetime.date] = orm.mapped_column()
    house_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey('house.house_id'),
        init=False,
    )

    house: orm.Mapped['House'] = orm.relationship(
        back_populates='pupils',
        init=False,
        default=None,
    )

class House(Base):
    __tablename__ = 'house'

    house_id: orm.Mapped[int] = orm.mapped_column(primary_key=True, init=False)
    house_name: orm.Mapped[str] = orm.mapped_column()

    pupils: orm.Mapped[list[Pupil]] = orm.relationship(
        back_populates='house',
        init=False,
    )