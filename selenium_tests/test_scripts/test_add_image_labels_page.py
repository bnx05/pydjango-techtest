import pytest

from page_objects.admin_dashboard_page import AdminDashboardPage


class TestAddImageLabelsPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser, login_to_django_admin):
        admin_dashboard = AdminDashboardPage(browser)

        self.image_labels_page = admin_dashboard.go_to_image_labels_page()
        self.add_image_label_page = self.image_labels_page.add_image_label()

    @pytest.mark.xfail(reason="image and label are required.")
    def test_add_empty_image_label(self):
        self.add_image_label_page.create_new_label(image_name='', label='')
