from flask import Blueprint

blueprint = Blueprint(
    'auth_blueprint',
    __name__,
    url_prefix='/api',
    template_folder='templates',
    static_folder='static'
)