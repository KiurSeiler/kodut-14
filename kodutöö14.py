import csv
import math
import random

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age


nimed = []

n = 0
with open('nimed.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        nimed.append(Person(row['Eesnimi'], row['Perekonnanimi'], row ['vanus']))
        if Person('Eesnimi').isupper and Person('Perekonnanimi').isupper:
        
            n = n + 1

            random.shuffle(nimed)

            max_num = int(input("sisesta max num: "))

            gruppide_arv = math.ceil(len(nimed) / max_num)

            gruppid = []
            for i in range (0, gruppide_arv):
                gruppid.append([])

            i = 0
            for nimi in nimed:
                gruppid[i % gruppide_arv].append(nimi)
                i = i + 1

            for grupp in gruppid:
                print("======")
                for isik in grupp:
                    print(f"{isik.first_name},{isik.last_name},{isik.age}")
        else:
            break
