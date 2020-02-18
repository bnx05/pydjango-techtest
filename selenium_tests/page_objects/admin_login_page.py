from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .admin_dashboard_page import AdminDashboardPage
from .base import Base


class AdminLoginPage(Base):
    username_field = (By.ID, 'id_username')
    password_field = (By.ID, 'id_password')
    login_form = (By.ID, 'login-form')
    login_button = (By.CSS_SELECTOR, 'input[type="submit"]')

    def login_to_admin(self, username, password):
        self.input_text(element=self.username_field, text=username)
        self.input_text(element=self.password_field, text=password)
        self.click(element=self.login_button)
        self.wait.until(EC.invisibility_of_element_located(self.login_form))
        return AdminDashboardPage(self.browser)
