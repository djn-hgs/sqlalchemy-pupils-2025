# SQLalchemy updated for standard use in 2025

Things have changed a bit again.

So `sqlalchemy.orm.Mapped` is now a very effective way to declare the python type of an attribute (using type-hinting) and sqlalchemy will then decide what the correct type should be at the engine (SQL) level.

And if, like me, you were struggling to deal with the use of `@dataclass` headers because it wasn't clear how to include/exclude defaults from the `__init__` method or exclude attributes from the `__repr__` method then that is also now solved:
- we should be deriving `Base` from `sqlalchemy.orm.MappedAsDataclass` (or something like that) rather than using the decorator (though there is an orm equivalent available per class)
- we can include an `init` and `default` keyword in the field descriptor, so `init=False` and `default=None` will not expect an attribute and set a default value 
- we can include `repr=False` in our field descriptions to stop them being printed

Relationships are a bit spooky now, but seem to work well with the `Mapped` approach. See my code, but here were a couple of points that I need not to forget:
- `default` and `default_factory` need to be declared
- when the relationship column is `Mapped[List[Class]]` then `default_factory=list` is usually useful
- I need to use `back_populates` and get out of the old-school habit of using the non-symmetric `backref` which doesn't work in this setup
