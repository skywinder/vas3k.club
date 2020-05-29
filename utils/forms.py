import io

from django import forms

from utils.images import upload_image_bytes


class ImageUploadField(forms.ImageField):
    def __init__(self, resize=None, convert_to=None, quality=None, **kwargs):
        super().__init__(**kwargs)
        self.resize = resize
        self.convert_to = convert_to
        self.quality = int(quality or 90)

    def clean(self, data, initial=None):
        if not data:
            return initial

        return upload_image_bytes(
            filename=data.name,
            data=io.BytesIO(data.read()),
            resize=self.resize,
            convert_to=self.convert_to,
            quality=self.quality,
        )
