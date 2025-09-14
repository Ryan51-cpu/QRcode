import qrcode

# Open the text file with the user data
with open("user_data.txt", "r") as file:
    lines = file.read().splitlines()

# Line 1: URL
# Line 2: Output filename
url = lines[0]
filename = lines[1]

#Generate the QR code
qr = qrcode.QRCode(
    version=1,  # QR size
    box_size=10,
    border=5
)
qr.add_data(url)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill="black", back_color="white")

# Save the image using the filename from the file
img.save(filename)

print(f"QR code saved as {filename} ✅")