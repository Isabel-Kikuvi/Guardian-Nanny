from app import app, db
from app.models import User, Nanny, NannySelection

@app.shell_context_processor
def make_shell_context():
    return {'app': app, 'db': db, 'User': User, 'Nanny': Nanny, 'NannySelection': NannySelection}