from server.app import db

class Restaurant(db.Model):
    __tablename__ = "restaurants"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship("RestaurantPizza", back_populates="restaurant", cascade="all, delete-orphan")


class Pizza(db.Model):
    __tablename__ = "pizzas"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship("RestaurantPizza", back_populates="pizza")


class RestaurantPizza(db.Model):
    __tablename__ = "restaurant_pizzas"
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey("pizzas.id"), nullable=False)

    restaurant = db.relationship("Restaurant", back_populates="restaurant_pizzas")
    pizza = db.relationship("Pizza", back_populates="restaurant_pizzas")
