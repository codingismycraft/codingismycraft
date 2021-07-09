import qr_utils

downloaded = [
    "downloaded_1.jpg",
    "downloaded_2.jpg",
    #"blog-qr-code-2x.png",
    #"miller-qrcode.jpg",
    #"QR-Code-Standard.jpg",
    "17561-1.jpg"
]


#qr_utils.make_qr("junk.png", "asdaslkd asdas d; asdas")


for fn in downloaded:
    binary_text = qr_utils.read_qr(fn)
    #print(binary_text)
    if '1010011010' in binary_text:
        print(fn, "exists")
    else:
        print(fn, "does not exist")


