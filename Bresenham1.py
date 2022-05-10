import matplotlib.pyplot as plt

plt.title("Bresenham Line Drawing")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

x1 = int(input("Enter the Starting point x: "))
y1 = int(input("Enter the Starting point y: "))
x2 = int(input("Enter the End point x: "))
y2 = int(input("Enter the End point y: "))

x = x1
y = y1

dx = abs(x2 - x1)
dy = abs(y2 - y1)
print("dx : ", dx, "\ndy : ", dy)

gradient = dy / float(dx)
print("gradient : ", gradient)

if gradient < 1:
    dx, dy = dy, dx
    x, y = y, x
    x1, y1 = y1, x1
    x2, y2 = y2, x2

p = 2 * dy - dx

#initialize the plotting points
x_coordinates = [x]
y_coordinates = [y]
for k in range(dx):
    if p < 0:
        p = p + 2 * dy

    else:
        p = p + 2 * (dy - dx)
        y = y + 1 if y < y2 else y - 1
    x = x + 1 if x < x2 else x - 1


    print('x = %s, y = %s' % (x, y))
    x_coordinates.append(x)
    y_coordinates.append(y)

plt.scatter(x_coordinates, y_coordinates, color='red')
plt.plot(x_coordinates, y_coordinates)
plt.show()
