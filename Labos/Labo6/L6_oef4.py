from PIL import Image 
import numpy as np 
 
breedte = 900 
hoogte = 600 


blue = [0, 32, 91]
white = [255, 255, 255]
red = [252, 29, 0]  
black = [0, 0, 0]

oor_ver = int(input("Geef pixel voor verticale oorsprong: "))
oor_hor = int(input("Geef pixel voor horizontale oorsprong: ")) 

start_oor_ver = round(oor_ver - 12.5)
end_oor_ver = round(oor_ver + 12.5)

start_oor_hor = round(oor_hor - 12.5)
end_oor_hor = round(oor_hor + 12.5)

img = np.zeros((hoogte, breedte, 3), dtype=np.uint8)

img[:, :, :] = black

img[start_oor_hor:end_oor_hor, :, :] = red
img[:, start_oor_ver:end_oor_ver, :] = blue

Image.fromarray(img).show()