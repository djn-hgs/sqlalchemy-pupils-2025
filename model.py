import sqlalchemy
import sqlalchemy.orm as orm

class Base(orm.DeclarativeBase):
    pass

class Pupil(Base):
    __tablename__ = "pupil"
    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    first_name: orm.Mapped[str] = orm.mapped_column()
    last_name: orm.Mapped[str] = orm.mapped_column()
    house_id: orm.Mapped[int] = orm.mapped_column(sqlalchemy.ForeignKey('house.house_id'))


class House(Base):
    __tablename__ = "house"
    house_id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    name: orm.Mapped[str] = orm.mapped_column()

    pupils = orm.relationship(Pupil, backref='house')


