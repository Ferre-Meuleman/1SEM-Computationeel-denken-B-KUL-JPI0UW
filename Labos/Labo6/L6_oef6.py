"""Genereer een zwarte afbeelding met witte diagonalen.  
 
Neem als breedte 900 pixels en als hoogte 600 pixels.  
 
Zorg dat de diagonalen 10 pixels breed zijn. 
 
Voor het bepalen van de diagonalen kan je gebruik maken van de 
vergelijking van een rechte r door de oorsprong:  
 
r ↔ y = m x 
 
Hierin is m = Δy / Δx de richtingscoëfficiënt. 
 
Voor de rico m kan je de verhouding breedte/hoogte gebruiken."""


from PIL import Image, ImageDraw
import numpy as np 

breedte = 900 
hoogte = 600 

blue = (0, 32, 91)
white = (255, 255, 255)
red = (252, 29, 0)  


img_array = np.zeros((hoogte, breedte, 3), dtype=np.uint8)

m = hoogte / breedte

for x in range(breedte):
    y = int(m * x)
    for dy in range(-5, 5):
        if 0 <= y + dy < hoogte:
            img_array[y + dy, x, :] = white
    y_inv = hoogte - y
    for dy in range(-5, 5):
        if 0 <= y_inv + dy < hoogte:
            img_array[y_inv + dy, x, :] = white
            
final_image = Image.fromarray(img_array)
final_image.show()
