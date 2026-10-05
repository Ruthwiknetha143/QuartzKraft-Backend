from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import os, resend
from dotenv import load_dotenv

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

from schemas import ContactForm

load_dotenv()

Base.metadata.create_all(bind=engine)

resend.api_key = os.getenv("EMAIL_API")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
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

@app.post("/contact")
def contact(form: ContactForm):

    admin_email = os.getenv("ADMIN_EMAIL")

    # Email to admin
    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": [admin_email],
        "subject": f"New Contact Form Submission - {form.name}",
        "html": f"""
            <h2>New Contact Form Submission</h2>

            <p><strong>Name:</strong> {form.name}</p>
            <p><strong>Email:</strong> {form.email}</p>
            <p><strong>Phone:</strong> {form.phone}</p>
            <p><strong>Customer Type:</strong> {form.customer}</p>

            <h3>Message</h3>
            <p>{form.message}</p>
        """
    })

    # Confirmation email
    # Resend testing mode only allows the approved testing recipient
    resend.Emails.send({
        "from": "onboarding@resend.dev",
        "to": [form.email],
        "subject": "Thank you for contacting QuartzKraft",
        "html": f"""
            <h2>Hi {form.name},</h2>

            <p>Thank you for contacting QuartzKraft.</p>

            <p>
                We have received your message and our team
                will get back to you soon.
            </p>

            <hr>

            <h3>Your message</h3>
            <p>{form.message}</p>

            <br>

            <p>
                Regards,<br>
                <strong>QuartzKraft Team</strong>
            </p>
        """
    })

    return {
        "message": "Emails sent successfully"
    }