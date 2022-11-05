import sys, os
from PIL import Image
image_folder_input = sys.argv[1]
image_folder_output = sys.argv[2]
if not os.path.exists(image_folder_output):
    os.makedirs(image_folder_output)
processed_image = 0
for file in os.listdir(image_folder_input):
    processed_image +=1
    img = Image.open(f'{image_folder_input}{file}')
    just_name = os.path.splitext(file)[0]
    img.save(f'{image_folder_output}{just_name}.pdf', 'pdf')
print(f'All done {processed_image} processed')