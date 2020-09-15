from scripts.logic.core_logic import DataInDB
from werkzeug.security import check_password_hash


def is_authentication(name, password):
    """User Authentication."""
    user = DataInDB.is_authentication(name, password)
    if user:
        hash_ = user[0][1]
        return check_password_hash(hash_, password)
    return False
