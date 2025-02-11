import sqlalchemy
import sqlalchemy.orm as orm

class Base(orm.DeclarativeBase, orm.MappedAsDataclass):
    pass

class Pupil(Base):
    __tablename__ = "pupil"
    id: orm.Mapped[int] = orm.mapped_column(init=False, primary_key=True, repr=False)
    first_name: orm.Mapped[str] = orm.mapped_column()
    last_name: orm.Mapped[str] = orm.mapped_column()
    house_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey('house.house_id'),
        init=False,
        repr=False
    )

    house: orm.Mapped['House'] = orm.relationship(default=None, back_populates="pupils", repr=False)

class House(Base):
    __tablename__ = "house"
    house_id: orm.Mapped[int] = orm.mapped_column(init=False, primary_key=True, repr=False)
    name: orm.Mapped[str] = orm.mapped_column()

    pupils: orm.Mapped[list[Pupil]] = orm.relationship(default_factory=list, back_populates="house", repr=False)


