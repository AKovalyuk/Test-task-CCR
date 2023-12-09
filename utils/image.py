from io import BytesIO

from PIL import Image
from django.core.files.base import ContentFile


def rescale(image_field, new_max_side: int):
    image = Image.open(image_field)
    w, h = image.size
    max_side = max(w, h)
    scale_factor = new_max_side / max_side
    new_w = int(w * scale_factor)
    new_h = int(h * scale_factor)
    new_image = image.resize((new_w, new_h))
    buffer = BytesIO()
    try:
        new_image.save(buffer, format='PNG')
        return ContentFile(buffer.getvalue())
    finally:
        buffer.close()
