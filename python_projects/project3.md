##  We have a script that we use to generate QR codes. It needs two input the message/url and the file name for the qr code. Please look to how to use the argparser module to set it in the way that we can run it with arguments and provide those inputs. -h or --help should show how to use the script, -u or --url should be used to provide a url and -i or --im shoulb be used to provide the fileimage name.

### the script is below:

```
import pyqrcode
import png
from pyqrcode import QRCode
# Text which is to be converted to QR code
print("Enter text to convert")
s=input(": ")
# Name of QR code png file
print("Enter image name to save")
n=input(": ")
# Adding extension as .pnf
d=n+".png"
# Creating QR code
url=pyqrcode.create(s)
# Saving QR code as  a png file
url.show()
url.png(d, scale =6)

```
