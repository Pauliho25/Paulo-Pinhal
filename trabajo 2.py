horas = int(input("Ingrese la cantidad de horas trabajadas: "))
tarifa = float(input("Ingrese su tarifa por hora: "))

if horas < 160:
    extra = 0
    pago = horas * tarifa
    print("Este es su pago: $" + str(pago))
else:
    extra = horas - 160
    pago_extra = tarifa * (extra + 160)  # Se paga extra a 1.5 veces la tarifa normal
    print("Este es su pago: $" + str(pago_extra))