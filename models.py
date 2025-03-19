from config import db

class Menu(db.Model):
    __tablename__ = "menu"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    category = db.Column(db.String(30), unique=False, nullable=False)
    # description = db.Column(db.String(256), unique=False, nullable=False)
    # price = db.Column(db.Integer, unique=False, nullable=False)
    # allergens = db.Column(db.String(140), unique=False, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            # "description": self.description,
            # "price": self.price,
            # "allergens": self.allergens
        }