#!/usr/bin/env python3

# Script goes here!
from models import Base, Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


google = Company(name="Google", founding_year=1998)
meta = Company(name="Meta", founding_year=2004)
alice = Dev(name="Alice")
bob = Dev(name="Bob")

session.add_all([google, meta, alice, bob])
session.commit()
f1 = Freebie(item_name="Sticker", value=2, company=google, dev=alice)
f2 = Freebie(item_name="T-shirt", value=20, company=google, dev=bob)
f3 = Freebie(item_name="Water Bottle", value=10, company=meta, dev=alice)

session.add_all([f1, f2, f3])
session.commit()
print("Seeded test data!")