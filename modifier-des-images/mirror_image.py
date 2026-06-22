from PIL import Image

Image.open('kevinManda.jpg')

image= Image.open("kevinManda.jpg")
mirrorImage=image.transpose(Image.FLIP_LEFT_RIGHT)
mirrorImage.save(r"kevinManda1.jpg")

Image.open("kevinManda1.jpg")
