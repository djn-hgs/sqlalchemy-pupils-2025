from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

# 1) Point this to your Chinook .sqlite file
engine = create_engine("sqlite:///chinook.sqlite", echo=False, future=True)

# 2) Reflect tables into ORM classes automatically
Base = automap_base()
Base.prepare(autoload_with=engine)

print(Base.classes.keys())

# Reflected classes (names come from table names)
Album = Base.classes.albums
Artist = Base.classes.artists
Track = Base.classes.tracks
Invoice = Base.classes.invoices
InvoiceLine = Base.classes.invoice_items
Customer = Base.classes.customers
Employee = Base.classes.employees
Genre = Base.classes.genres
MediaType = Base.classes.media_types
Playlist = Base.classes.playlists

# 3) Query with ORM
with Session(engine) as session:
    # Example A: First 5 artists
    artists = session.execute(select(Artist)).scalars().all()
    artists = sorted(artists, key=lambda a: a.Name)
    for a in artists:
        print(a.ArtistId, a.Name)

    # # Example B: Albums by a specific artist
    # albums = (
    #     session.query(Album)
    #     .join(Artist, Album.ArtistId == Artist.ArtistId)
    #     .filter(Artist.Name == "AC/DC")
    #     .all()
    # )
    # print([al.Title for al in albums])
    #
    # # Example C: Top 10 tracks by unit price (descending)
    # top_tracks = (
    #     session.query(Track.Name, Track.UnitPrice)
    #     .order_by(Track.UnitPrice.desc())
    #     .limit(10)
    #     .all()
    # )
    # print(top_tracks)
    #
    # # Example D: Revenue by country
    # rev_by_country = (
    #     session.query(Invoice.BillingCountry, func.sum(Invoice.Total).label("Revenue"))
    #     .group_by(Invoice.BillingCountry)
    #     .order_by(func.sum(Invoice.Total).desc())
    #     .all()
    # )
    # for country, rev in rev_by_country:
    #     print(country, rev)