from telnetlib import Telnet

class JamesHelper:
    def __init__(self, app):
        self.app = app

    def ensure_user_exist(self, username, password):
        pass

    class Session:
        def __init__(self, host, port, username, password):
            # Устанавливаем соединение
            self.telnet = Telnet(host, port, 5)
            # Ожидаем указанную строку в течении 5 секунд
            self.telnet.read_until("Login id", 5)
            # Вводим имя пользователя
            self.telnet.write(username + "\n")
            # Ожидаем указанную строку в течении 5 секунд
            self.telnet.read_until("Password", 5)
            # Вводим имя пароль
            self.telnet.write(password + "\n")
            # Ожидаем указанную строку в течении 5 секунд
            self.telnet.read_until("Welcome root. HELP for a list of commands", 5)

        def is_users_registred(self, username):
            pass

        def create_user(self, username, password):
            pass

        def reset_password(self, username, password):
            pass

