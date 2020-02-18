from django.contrib import admin

from .models import Image, ImageLabel


# Using inlines enables the user to create/edit an Image object
# with multiple labels. (feature #1)
class ImageLabelInline(admin.TabularInline):
    extra = 0
    min_num = 1
    model = ImageLabel


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    inlines = [ImageLabelInline]
    # This change ensures that the image label table has the ID column
    # as well as the LABEL column, so that the user can easily see the
    # labels of each image in the table. (feature #2)
    list_display = ('id', 'labels')

    def labels(self, obj):
        return list(obj.labels.all())


@admin.register(ImageLabel)
class ImageLabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'label')
