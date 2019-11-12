field_under=float(0)

x_max = 2
step = 0.5
i = step
while(i <= x_max):
    field_under += step * (i**2)
    i += step

print(((x_max**3)-field_under)*2)

