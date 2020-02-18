from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .admin_add_image_label_page import AdminAddImageLabelPage
from .base import Base


class ImageLabelsPage(Base):
    add_image_label_button = (By.CLASS_NAME, 'addlink')
    image_labels_table = (By.ID, 'result_list')

    def add_image_label(self):
        self.click(self.add_image_label_button)
        self.wait.until(EC.invisibility_of_element_located(
            self.image_labels_table))
        return AdminAddImageLabelPage(self.browser)
