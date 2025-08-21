#Calculadora de propinas de un restaurante
total_cuenta = float(input("Ingrese el total de la cuenta a pagar "))

propina_10 = total_cuenta*0.10

propina_15 = total_cuenta*0.15

total_pagar_10 = total_cuenta + propina_10
print(f"El total de su cuenta es de ${total_cuenta}, sumandole una propina del 10%, su cuenta final queda en ${total_pagar_10}")

total_pagar_15 = total_cuenta + propina_15
print(f"El total de su cuenta es de ${total_cuenta}, sumandole una propina del 15%, su cuenta final queda en ${total_pagar_15}")