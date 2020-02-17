from django.contrib import admin
from .forms import ImageForm
from .models import Image, ImageLabel


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'labels')
    form = ImageForm

    def labels(self, obj):
        return list(obj.labels.all())

    def save_model(self, request, obj, form, change):
        label = form.cleaned_data['label_field']
        label_list = label.split(",")

        def create_img_label(obj, labels_to_create):
            for label in label_list:
                img_label = ImageLabel(image=obj, label=label)
                img_label.save()

        if not obj.id:
            obj.save()
        create_img_label(obj, label_list)


@admin.register(ImageLabel)
class ImageLabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'label')
