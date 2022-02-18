niños=int(input("cuantos niños hay:"))
preciopers = 15 
adultos = int (input("cuantos adultos hay"))
gasto = 0
if int(niños)==2:
    gasto = (preciopers * (niños + adultos))*(9/10)
    print(gasto)
if int(niños)==3:
    gasto = (preciopers * (niños + adultos))*(85/100)
    print(gasto)
if int(niños)==4:
    gasto = (preciopers * (niños + adultos))*(82/100)
    print(gasto)   
if int(niños)>4:
    gasto = (preciopers * (niños + adultos))*((82-((niños)-4))/100)
    print(gasto) 