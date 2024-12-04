from __main__ import db, app
from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from marshmallow import fields

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    lastname = db.Column(db.String(20))
    email = db.Column(db.String(30))
    writer = db.Column(db.Boolean)
    username = db.Column(db.String(10))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, name, lastname, email, writer, username):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.writer = writer
        self.username = username

    def __repr__(self):
        return '<Author %d>' % self.id


with app.app_context():
    db.create_all()


class ExtraInformation(db.Model):
    user_ID = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    type = db.Column(db.String(10), nullable=False)
    information = db.Column(db.String(50), nullable=False, primary_key=True)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, user_ID, type, information):
        self.user_ID = user_ID
        self.type = type
        self.information = information

    def __repr__(self):
        return f'<ExtraInformation {self.user_ID}>'


class Blogs(db.Model):
    blog_ID = db.Column(db.String(8), primary_key=True)
    user_ID = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_ID = db.Column(db.Integer, db.ForeignKey('categories.category_ID'), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    keywords = db.Column(db.String(100), nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, blog_ID, user_ID, category_ID, title, keywords):
        self.blog_ID = blog_ID
        self.user_ID = user_ID
        self.category_ID = category_ID
        self.title = title
        self.keywords = keywords

    def __repr__(self):
        return f'<Blog {self.blog_ID}>'


class Categories(db.Model):
    category_ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Category {self.category_ID}>'


class Contents(db.Model):
    blog_ID = db.Column(db.String(8), db.ForeignKey('blogs.blog_ID'), primary_key=True)
    user_ID = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_ID = db.Column(db.Integer, db.ForeignKey('categories.category_ID'))
    content_num = db.Column(db.Integer, nullable=False, primary_key=True)
    type = db.Column(db.String(10), nullable=False)
    content = db.Column(db.String(1000), nullable=False)

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, blog_ID, user_ID, category_ID, content_num, type, content):
        self.blog_ID = blog_ID
        self.user_ID = user_ID
        self.category_ID = category_ID
        self.content_num = content_num
        self.type = type
        self.content = content

    def __repr__(self):
        return f'<Content {self.blog_ID}-{self.user_ID}-{self.category_ID}>'


class UserSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Users
        sql_session = db.session
    
    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    lastname = fields.String(required=True)
    email = fields.String(required=True)
    writer = fields.Bool(required=True)
    username = fields.String(required=True)

class ExtraInformationSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = ExtraInformation
        sql_session = db.session
    
    user_ID = fields.Number(required=True)
    type = fields.String(required=True)
    information = fields.String(required=True)

class BlogSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Blogs
        sql_session = db.session
    
    blog_ID = fields.String(required=True)
    user_ID = fields.Number(required=True)
    category_ID = fields.Integer(required=True)
    title = fields.String(required=True)
    keywords = fields.String(required=True)

class CategorySchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Categories
        sql_session = db.session
    
    category_ID = fields.Integer(dump_only=True)
    name = fields.String(required=True)

class ContentSchema(SQLAlchemyAutoSchema):
    class Meta(SQLAlchemyAutoSchema.Meta):
        model = Contents
        sql_session = db.session
    
    blog_ID = fields.String(required=True)
    user_ID = fields.Number(required=True)
    category_ID = fields.Integer(required=True)
    content_num = fields.Integer(required=True)
    type = fields.String(required=True)
    content = fields.String(required=True)


