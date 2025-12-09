from PIL import Image, ImageDraw
import numpy as np 

breedte = 900 
hoogte = 600 

blue = (0, 32, 91)
white = (255, 255, 255)
red = (252, 29, 0)  
black = (0, 0, 0)

print("Image dimensions: 900x600")
oor_hor = int(input("Geef pixel voor horizontale oorsprong (x): ")) 
oor_ver = int(input("Geef pixel voor verticale oorsprong (y): "))
straal = int(input("Geef straal van de cirkel in pixels: "))

start_oor_ver = int(oor_ver - 12.5)
end_oor_ver = int(oor_ver + 12.5)

start_oor_hor = int(oor_hor - 12.5)
end_oor_hor = int(oor_hor + 12.5)

img_array = np.zeros((hoogte, breedte, 3), dtype=np.uint8)

img_array[start_oor_ver:end_oor_ver, :, :] = red

img_array[:, start_oor_hor:end_oor_hor, :] = blue

final_image = Image.fromarray(img_array)

draw = ImageDraw.Draw(final_image)

draw.circle(xy=(oor_hor, oor_ver), radius=straal, fill=white)

final_image.show()