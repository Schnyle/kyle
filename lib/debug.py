from db.models import Base, KyleItem, KyleCart
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine('sqlite:///db/kyle.db')
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()

    kyle1 = session.query(KyleItem).first()

    kyle_cart = KyleCart()

    import ipdb; ipdb.set_trace()