from io import BytesIO
import sys
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

def crop_avatar(self):
    # Opening the uploaded image
    im = Image.open(self.avatar)

    if im.mode == "JPEG":
        pass
    elif im.mode in ["RGBA", "P"]:
        im = im.convert("RGB")

    # Calculate dimensions for the square crop
    short_edge = min(im.size)
    left = (im.width - short_edge) // 2
    upper = (im.height - short_edge) // 2
    right = left + short_edge
    lower = upper + short_edge

    # Crop the image to a square
    im = im.crop((left, upper, right, lower))

    # Resize the cropped image to 300x300 pixels
    desired_size = 300
    im = im.resize((desired_size, desired_size), Image.ANTIALIAS)

    # Save the modified image to a BytesIO buffer
    output = BytesIO()
    im.save(output, format='JPEG', subsampling=0, quality=95)
    output.seek(0)

    # Create an InMemoryUploadedFile instance with the modified image data
    new_avatar = InMemoryUploadedFile(output, 'ImageField',
                                      "%s.jpg" % self.avatar.name.split('.')[0], 'image/jpeg',
                                      sys.getsizeof(output), None)

    # Update the avatar field with the new image
    self.avatar = new_avatar
