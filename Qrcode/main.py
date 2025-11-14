import qrcode

url=input("Enter the URL: ").strip()

#create a file path or enter an existing path to save the image
file_path="qrcode.png"

qr=qrcode.QRCode()
qr.add_data(url)

img=qr.make_image()
img.save(file_path)

print("QR code is generated!")