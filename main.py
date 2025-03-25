from flask import request, jsonify
from config import app, db
from models import Menu

@app.route("/menu", methods=["GET"])
def get_menu_items():
    category = request.args.get("category", "all").lower()
    search_query = request.args.get("search", "").strip().lower()

    # Start with all items
    query = Menu.query

    # Filter by category (ignore "all" to get everything)
    if category != "all":
        query = query.filter_by(category=category)

    # Apply search filtering if search_query is provided
    if search_query:
        query = query.filter(Menu.name.ilike(f"%{search_query}%"))

    menu_items = query.all()
    json_menu = [item.to_json() for item in menu_items]

    return jsonify({"items": json_menu})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()