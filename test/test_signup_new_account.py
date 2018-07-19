import string
import random

def random_username(perfix, maxlen):
    symbols = string.ascii_letters
    return perfix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_signup_account(app):
    username = random_username("user_", 10)
    password = "test"
    email = username + "@localhost"
    app.james.ensure_user_exist(username, password)
    app.signup.new_user(username, email, password)
    app.soap.can_login(username, password)