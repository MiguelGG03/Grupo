pedido=int(input('Cuantos componentes vas a comprar:'))
descuento=0
if(pedido>=10000 and pedido<=20000):
    descuento=10
elif(pedido>20000 and pedido<=40000):
    descuento=15
elif(pedido>40000):
    descuento=20
commaq=str(input('El cliente es COMMAQ?(S/N):'))
if(commaq=='s' or commaq=='S'):
    descuento=descuento-2
else:
    bel=str(input('El cliente es BEL?(S/N):'))
    if(bel=='s' or bel=='S'):
        descuento=descuento+1
print('\n')
print('El nuevo descuento es del '+str(descuento)+'%')