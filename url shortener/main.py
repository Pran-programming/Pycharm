

link2 = input("Do you want it as a QR Code? ")
link2 = link2.lower()

if link2 == "yes":
    img = qrcode.make(x)
    a = img.save("qrcode.png")
    a1 = Image.open('qrcode.png')
    a1.show()