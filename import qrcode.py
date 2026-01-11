import qrcode

pdf_link = "file:///C:/Users/Admin/OneDrive/Desktop/QR%20Code/Sharda_Birajdar_Cover-letter.pdf"

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(pdf_link)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Save QR code
img.save("cover_letter_qr.png")

print("QR Code for Cover Letter PDF created successfully!")

