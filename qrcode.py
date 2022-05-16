import qrcode

img = qrcode.make('SipSipi')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")