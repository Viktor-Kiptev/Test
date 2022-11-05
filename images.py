from PIL import Image, ImageFilter

# img = Image.open('./Pokedex/pikachu.jpg')
# filter_img = img.filter(ImageFilter.BLUR)
# filter_img = img.convert('L')
# crooked = filter_img.rotate(180)
# resize = filter_img.resize((400, 400))
# resize.save('grey.png', 'png')
# filter_img.show()
# box = (100, 100, 400, 400)
# region = filter_img.crop(box)
# region.save('grey.png', 'png')

img2 = Image.open('./Pokedex/astro.jpg')
img2.thumbnail((400, 400))
img2.save('astro_600x600.jpg')

