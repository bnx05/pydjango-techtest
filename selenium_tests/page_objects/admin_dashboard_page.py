from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from page_objects.admin_image_labels_page import ImageLabelsPage

from .base import Base


class AdminDashboardPage(Base):
    auth_app_link = (By.CSS_SELECTOR, '.app-auth.module > table a.section')
    image_labels_link = '.model-imagelabel > th > a'

    def go_to_image_labels_page(self):
        element = self.browser.find_element_by_css_selector(
            self.image_labels_link)
        self.browser.execute_script("(arguments[0]).click();", element)
        self.wait.until(EC.invisibility_of_element_located(self.auth_app_link))
        return ImageLabelsPage(self.browser)
