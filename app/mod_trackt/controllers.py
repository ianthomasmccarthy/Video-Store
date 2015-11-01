from app import app
from Flask import flask, Blueprint

mod_trakt = Blueprint('trakt', __name__, url_prefix='/trakt')
