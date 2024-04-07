from PIL import Image
import qrcode
import qrcode.main

#create qrcode object
qr = qrcode.main.QRCode(version=1, box_size=10, border=5)

# define the data to be encoded in qr code
data = 'https://github.com/Reviro-Spring-TechStart2024-T1/backend'

# add data to qr object
qr.add_data(data=data)

# make the qr code
qr.make(fit=True)

# create an image from the qrcode
img = qr.make_image(fill_color='black', back_color='white')

# open logo or image file
logo = Image.open('/home/eddy-di/Desktop/learning_python/github-mark/github-mark-white.png')

# resize the logo or image if needed
logo = logo.resize((80,80))

# Position the logo or image in the center of the QR code
img_w, img_h = img.size
logo_w, logo_h = logo.size
pos = (((img_w - logo_w) // 2), ((img_h - logo_h) // 2))

# Paste the logo or image onto the QR code
img.paste(logo, pos)

# Save the QR code image with logo or image
img.save('qr_code_with_logo.png')
