from PIL import Image, ImageEnhance, ImageFilter
import os

# img1.save("dog1.png")
# img1.save("dog1.pdf")
# img1.show()
# MAX_SIZE = (250,250)
# img1.thumbnail(MAX_SIZE)
# img1.save('dog1small.jpg')

# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img1 = Image.open(item)
#         filename,extention = os.path.splitext(item)
#         img1.save(f'{filename}.png')

# img1 = Image.open("dog1.jpg")
# enhancer = ImageEnhance.Sharpness(img1)
# # enhancer.enhance(5).save("dogledited.jpg")


# Colour image
# img1 = Image.open("dog1.jpg")
# enhancer = ImageEnhance.Color(img1)
# enhancer.enhance(5).save("dogledited1.jpg")

# brightness clss

# img1 = Image.open("dog1.jpg")
# enhancer = ImageEnhance.Brightness(img1)
# enhancer.enhance(1.5).save("dogledited2.jpg")

img1 = Image.open("dog1.jpg")
img1.filter(ImageFilter.GaussianBlur(radius=4)).save("dog123.jpg")