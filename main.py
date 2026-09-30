from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import (
    home,
    aboutUs,
    offerings,
    resources,
    Foundation,
    Persephone,
    Midnight,
    Diffusion,
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://quartzkraft-frontend.vercel.app/",],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def working():
    return {"mesg": "API is working"}


@app.get("/homeImages")
def homeImages(db: Session = Depends(get_db)):
    return db.query(home).all()


@app.get("/aboutUsImages")
def aboutUsImages(db: Session = Depends(get_db)):
    return db.query(aboutUs).all()


@app.get("/offeringsImages")
def offeringsImages(db: Session = Depends(get_db)):
    return db.query(offerings).all()


@app.get("/resourcesImages")
def resourcesImages(db: Session = Depends(get_db)):
    return db.query(resources).all()


@app.get("/collections")
def collections(db: Session = Depends(get_db)):
    res1 = db.query(Foundation).limit(3).all()
    res2 = db.query(Persephone).limit(3).all()
    res3 = db.query(Midnight).limit(3).all()
    res4 = db.query(Diffusion).limit(3).all()
    return res1, res2, res3, res4


@app.get("/Foundation")
def foundation(db: Session = Depends(get_db)):
    return db.query(Foundation).all()


@app.get("/Foundation/{title}")
def foundationTile(title: str, db: Session = Depends(get_db)):
    tile = db.query(Foundation).filter(Foundation.title == title).first()

    if not tile:
        raise HTTPException(status_code=404, detail="Product not found")
    return tile


@app.get("/Persephone")
def persephone(db: Session = Depends(get_db)):
    return db.query(Persephone).all()


@app.get("/Persephone/{title}")
def persephoneTile(title: str, db: Session = Depends(get_db)):
    tile = db.query(Persephone).filter(Persephone.title == title).first()

    if not tile:
        raise HTTPException(status_code=404, detail="Product not found")
    return tile


@app.get("/Midnight")
def midnight(db: Session = Depends(get_db)):
    return db.query(Midnight).all()


@app.get("/Midnight/{title}")
def midnightTile(title: str, db: Session = Depends(get_db)):
    tile = db.query(Midnight).filter(Midnight.title == title).first()

    if not tile:
        raise HTTPException(status_code=404, detail="Product not found")
    return tile


@app.get("/Diffusion")
def diffusion(db: Session = Depends(get_db)):
    return db.query(Diffusion).all()


@app.get("/Diffusion/{title}")
def diffusionTile(title: str, db: Session = Depends(get_db)):
    tile = db.query(Diffusion).filter(Diffusion.title == title).first()

    if not tile:
        raise HTTPException(status_code=404, detail="Product not found")
    return tile
