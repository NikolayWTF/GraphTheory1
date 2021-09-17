from  tkinter import *
import math
root = Tk()

c = Canvas(root, width="2048", heigh="1024") # Создаю окно
c.pack()

n = int(input("Введите количество вершин: "))
i = 0
centerX = 700.0 # Вершины будут расположены в форме правильного n-угольника
centerY = 350.0 # Для этого задаю координаты центра окружности в которую впсиан многоугольник
radius = 7*n    # Расстояние на которое вершина удалена от центра
angel = 2 * math.pi / n # Угол между двумя смежными вершинами
X = []
Y = []
while i < n:
    x = centerX + radius * math.sin(i * angel) # Координата новой вершины по x
    y = centerY + radius * math.cos(i* angel)  # И по y
    X.append(x)
    Y.append(y)
    c.create_oval(x, y, x + 10, y + 10, fill="black") # Рисуем вершину
    c.create_text(x+15, y-2, text=f"{i+1}")           # Подписываем её
    i += 1

v = []
i = 0
while i < n:
    print("Введите список смежности для вершины " + str(i+1))
    a = list(map(int, input().split()))
    l = len(a) # Узнаём степень i-й вершины
    j = 0
    while j < l:
        if (a[j] > (i+1)): # чтобы не рисовать дважды одно ребро, проверяем не было ли оно уже нарисовано
            c.create_line(X[i] + 5, Y[i] + 5, X[a[j]-1] + 5 , Y[a[j]-1] + 5) #Создаём рёбра между i-й вершиной и смежными с ней
        j += 1
    i += 1


root.mainloop()

