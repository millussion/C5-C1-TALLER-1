p = int(input("¿Cuantas personas desea registar?: "))

for i in range(p):
    n = input("Ingrese su nombre: ")
    e = int(input("Ingrese su edad: "))
    while e < 0 :
        print("Error")
        e = int(input("Ingrese nuevamente su edad: "))
    
    c = input("¿Tiene conocimientos básicos en programación? (Si/No): ")
    c_convertido = c.lower()
    
    if e >= 15 and c_convertido == "si":
        print("Puede participar en el taller.")
        
    else :
        print("No cumple los requisitos.")

    
print("Proceso finalizado")