from flask import Blueprint

blueprint = Blueprint(
    'login_blueprint',
    __name__,
    url_prefix='/auth',
    template_folder='templates',
    static_folder='static'
)