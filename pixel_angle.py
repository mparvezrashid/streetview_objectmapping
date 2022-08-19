import math

w= 2748
h = 2198

HFOV = 76.88725
VFOV = 64.82693


x = 1843
y = 895

center_image_x = w/2
center_image_y = h/2

h_angle = ((x - w/2)/(w/2))*(HFOV/2)
v_angle = ((y - h/2)/(h/2))*(VFOV/2)

print(h_angle,v_angle)

print (((h_angle**2)+(v_angle**2))**0.5)