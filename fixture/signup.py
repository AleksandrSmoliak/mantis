import re

class SignupHelper:
    def __init__(self, app):
        self.app = app

    def new_user(self, username, email, password):
        wd = self.app.wd
        self.app.open_home_page()
        # wd.get(self.app.base_url + "/signup_page.php")
        wd.find_element_by_xpath("//div[@class='toolbar center']/a").click()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_css_selector("input[type='submit']").click()

        mail = self.app.mail.get_mail(username, password, "[MantisBT] Регистрация учетной записи")
        url = self.extract_confimation_url(mail)

        wd.get(url)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("password_confirm").send_keys(password)
        wd.find_element_by_css_selector("input[type='submit']").click()

    def extract_confimation_url(self, text):
        return re.search("http://.*$", text, re.MULTILINE).group(0)