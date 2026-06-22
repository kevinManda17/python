from rembg import remove 
from PIL import Image 

input_path="kevinManda.jpg"
output_path="kev.png"

input=Image.open(input_path)
output=remove(input)
output.save(output_path)