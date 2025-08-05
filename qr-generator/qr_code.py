# Import library qrcode
import qrcode as qr

# Class QrCode
class QrCode:
    def __init__(self, url):
        self.url = url;
    
    # Check valid URL
    def check_url(self, url):
        # If the page don't have "www" is invalid
        while (self.url.find("www") == -1):
            print(f"The url {self.url} is invalid, please, insert a valid url: ")
            self.url = input()

# URL request to the user
url = input("Insert the url to transform to QR: ")

# Object creation
code = QrCode(url);
code.check_url(url);

# QR creation
img = qr.make(code.url)

# Save image
name = input("What name do you want to save the QR code? ")
img.save("QR_" + name + ".png")