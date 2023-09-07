from faker import Faker
import random
from app.db import Base, engine, session
from app.models import Member, Route, Matatu

komatsu = Matatu(number_plate='KDM 245R', capacity=41, member_id=23, route_id=105)

komatsu = session.query(Matatu).first()




if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print(komatsu)