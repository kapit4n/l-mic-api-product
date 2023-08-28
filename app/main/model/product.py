from app.main import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f'Product: {self.name}'
    
    def serialize(self):
        return {"id": self.id, "name": self.name}
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    