import qrcode


def generate_QRcode(text):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")


# test the QR - code generator
# generate_QRcode("https://www.linkedin.com/in/ghada-shwayat-5136b6162/")

url = input("enter your URL:")
generate_QRcode(url)
