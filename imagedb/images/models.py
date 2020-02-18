from time import time

from django.db import models


def user_directory_path(_, filename):
    return f'{round(time())}/{filename}'


class Image(models.Model):
    image = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return str(self.image).split("/")[-1]


class ImageLabel(models.Model):
    image = models.ForeignKey(Image, related_name='labels', on_delete=models.CASCADE)
    label = models.CharField(max_length=255, db_index=True)
    # Setting blank to True ensures that the field is not required
    # in the Image Label form. Setting null to True ensures that NULL
    # is allowed in the database. (bug #1)
    confidence = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.label
