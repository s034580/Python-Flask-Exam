from enum import Enum
from datetime import datetime
from app import db

articles_tags = db.Table('articles_tags', db.metadata,
    db.Column('id', db.Integer, primary_key=True),
    db.Column('article_id', db.Integer, db.ForeignKey('articles.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)

class StatusType(Enum):
    IN_REVIEW = 'In review'
    PUBLISHED = 'Published'


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text, nullable=False)
    status = db.Column(db.Enum(StatusType), nullable=False,
                       default=StatusType.IN_REVIEW)
    date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))
    
    author = db.relationship('Authors')
    tags = db.relationship('Tags', secondary=articles_tags)

    def __init__(self, author_id, title, text, status=None, date=None):
        self.author_id = author_id
        self.title = title
        self.text = text
        self.status = status
        self.date = date
