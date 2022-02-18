num1 = int(input("Introduce el primer numero:\n"))
num2 = int(input("Introduce el segundo numero:\n"))
suma = num1 + num2
mult = num1 * num2
orden = [num1, num2, suma, mult]
orden.sort(reverse=True)
print(orden)