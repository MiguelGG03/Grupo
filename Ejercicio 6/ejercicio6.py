pedido=int(input('Cuantos componentes vas a comprar:'))
if(pedido>=10000 and pedido<=20000):
    print('Se le concede un descuento del 10%')
    descuento=10
elif(pedido>20000 and pedido<=40000):
    print('Se le concede un descuento del 15%')
    descuento=15
elif(pedido>40000):
    print('Se le concede un descuento del 20%')
    descuento=20
else:
    print('No hay descuentos para tal cantidad')
    descuento=0
commaq=str(input('El cliente es COMMAQ?(S/N):'))
if(commaq=='s' or commaq=='S'):
    descuento=descuento-2
    print('El nuevo descuento es del '+str(descuento)+'%')
else:
    print()
bel=str(input('El cliente es BEL?(S/N):'))
if(bel=='s' or bel=='S'):
    descuento=descuento+1
    print('El nuevo descuento es del '+str(descuento)+'%')
else:
    print()