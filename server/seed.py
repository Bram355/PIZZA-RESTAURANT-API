from server.app import create_app, db
from server.models import Restaurant, Pizza, RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Mama Mia", address="123 Pizza Lane")
    r2 = Restaurant(name="Cheesy Bites", address="456 Crust Ave")
    p1 = Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil")
    p2 = Pizza(name="Pepperoni", ingredients="Pepperoni, Cheese")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=9.99, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=11.5, restaurant_id=r2.id, pizza_id=p2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()
