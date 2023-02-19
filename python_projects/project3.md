## We have a script that we use to generate QR codes. It needs two inputs the message/URL and the file name for the QR code. Please look at how to use the argparser module to set it in a way that we can run it with arguments and provide those inputs. -h or --help should show how to use the script, -u or --url should be used to provide a URL and -i or --im should be used to provide the fileimage name.

### the script is below:

```python
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
