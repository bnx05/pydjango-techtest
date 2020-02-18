import tempfile

from django.test import TestCase

from .models import Image


class ImageModelTests(TestCase):

    def setUp(self):
        self.test_img = tempfile.NamedTemporaryFile(suffix=".png").name
        self.test_image_name = str(self.test_img).split("/")[-1]

    def test_create_new_image(self):
        img = Image(image=self.test_img)
        img.save()
        self.assertEqual(Image.objects.count(), 1)
        self.assertEqual(str(Image.objects.get(pk=1)), self.test_image_name)
