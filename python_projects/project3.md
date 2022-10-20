##  we have a script that we use to generate QR codes. It needs two input the message/url and the file name for the qr code.

#### To execute this script, you have to install "pyqrcode" and "pypng" modules with the following commands:
```pip install pyqrcode``` or ```pip3 install pyqrcode```

```pip install pypng``` or ```pip3 install pypng```

### the script is below:

```
# import pyqrcode
import pyqrcode

# Text which is to be converted to QR code
print("Enter text to convert")
s=input(": ")
# Name of QR code png file
print("Enter image name to save")
n=input(": ")
# Adding extension as .png
d=n+".png"
# Creating QR code
url=pyqrcode.create(s)
# Saving QR code as  a png file
url.show()
url.png(d, scale =6)

```
