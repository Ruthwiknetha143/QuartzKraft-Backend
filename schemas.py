from pydantic import BaseModel,EmailStr

class ContactForm(BaseModel):
    name:str
    email:EmailStr
    phone:str
    customer:str
    message:str