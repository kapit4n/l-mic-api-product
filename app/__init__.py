from .main import create_app, db
from werkzeug.middleware.proxy_fix import ProxyFix

app = create_app('dev')
app.app_context().push()

app.wsgi_app = ProxyFix(app.wsgi_app)

@app.route("/create-tables")
def create_tables():
    db.create_all()
    return "Tables created"

@app.route("/")
def home():
    return "Hello, Flask!"

from app.main.resources.products import *
from app.main.resources.product_details import *
