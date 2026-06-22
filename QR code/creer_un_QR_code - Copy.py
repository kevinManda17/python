import qrcode
from qrcode.constants import ERROR_CORRECT_L
qr = qrcode.QRCode(
    version = 3 ,
    error_correction = ERROR_CORRECT_L,
    box_size = 512,
    border = 5 ,
)

qr.add_data('localhost:8000')
qr.make(fit=True)

img = qr.make_image( fill_color ="rouge" , back_color = 'white')
img.save("abi.png")