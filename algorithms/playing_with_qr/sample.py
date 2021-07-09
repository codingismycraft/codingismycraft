import qrcode
img = qrcode.make('This is a test')
#img = qrcode.make('junk')
type(img)  # qrcode.image.pil.PilImage

filename = "george.png"
img.save(filename)
import cv2

d = cv2.QRCodeDetector()
v, p, s = d.detectAndDecode(cv2.imread(filename))

print(v)
print(p)

total = 0
for l in s:

    points = []
    for i in list(l):
        if i == 0:
            points.append('0')
        else:
            points.append('1')
    print(''.join(points))


