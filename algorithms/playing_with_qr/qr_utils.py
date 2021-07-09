import qrcode
import cv2


def make_qr(filename, text):
    img = qrcode.make(text)
    img.save(filename)


def read_qr(filename):
    d = cv2.QRCodeDetector()
    v, p, s = d.detectAndDecode(cv2.imread(filename))
    print(v)
    print(p)
    binary_text = ''
    for l in s:
        points = []
        for i in list(l):
            if i == 0:
                points.append('0')
            else:
                points.append('1')
        print(''.join(points))
        binary_text += ''.join(points)
    return binary_text



