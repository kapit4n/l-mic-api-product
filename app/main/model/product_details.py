from app.main import db

class ProductDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)

    def __repr__(self):
        return f'Product: {self.description}'
    
    def serialize(self):
        return {"id": self.id, "description": self.description}
    
    def as_dict(self):
        
        return {c.description: getattr(self, c.description) for c in self.__table__.columns}
