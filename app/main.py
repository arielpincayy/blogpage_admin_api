from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:terrioco@localhost:3306/blogpagedb'

db = SQLAlchemy(app)

from routes.user import user_routes 
from routes.extrainformation import extra_info_routes
from routes.blogs import blog_routes
from routes.categories import category_routes
from routes.contents import content_routes
from routes.joins import join_routes

app.register_blueprint(user_routes, url_prefix='')
app.register_blueprint(extra_info_routes, url_prefix='')
app.register_blueprint(blog_routes, url_prefix='')
app.register_blueprint(category_routes, url_prefix='')
app.register_blueprint(content_routes, url_prefix='')
app.register_blueprint(join_routes, url_prefix='')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5000)