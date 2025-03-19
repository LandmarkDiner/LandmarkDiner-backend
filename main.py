from flask import request, jsonify
from config import app, db
from models import Menu

@app.route("/menu", methods=["GET"])
def get_menu_items():
    category = request.args.get("category")  # Get category from query param
    search_term = request.args.get("search", "").lower()  # Get search term (optional)

    # Start with all menu items
    query = Menu.query

    # Apply category filter if specified
    if category and category.lower() != "all":
        query = query.filter(Menu.category.ilike(category))  # Case-insensitive match

    # Apply search filter if specified
    if search_term:
        query = query.filter(
            (Menu.name.ilike(f"%{search_term}%")) | 
            (Menu.description.ilike(f"%{search_term}%"))
        )

    # Fetch filtered results
    menu_items = query.all()
    json_menu = [item.to_json() for item in menu_items]

    return jsonify({"items": json_menu})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
