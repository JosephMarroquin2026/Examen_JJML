import mysql.connector
conexion = mysql.connector.connect(
    host="localhost", user="root" , password="123456789", database="restaurante_db"
)
cursor = conexion.cursor()
while (True):
    print("------- Bienvenido a el restaurante -------")
    print(" 1. Agregar plato")
    print(" 2. Eliminar plato")
    print(" 3. Mostrar el catalogo")
    print(" 4. salir")
    opc = input("Ingrese un numero para realizar la accion: "+"\n")
    if opc =="1":
        plato = input("Ingresa el nombre de la comida: ").strip()
        if plato:
            sql = ("insert into plato(comida) values (%s)")
            valores = (plato,)
            cursor.execute(sql, valores)
            conexion.commit()
            print(f"Plato ' {plato}' se a agregado al catalogo \n")
        else:
            print("no se puede agreagar un libro vacio")
    elif opc =="2":
        plato = input("Ingresa el nombre de la comida que deseas eliminar: ").strip()
        if plato:
         sql = ("delete from plato where comida = %s")
         valores = (plato,)
         cursor.execute(sql, valores)
         conexion.commit()
         if cursor.rowcount>0:
          print(f"Plato ' {plato}' se a eliminado de el catalogo \n")
        else:
         print("nombre ingresado incorrecto o inexistente")
    elif opc =="3":
        sql = ("select nombre from plato")
        print(f"Restaurante: '{plato}'")
    elif opc =="4":
        print("Saliendo de el programa....")
        cursor.close()
        conexion.close()
        break
    elif opc > "4":
        print("numero incorrecto. de el 1 al 4")

