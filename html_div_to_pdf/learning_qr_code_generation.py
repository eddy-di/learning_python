import qrcode
from qrcode.main import QRCode

qr = QRCode(
    version=3, 
    box_size=35,
    border=5,
    error_correction=qrcode.ERROR_CORRECT_H
)

data = 'https://www.djangoproject.com/'

qr.add_data(data=data)

qr.make(fit=True)

image = qr.make_image(
    fill_color='#8FBC8F',
    back_color='#F8F807F0'
)

image.save('qr_code.png')
