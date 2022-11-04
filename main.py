import os
import uuid
from dotenv import load_dotenv
from twilio.rest import Client
from fastapi import FastAPI, Form
from models import Product, session

load_dotenv()

#Twilio settings
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)
app = FastAPI()

# test endpoint
@app.get("/")
async def index():
    return {"message": "hello"}


def send_message(body_text):
    client.messages.create(
        from_='whatsapp:+14155238886', body=body_text, to="whatsapp:+263782875112"
    )

@app.post("/message")
async def reply(Body: str = Form()):
    message = Body.lower()
    products = session.query(Product)
    for product in products:
        if product.name.lower() in message:
            if product.amount >= 1:
                id = str(uuid())
                message = f"Your order is placed for {product.name}. This is the tracking id: {id}"
                ordered_product = products.filter(Product.name == product.name).first()
                ordered_product.amount -=1
                session.commit()
                return send_message(message)
    message = "The product you mentioned is not available at the moment."
    return send_message(message)