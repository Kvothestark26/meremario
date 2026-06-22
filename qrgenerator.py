# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 19:57:01 2026

@author: Darío
"""

import qrcode
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, box_size=20)

qr.add_data("https://kvothestark26.github.io/meremario/")
qr.make()

print("Tamaño del QR:", len(qr.get_matrix()), "x", len(qr.get_matrix()))

matrix = qr.get_matrix()

negros = 0
blancos = 0

for fila in matrix:
    for modulo in fila:
        if modulo:
            negros += 1
        else:
            blancos += 1

print("Negros:", negros)
print("Blancos:", blancos)
print("Total:", negros + blancos)


img = qr.make_image()
img.save("qr.png")
