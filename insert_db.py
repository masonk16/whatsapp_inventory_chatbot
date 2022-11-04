from models import  Product, session

umbrella = Product(name="Collapsible Umbrella", amount=2)
smartwatch = Product(name="Hybrid Smartwatch", amount=1)
kicks = Product(name="Converse AllStars", amount=5)

session.add_all([umbrella, smartwatch])
session.commit()