
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash


hash_ = generate_password_hash('foobar')
print(hash_)

print(check_password_hash(hash_, 'foobar'))
print(check_password_hash(hash_, 'barfoo'))



# Перенести в другой класс!!!
    # def authentication(self):
    #     for user in DataInDB.get_users()['users']:
    #         if user.get('user_name') == self.user_name:
    #             if user.get('user_secret') == self.user_secret:
    #                 return True
    #     raise AuthenticationError