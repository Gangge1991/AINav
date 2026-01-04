from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    avatar_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    favorites = db.relationship('Favorite', backref='user', lazy='dynamic')
    submissions = db.relationship('SiteSubmission', backref='user', lazy='dynamic')

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    slug = db.Column(db.String(100), unique=True, nullable=False, index=True)
    icon = db.Column(db.String(10))
    parent_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'))
    sort_order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    children = db.relationship('Category', backref=db.backref('parent', remote_side=[id]), lazy='dynamic')
    sites = db.relationship('Site', backref='category', lazy='dynamic')

class Site(db.Model):
    __tablename__ = 'sites'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), unique=True, nullable=False)
    description = db.Column(db.Text)
    icon_url = db.Column(db.String(500))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    visit_count = db.Column(db.Integer, default=0, index=True)
    status = db.Column(db.Enum('active', 'inactive'), default='active', index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    favorites = db.relationship('Favorite', backref='site', lazy='dynamic')
    visit_logs = db.relationship('VisitLog', backref='site', lazy='dynamic')

class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    site_id = db.Column(db.Integer, db.ForeignKey('sites.id', ondelete='CASCADE'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    __table_args__ = (db.UniqueConstraint('user_id', 'site_id', name='uk_user_site'),)

class SiteSubmission(db.Model):
    __tablename__ = 'site_submissions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    status = db.Column(db.Enum('pending', 'approved', 'rejected'), default='pending', index=True)
    reject_reason = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class VisitLog(db.Model):
    __tablename__ = 'visit_logs'
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey('sites.id', ondelete='CASCADE'), nullable=False)
    ip_address = db.Column(db.String(45), index=True)
    user_agent = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)
