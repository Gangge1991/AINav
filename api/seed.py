from . import create_app, db
from .models import Category, Site, User
from werkzeug.security import generate_password_hash

app = create_app()

def seed():
    with app.app_context():
        # Create categories
        categories = [
            {'name': '技术工具', 'slug': 'tech-tools', 'icon': '🔧'},
            {'name': '开发工具', 'slug': 'dev-tools', 'icon': '💻', 'parent_slug': 'tech-tools'},
            {'name': '设计工具', 'slug': 'design-tools', 'icon': '🎨', 'parent_slug': 'tech-tools'},
            {'name': '生活娱乐', 'slug': 'entertainment', 'icon': '🎬'},
            {'name': '学习教育', 'slug': 'education', 'icon': '📚'},
            {'name': '商务办公', 'slug': 'business', 'icon': '💼'},
        ]

        for cat_data in categories:
            parent_slug = cat_data.pop('parent_slug', None)
            category = Category.query.filter_by(slug=cat_data['slug']).first()
            if not category:
                parent = None
                if parent_slug:
                    parent = Category.query.filter_by(slug=parent_slug).first()
                
                category = Category(**cat_data)
                if parent:
                    category.parent = parent
                db.session.add(category)
        
        db.session.commit()
        print("Categories seeded.")

        # Create sites
        sites = [
            {
                'title': 'GitHub',
                'url': 'https://github.com',
                'description': '全球最大的代码托管平台',
                'icon_url': 'https://github.com/favicon.ico',
                'category_slug': 'dev-tools'
            },
            {
                'title': 'Stack Overflow',
                'url': 'https://stackoverflow.com',
                'description': '程序员问答社区',
                'icon_url': 'https://stackoverflow.com/favicon.ico',
                'category_slug': 'dev-tools'
            },
            {
                'title': 'Figma',
                'url': 'https://figma.com',
                'description': '在线协作设计工具',
                'icon_url': 'https://figma.com/favicon.ico',
                'category_slug': 'design-tools'
            }
        ]

        for site_data in sites:
            cat_slug = site_data.pop('category_slug')
            category = Category.query.filter_by(slug=cat_slug).first()
            if category:
                site = Site.query.filter_by(url=site_data['url']).first()
                if not site:
                    site = Site(**site_data, category=category)
                    db.session.add(site)
        
        db.session.commit()
        print("Sites seeded.")

        # Create test user
        if not User.query.filter_by(email='user@example.com').first():
            user = User(
                email='user@example.com',
                name='Test User',
                password_hash=generate_password_hash('password', method='pbkdf2:sha256')
            )
            db.session.add(user)
            db.session.commit()
            print("Test user created.")

if __name__ == '__main__':
    seed()
