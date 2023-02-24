# Importing Dependencies
import qrcode

# Defining The Data
data = ""

# Creating The QR Code Object

qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Adding The Data To QR
qr.add_data(data)

# Making The Image
img = qr.make_image(fill_color="black", back_color="white")

# Saving The Image & Showing It

img.save("my_code.png")
img.show()