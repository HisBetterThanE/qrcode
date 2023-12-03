import qrcode

data = 'Andrey'
qr = qrcode.QRCode(
    version=5,
    box_size=20,
    border=10
)
qr.add_data(data)
img = qr.make_image(fill_color='chocolate', back_color='moccasin')
img.save('test.png')