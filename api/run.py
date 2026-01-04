from . import create_app, db
from .models import User, Category, Site

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Category': Category, 'Site': Site}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
