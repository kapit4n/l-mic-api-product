from flask import jsonify, json, request
from app.main import api
from app.main import db

from flask_restx import Resource

from app.main.model.product import Product

ns = api.namespace("products", description="Products operations")

@ns.route('')
class ProductList(Resource):
    @ns.doc("list_products")
    def get(self):
        products = Product.query.all()
        return jsonify(list(map(Product.as_dict, products)))
    
    @ns.doc("create_product")
    def post(self):
        product = json.loads(request.data)
        product_cast = Product(id=product['id'], name=product['name'])
        db.session.add(product_cast)
        db.session.commit()
        return product

@ns.route('/<int:product_id>')
@ns.param("id", "Product Identifier")
class ProductView(Resource):
    @ns.doc("get_product_by_id")
    def get(self, product_id):
        product = Product.query.get(product_id)

        if product:
          return jsonify(product.as_dict())
        else:
            return "Not Found Product"
