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
        # Determines whether the field is
        # required as an argument at initialisation
        # ie it is a parameter of `Pupil.__init__`

        primary_key=True,
        # If the field is a primary key then it is auto-numbered

        repr=False
        # Determines whether the field id is included in
        # the output of `Pupil.__repr__`
    )
    first_name: orm.Mapped[str] = orm.mapped_column()
    # Notice the way that `orm.DeclaritiveBase` maps the
    # `str` type to the right kind of sqlite field
    # And `orm.MappedAsDataclass` manages the attributes
    # and `Pupil.__repr__` output for us.

    last_name: orm.Mapped[str] = orm.mapped_column()
    house_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey('house.house_id'),
        # This is how we declare a foreign key

        init=False,
        repr=False
    )

    house: orm.Mapped['House'] = orm.relationship(
        # This is how we link the `Pupil` and `House` classes
        # There should be a matching field in the `House` class
        # This is a many-to-one relationship, so the pupil only
        # has a single house assigned to them.

        default=None,
        # Gives the default value of the field

        back_populates="pupils",
        # Tells `sqlalchemy` what the corresponding field is
        # in the `House` class

        repr=False
    )

    subjects: orm.Mapped[list['Subject']] = orm.relationship(
        # This is a many-to-many relationship so each pupil
        # can be assigned many `Subject` objects in a `list`

        default_factory=list,
        # A `default_factory` tells Python how to initialise
        # the field - we can't just use `[]` because this is a
        # mutable data type

        secondary='pupil_subject',
        # Tells `sqlalchemy` what table we are using to handle
        # the many-to-many relationship

        back_populates="pupils",
        # This will have a matching attribute in the `Subject` class

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
        # This is the other half of the relationship
        # declared in the `Pupil` class.
        # The relationship is many-to-one and so the `pupils`
        # attribute contains a list of `Pupil` objects.

        default_factory=list,
        # The `list` data type cannot be declared using the
        # mutable `[]` and so we tell it to use the `list`
        # factory.

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
        # This is the other half of the many-to-many
        # relationship declared in the `Pupil` class

        default_factory=list,
        secondary='pupil_subject',
        back_populates="subjects",
        # This has to be the same attribute as declared
        # in the `Pupil` class

        repr=False
    )


class PupilSubject(Base):
    __tablename__ = "pupil_subject"

    # This is the link table to facilitate the
    # many-to-many relationship. We don't need this to
    # be a class and can create the table at a lower
    # level in `sqlalchemy`, but this approach is sufficient.
    # There will be methods `PupilSubject.__init__` and
    # `PupilSubject.__repr__` but we don't need them.
    # If we are to use the class in any way then the fields
    # will need to have `init=False` added to them.

    pupil_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey('pupil.pupil_id'),
        primary_key=True
    )
    subject_id: orm.Mapped[int] = orm.mapped_column(
        sqlalchemy.ForeignKey('subject.subject_id'),
        primary_key=True
    )
