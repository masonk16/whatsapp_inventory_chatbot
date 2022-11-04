# WhatsApp Inventory Chatbot
Uses Twilio's API to access the WhatsApp messaging product to let the clients send messages via WhatsApp and start the chatbot. This chatbot is built using a FastAPI backend. It is then communicated with Pyngrok, which is a Python wrapper for ngrok that puts the FastAPI localhost on the internet. This chatbot will fetch data from the PostgreSQL database and update inventory data in the database using the SQLAlchemy ORM.

