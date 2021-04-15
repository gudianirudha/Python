from PIL import Image
import matplotlib.pyplot as plt

# Opening the respective images 
img = Image.open("file.jpg")
img = Image.open("file1.jpg")

# Converting the images into the same size so that it will be easier to concatenate 
img_size = img.resize((250, 90))
img1_size = img1.resize((250, 90))


# Creating a new blank rgb image to paste the above imgs
final = Image.new("RGB", (1000, 180), "white")


#Paste the above images
final.paste(img_size, (0, 0))
final.paste(img1_size, (250, 0))


final.paste(img_size, (0, 0))
final.paste(img1_size, (250, 0))


final.paste(img_size, (0, 0))
final.paste(img1_size, (90, 0))
