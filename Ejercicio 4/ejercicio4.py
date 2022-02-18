nota1 = int(input("escriba la prmera nota de su alumno:"))
nota2 = int(input("escriba la segunda nota de su alumno:"))
nota3 = int(input("escriba la tercera nota de su alumno:"))
nota4 = int(input("escriba la cuarta nota de su alumno:"))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(media)
sapo = True
while sapo == True:
    if media >= 15:
        print("Alumno con talento")
        sapo = False
    if media in range(12,15):
        print("Con capacidad")
    if media < 12:
        print("Debe reorientarse")    
        sapo = False
    if media> 20:
        print("esto es imposible ha debido haber un error introduciendo las notas")   
        sapo = False 