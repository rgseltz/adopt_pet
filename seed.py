from models import Pet, db
from app import app

db.drop_all()
db.create_all()

p1 = Pet(name="Scruff", age=2, species="dog")
p2 = Pet(name="Bae", age=5, species="cat")
p3 = Pet(name="Missy", age=1, species="cat")
p4 = Pet(name="Alfred", age=7, species="dog")
p5 = Pet(name="Enzo", age=1, species="girble")

db.session.add_all([p1, p2, p3, p4, p5])
db.session.commit()
