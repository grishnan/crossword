#!/usr/bin/python3

from tkinter import *
import tkinter.font as tkFont

win = Tk()

d   = 0.07 # относительная сторона кнопки
pad = 0.03 # отступ от края окна
gap = round((1-2*pad-11*d)/10, 3) # зазор между кнопками

f = tkFont.Font(family="Monospace Regular", size=round(600*d))

L = []
for i in range(0, 11):
  L.append([])
  for j in range(0, 4):
    L[i].append(Button(win, text="B", bg='grey', font=f));
    L[i][j].place(relx=pad+i*(d+gap), rely=pad+j*(d+gap), relwidth=d, relheight=d)

win.attributes('-fullscreen', True)
win.mainloop()
