
x1 = int(input("Введите координату первой точки по оси x: "))
y1 = int(input("Введите координату первой точки по оси y: "))
x2 = int(input("Введите координату второй точки по оси x: "))
y2 = int(input("Введите координату второй точки по оси y: "))

result = (((x2-x1)**2)+((y2-y1)**2))**0.5

print(f"{result}")
