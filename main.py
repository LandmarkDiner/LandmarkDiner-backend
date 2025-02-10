from flask import request, jsonify
from config import app, db
from models import Item

@app.route("/items", methods=["GET"])
def get_items():
    items = Item.query.all()
    json_items = list(map(lambda x: x.to_json(), items))
    return jsonify({"items": json_items})

@app.route("/create_item", methods=["GET"])
def create_item():
    name = request.json.get("name")
    description = request.json.get("description")
    price = request.json.get("price")
    allergens = request.json.get("allergens")

    if not name or not description or not price or not allergens:
        return {
            jsonify({"message": "You must include, a name, description, price, and the allergens"}),
            400,
        }

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    
    app.run(debug=True)
