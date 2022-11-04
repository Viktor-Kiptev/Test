from PIL import Image, ImageFilter

img =Image.open('./Pokedex/pikachu.jpg')
# filter_img = img.filter(ImageFilter.BLUR)
filter_img = img.convert('L')
filter_img.save('grey.png', 'png')
