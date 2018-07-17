def test_signup_account(app):
    username = "user3"
    password = "test"
    app.james.ensure_user_exist(username, password)