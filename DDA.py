import matplotlib.pyplot as plt

plt.title("Digital Differential Analyser")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

x1 = int(input("Enter x1 :"))
y1 = int(input("Enter y1 :"))
x2 = int(input("Enter x2 :"))
y2 = int(input("Enter y2 :"))
print("\n###############")

x = x1
y = y1

dx = abs(x2 - x1)
dy = abs(y2 - y1)
print("dx : ", dx, "\ndy : ", dy)
gradient = dy / float(dx)
print("gradient : ", gradient)

if dx > dy:
    steps = dx
else:
    steps = dy

print('x = %s, y = %s' % (x, y))
x_coordinates = [x]
y_coordinates = [y]
for k in range(steps):
    if dx > dy:
        steps = dx
        if x1 < x2:
            x += 1
            y += gradient
    else:
        steps = dy
        if y1 < y2:
            y += 1
            x += (1 / gradient)
        else:
            y -= 1
            x -= 1 / gradient
    print('x = %s, y = %s' % (x, y))
    x_coordinates.append(x)
    y_coordinates.append(y)
#plot the line
plt.scatter(x_coordinates, y_coordinates, color='red')
plt.plot(x_coordinates, y_coordinates)
plt.show()