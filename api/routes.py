from flask import Blueprint, jsonify, request
from .models import Category, Site, User, SiteSubmission
from .schemas import CategorySchema, SiteSchema, UserSchema, SiteSubmissionSchema
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/categories', methods=['GET'])
def get_categories():
    # Fetch root categories (parent_id is NULL)
    categories = Category.query.filter_by(parent_id=None).order_by(Category.sort_order).all()
    schema = CategorySchema(many=True)
    return jsonify({'status': 'success', 'data': schema.dump(categories)})

@main_bp.route('/sites', methods=['GET'])
def get_sites():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 20, type=int)
    category_id = request.args.get('category_id', type=int)
    keyword = request.args.get('keyword')
    
    query = Site.query.filter_by(status='active')
    
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    if keyword:
        search = f"%{keyword}%"
        query = query.filter(
            (Site.title.like(search)) | 
            (Site.description.like(search))
        )
        
    pagination = query.order_by(Site.visit_count.desc()).paginate(page=page, per_page=per_page)
    
    schema = SiteSchema(many=True)
    return jsonify({
        'status': 'success',
        'data': {
            'sites': schema.dump(pagination.items),
            'total': pagination.total,
            'page': page,
            'per_page': per_page
        }
    })

@main_bp.route('/sites/<int:id>', methods=['GET'])
def get_site(id):
    site = Site.query.get_or_404(id)
    # Increment visit count
    site.visit_count += 1
    db.session.commit()
    
    schema = SiteSchema()
    return jsonify({'status': 'success', 'data': schema.dump(site)})

# Placeholder for Auth and User routes (to be implemented with JWT)
@main_bp.route('/auth/register', methods=['POST'])
def register():
    return jsonify({'status': 'error', 'message': 'Not implemented yet'}), 501

@main_bp.route('/auth/login', methods=['POST'])
def login():
    return jsonify({'status': 'error', 'message': 'Not implemented yet'}), 501
