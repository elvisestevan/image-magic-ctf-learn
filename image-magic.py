from PIL import Image

myImage = Image.open("out copy.jpg")
pixels = myImage.load()

img = Image.new("RGB", (304, 92), "white")
pixels_new = img.load()

col = 0

for i in range(img.size[0]):
    for j in range(img.size[1]):
            pixels_new[i, j] = pixels[col, 0]
            col += 1

img.save("copy.jpg")
