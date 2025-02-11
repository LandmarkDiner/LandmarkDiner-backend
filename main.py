from flask import request, jsonify
from config import app, db
from models import Item

@app.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    json_items = list(for x in items: x.to_json())
    # json_items = list(map(lambda x: x.to_json(), items))
    return jsonify({"items": json_items})

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

    return jsonify({"message": "Item created successfully", "item": new_item.to_json()}), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
