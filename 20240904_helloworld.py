# -*- coding: utf-8 -*-
"""20240904 helloworld.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_VdHEH10c8a-nGPje7vEpU_VxZlKn6rO
"""

print("Hello World")

print("Hello Pyton")

print("바보")

import pylab as py

x_deg = py.arange(-180, 180+1,)
x_rad = py.deg2rad(x_deg)
y = py.sin(x_rad)

py.plot(x_deg, y)
py.xlabel('x(deg)')
py.ylabel('sin(x)')
py.grid(True)

