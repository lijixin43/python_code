# AUTHOR lijixin

from math import pi

r=float(input('输入半径的长度：'))
d= 2*r
perimeter = 2*pi*r
area = pi*r**2
print("圆的直径是:",int(d))
print("圆的周长是",round(perimeter,2))
print("圆的面积是",round(area,2))
