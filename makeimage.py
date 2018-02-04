import math
import random 

def rand(): 
    ret = ""
    for i in range(3):
        ret += str(random.randint(0, 256)) + " "
    ret += "\n"
    return ret

def write_to_file():
    file = open("image.ppm", "w+")
    file.write("P3\n")
    file.write("500 500\n")
    file.write("255\n")
    list = []
    for i in range(500):
        list.append([])
    for i in range(500): 
        for j in range(500): 
            list[i].append("72 61 48\n")
    for i in range(500): 
        for j in range(500):
            x = (j-250)/10.0
            y = (250-i)/10.0
            if (i == 250 or j == 250): 
                list[i][j] = "255 255 255\n"
            elif (abs(i-250) < 3 and j % 20 == 0):
                list[i][j] = "255 255 255\n"
            elif (abs(j-250) < 3 and i % 20 == 0): 
                list[i][j] = "255 255 255\n"
            elif abs((y - (x ** 2))) / ((x ** 2) ** 0.5)  < 0.2:
                list[i][j] = "255 255 0\n"
            elif abs((-y - (x ** 2))) / ((x ** 2) ** 0.5)  < 0.2:
                list[i][j] = "255 255 0\n"
            elif abs((x - (y ** 2))) / ((y ** 2) ** 0.5)  < 0.2:
                list[i][j] = "255 255 0\n"
            elif abs((-x - (y ** 2))) / ((y ** 2) ** 0.5)  < 0.2:
                list[i][j] = "255 255 0\n"
           # elif (abs(250-i) ** 2 + abs(250-j)**2) ** 0.5 < 50: 
            #    list[i][j] = rand()
            elif abs(x) - abs(y) < 1 and abs(x) - abs(y) > 0:
                list[i][j] = rand()
            file.write(list[i][j])
    file.close()
    
write_to_file()
        