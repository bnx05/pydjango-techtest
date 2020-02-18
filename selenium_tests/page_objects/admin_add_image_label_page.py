from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base import Base


class AdminAddImageLabelPage(Base):
    image_label_form = (By.ID, 'imagelabel_form')
    image_dropdown = (By.ID, 'id_image')
    label_field = (By.ID, 'id_label')
    confidence_field = (By.ID, 'id_confidence')
    save_button = (By.CSS_SELECTOR, '.submit-row > input[name="_save"]')

    def create_new_label(self, image_name, label, confidence=''):
        image_locator = '//select[@id="id_image"]//option[contains(text(), "{}")]'.format(
            image_name)
        self.browser.find_element_by_xpath(image_locator).click()
        self.input_text(element=self.label_field, text=label)
        self.input_text(element=self.confidence_field, text=confidence)
        self.click(self.save_button)
        self.wait.until(EC.invisibility_of_element_located(
            self.image_label_form))
