from sqlalchemy import Column,Integer,String
from database import Base

class home(Base):
    __tablename__ = 'homeImages'

    id = Column(Integer,primary_key=True,index=True)
    image = Column(String(250))

class aboutUs(Base):
    __tablename__ = 'aboutUsImages'

    id = Column(Integer,primary_key=True,index=True)
    image = Column(String(250))

class offerings(Base):
    __tablename__ = 'offeringsImages'

    id = Column(Integer,primary_key=True,index=True)
    image = Column(String(250))

class resources(Base):
    __tablename__ = 'resourcesImages'

    id = Column(Integer,primary_key=True,index=True)
    image = Column(String(250))

class Foundation(Base):
    __tablename__ = 'foundation'

    id = Column(Integer,primary_key=True,index=True)
    img1 = Column(String(100))
    img2 = Column(String(100))
    title = Column(String(25),nullable=False)
    desc = Column(String(500),nullable=False)
    thickness = Column(String(50))
    background = Column(String(50))
    vein = Column(String(50))
    category = Column(String(20))

class Persephone(Base):
    __tablename__ = 'persephone'

    id = Column(Integer,primary_key=True,index=True)
    img1 = Column(String(100))
    img2 = Column(String(100))
    title = Column(String(25),nullable=False)
    desc = Column(String(500),nullable=False)
    thickness = Column(String(50))
    background = Column(String(50))
    vein = Column(String(50))
    category = Column(String(20))

class Midnight(Base):
    __tablename__ = 'midnight'

    id = Column(Integer,primary_key=True,index=True)
    img1 = Column(String(100))
    img2 = Column(String(100))
    title = Column(String(25),nullable=False)
    desc = Column(String(500),nullable=False)
    thickness = Column(String(50))
    background = Column(String(50))
    vein = Column(String(50))
    category = Column(String(20))

class Diffusion(Base):
    __tablename__ = 'diffusion'

    id = Column(Integer,primary_key=True,index=True)
    img1 = Column(String(100))
    img2 = Column(String(100))
    title = Column(String(25),nullable=False)
    desc = Column(String(500),nullable=False)
    thickness = Column(String(50))
    background = Column(String(50))
    vein = Column(String(50))
    category = Column(String(20))