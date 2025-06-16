from flask import Blueprint, request, jsonify
from server.app import db
from server.models import RestaurantPizza, Pizza

restaurant_pizza_bp = Blueprint('restaurant_pizza_bp', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def add_restaurant_pizza():
    data = request.get_json()

    try:
        new_rp = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(new_rp)
        db.session.commit()

        pizza = Pizza.query.get(data['pizza_id'])
        return jsonify({
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }), 201

    except Exception as e:
        return jsonify({"errors": ["validation errors", str(e)]}), 400
