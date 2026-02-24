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

print("Sirve")

#1. git --version > para ver la version
#2. git init > para iniciar
#3. git config --global init.defaultBranch name > asignar el nombre main
#4. git branch -m main > para cambiarnos de rama
#5. git status > ver contenido del repositorio confirmado o sin confirmar
#6. git add > preparar archivos para subir
#7. git commit -m "" > Envia o guarda comentarios 
#8. git config user.email "you@example.com" > correo
#9. git config user.name "Tu Nombre" > se pone cuando el git pide el nombre.
#!! SE QUITA EL --global SI NO ES EL COMPUTADOR DE UNO.
#10. git commit -m "" > se vuelve a poner para enviar y sale confirmación (El mismo nombre entre comillas desde el primero)
#11. https://github.com/millussion/C5-C1-TALLER-1.git > eso sale en el repository en github
#12. git push > se pone y sale un codigo a poner 
#13. git push --set-upstream origin main > verificamos y autorizamos
#14. git add registro_de_estudiantes.py > preparamos los archivos para subir
#15. git commit -m "Revisado" > mandamos la confirmación 
#16.git push > lo enviamos.