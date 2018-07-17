from telnetlib import Telnet

class JamesHelper:
    def __init__(self, app):
        self.app = app

    def ensure_user_exist(self, username, password):
        james_config = self.app.config['james']
        # Создаем сессию для подключения к серверу
        session = JamesHelper.Session(
            james_config['host'], james_config['port'], james_config['username'], james_config['password'])
        # Если пользователь существует
        if session.is_users_registred(username):
            # Тогда сбрасываем пароль
            session.reset_password(username, password)
        else:
            # Иначе создаем нового пользователя
            session.create_user(username, password)
        # Закрывем сессию
        session.quit()

    class Session:
        def __init__(self, host, port, username, password):
            # Устанавливаем соединение
            self.telnet = Telnet(host, port, 5)
            # Ожидаем указанную строку в течении 5 секунд
            self.read_until("Login id:")
            # Вводим имя пользователя
            self.write(username + "\n")
            # Ожидаем указанную строку в течении 5 секунд
            self.read_until("Password:")
            # Вводим имя пароль
            self.write(password + "\n")
            # Ожидаем указанную строку в течении 5 секунд
            self.read_until("Welcome root. HELP for a list of commands")

        def read_until(self, text):
            # Ожидаем текст и перекодируем его в байтовый тип
            self.telnet.read_until(text.encode('ascii'), 5)

        def write(self, text):
            self.telnet.write(text.encode('ascii'))

        def is_users_registred(self, username):
            # Вводим команду на проверку существования пользователя
            self.write("verify %s\n" % username)
            # Задаем список возможных ответов при проверке попльзователя (b - преобразует строку в байты)
            res = self.telnet.expect([b"exists", b"does not exist"])
            # Если получаем значение из списка с индексом 0 тогда пользователь существует
            return res[0] == 0

        def create_user(self, username, password):
            # Вводим команду на добавление нового пользователя
            self.write("adduser %s %s\n" % (username, password))
            # Ожидаем указанную строку в течении 5 секунд
            self.read_until("User % added" % username)

        def reset_password(self, username, password):
            # Вводим команду на изменение пароля пользователя
            self.write("setpassword %s %s\n" % (username, password))
            # Ожидаем указанную строку в течении 5 секунд
            self.read_until("Password for % reset" % username)

        def quit(self):
            self.write("quit\n")

