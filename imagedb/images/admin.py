from django.contrib import admin

from .models import Image, ImageLabel


class ImageLabelInline(admin.TabularInline):
    extra = 0
    min_num = 1
    model = ImageLabel


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    inlines = [ImageLabelInline]
    list_display = ('id', 'labels')

    def labels(self, obj):
        return list(obj.labels.all())


@admin.register(ImageLabel)
class ImageLabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'label')
