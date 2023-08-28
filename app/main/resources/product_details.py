from flask import jsonify, json, request
from app.main import api
from app.main import db

from flask_restx import Resource

from app.main.model.product_details import ProductDetails

ns = api.namespace("product_details", description="Product Details operations")

@ns.route('')
class ProductDetailsList(Resource):
    def get(self):
        product_details = ProductDetails.query.all()
        return jsonify(list(map(ProductDetails.as_dict, product_details)))
    
    def post(self):
        product_detail = json.loads(request.data)
        product_cast = ProductDetails(id=product_detail['id'], description=product_detail['description'])
        db.session.add(product_cast)
        db.session.commit()
        return product_detail

@ns.route('/<int:product_details_id>')
class ProductDetailsView(Resource):
    def get(self, product_details_id):
        product_detail = ProductDetails.query.get(product_details_id)

        if product_detail:
          return jsonify(product_detail.as_dict())
        else:
            return "Not Found Product"
