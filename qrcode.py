import qrcode
code_f = qrcode.QRCode(box_size=40, border=6)
code_f.add_data("https://www.youtube.com/watch?v=Lmre1V5OWpk")
code_f.make(fit=True)
# now set image
qrcode_img = code_f.make_image(fill_color="red", back_color="white")
qrcode_img.save("qrcodeimg1.png")

