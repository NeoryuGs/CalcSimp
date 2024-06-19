# Función para calcular el área utilizando el método de Simpson
def calcular_area_simpson(delta, medidas):
    suma = 0  # Primer término
    for i in range(0, len(medidas)):
        if i % 2 == 0:
            suma += 4 * medidas[i]
        else:
            suma += 2 * medidas[i]
    
    return  (delta/3) * suma

# Solicitar al usuario los datos necesarios
delta = float(input("Ingrese la distancia de intervalos(en metros): "))  # Delta para el calculo
num_intervalos = int(input("Ingrese el número de intervalos (debe ser par): "))
while num_intervalos % 2 != 0:
    num_intervalos = int(input("El número de intervalos debe ser par. Ingréselo nuevamente: "))
medidas = []
for i in range(num_intervalos-1):  
    medida = float(input(f"Medida {i + 1}: "))
    medidas.append(medida)

# Calcular el área utilizando el método de Simpson
area = calcular_area_simpson(medidas, delta)
# Mostrar el resultado
print(f'El area aproximada es : {area} metros cuadrados')