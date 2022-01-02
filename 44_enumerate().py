#accessing items using enumerate()
cars = ["Aston","Audi","McLaren"]
for i,x in enumerate(cars):
    print(x)

#accessing items and indexes enumerate()
cars = ["Aston","Audi","McLaren"]
for y in enumerate(cars):
    print(y[0],y[1])

#printing return value of enumerate()
cars = ["Aston","Audi","McLaren"]
print(list(enumerate(cars)))

