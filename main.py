from flask import request, jsonify
from config import app, db
from models import Menu

@app.route("/menu", methods=["GET"])
def get_all_items():
    menu_items = Menu.query.all() 
    json_menu = list(map(lambda x: x.to_json(), menu_items))
    return jsonify({"items": json_menu})

# @app.route("/menu/breakfast", methods=["GET"])
# def get_breakfast_items():
#     breakfast_items = Menu.query.filter_by(category="breakfast").all()
#     json_menu = list(map(lambda x: x.to_json(), menu_items))
#     return jsonify({"Breakfast items": json_menu})

# @app.route("/menu/lunch", methods=["GET"])
# def get_breakfast_items():
#     breakfast_items = Menu.query.filter_by(category="lunch").all()
#     json_menu = list(map(lambda x: x.to_json(), menu_items))
#     return jsonify({"Lunch items": json_menu})

# @app.route("/menu/dinner", methods=["GET"])
# def get_breakfast_items():
#     breakfast_items = Menu.query.filter_by(category="dinner").all()
#     json_menu = list(map(lambda x: x.to_json(), menu_items))
#     return jsonify({"Dinner items": json_menu})

# @app.route("/menu/dessert", methods=["GET"])
# def get_breakfast_items():
#     breakfast_items = Menu.query.filter_by(category="dessert").all()
#     json_menu = list(map(lambda x: x.to_json(), menu_items))
#     return jsonify({"Dessert items": json_menu})

# @app.route("/create_item", methods=["POST"])  # Use POST instead of GET
# def create_item():
#     data = request.get_json()  # Get JSON data from the request
#     name = data.get("name")
#     description = data.get("description")
#     price = data.get("price")
#     allergens = data.get("allergens")

#     if not name or not description or not price or not allergens:
#         return jsonify({"message": "You must include a name, description, price, and allergens"}), 400

#     # Create a new item in the Supabase-connected database
#     new_item = Item(name=name, description=description, price=price, allergens=allergens)
#     db.session.add(new_item)
#     db.session.commit()

    # return jsonify({"message": "Item created successfully", "item": new_item.to_json()}), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
