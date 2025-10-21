# Programa por Daniela Velazquez y Cristian Tapia - 2025

#=============================================================================#
#======================== Defino el programa principal =======================#
#=============================================================================#

def programa_principal():
    import os

    def NombreArchivo():
        # Guardo el nombre del archivo en variable para reutilizarlo o cambiarlo en todas las coincidencias
        nombre_archivo = "productos.txt"
        return nombre_archivo

    def DirArchivo():
        # Ruta absoluta del archivo productos.txt en la misma carpeta que este script
        base = os.path.dirname(os.path.abspath(__file__))
        archivo = os.path.join(base, NombreArchivo())
        return archivo

    # Defino metodo para verificar si existe el archivo
    def ExisteArchivo(archivo):
        return os.path.isfile(archivo)

    # Defino metodo para pedir precio y devolverlo sin tener errores de entrada
    def PedirPrecio():
        while True:
            precio = input("\nIngrese el precio del producto: ").strip()
            import re
            precio_final = 0
            # Expresion regular para validar si la cadena es numero decimal positivo
            chars_permitidos = re.compile(r"^\d+(\.\d+)?$")
            precio_formato = precio.replace(",", ".")
            if chars_permitidos.match(precio_formato):
                precio_final = float(precio_formato)
            if (0 < precio_final < 10000):
                if precio_final.is_integer():
                    precio_final = int(precio_final)
            else:
                print("\n ⚠️  Ingrese un precio valido (numero mayor a 0$ y menor a 10000$).")
                continue
            break
        return precio_final

    # Defino metodo para pedir el nombre del producto al usuario
    def PedirNombre():
        while True:
            nombre = input("\nIngrese el nombre del producto: ").strip().capitalize()
            if not nombre.isalpha():
                print(f"\n⚠️  El nombre no debe estar vacio y debe estar formado por letras.")
                continue
            if len(nombre) < 2:
                print(f"\n⚠️  El nombre es demasiado corto.")
                continue
            if len(nombre) > 40:
                print(f"\n⚠️  El nombre es demasiado largo.")
                continue
            return nombre

    # Defino metodo para pedir la cantidad y devolverla sin errores de entrada
    def PedirCantidad():
        while True:
            cantidad = input("\nIngrese la cantidad deseada: ").strip()
            if not cantidad.isdigit():
                print("\n ⚠️  Ingrese una cantidad valida (numero entero entre 1 y 100).")
                continue
            # Despues de verificar que no hayan signos especiales transformo a entero
            cantidad = int(cantidad)
            if not (0 < cantidad < 101):
                print("\n ⚠️  Ingrese una cantidad valida (numero entero entre 1 y 100).")
                continue
            break
        return cantidad

    # Defino metodo para agregar productos al txt sin sobreescribir
    def AgregarNuevoProducto():
        archivo = DirArchivo()
        nombre = PedirNombre()
        if not ExisteProducto(nombre):
            precio = PedirPrecio()
            cantidad = PedirCantidad()
            # Decido si añadir salto de linea previo según existencia y tamaño del archivo
            prefijo = ""
            if ExisteArchivo(archivo):
                if os.path.getsize(archivo) > 0:
                    prefijo = "\n"
            with open(archivo, "a") as productos:
                productos.write(f"{prefijo}{nombre},{precio},{cantidad}")
            print(f"\n ✅ Producto {nombre} agregado correctamente.")
        else:
            print("\n ⚠️  El producto ingresado ya se encuentra dentro del catalogo.\n")
            MostrarProductoConsulta(nombre)

    # Defino metodo que formatea el txt de productos y devuelve las lineas formateadas
    def ProductosListaFormato():
        archivo = DirArchivo()
        lineas_formateadas = []
        if not ExisteArchivo(archivo):
            return lineas_formateadas
        with open(archivo, "r") as productos:
            lineas = productos.readlines()
            for linea in lineas:
                linea_strip = linea.strip()
                if linea_strip == "":
                    continue
                partes = linea_strip.split(",")
                # Aseguro que tenga al menos 3 partes; si no, la ignoro
                if len(partes) >= 3:
                    # tomo solo las tres primeras partes por consistencia
                    lineas_formateadas.append([partes[0], partes[1], partes[2]])
        return lineas_formateadas

    # Defino metodo que devuelve una lista de productos
    def ListaProductosDict():
                                            
        lista_productos = []
        for nombre, precio, cantidad in ProductosListaFormato():
            lista_productos.append({
                "Producto": nombre, 
                "Precio": precio + "$", # Agregamos el símbolo $ al precio
                "Cantidad": cantidad
            })
        return lista_productos

    # Defino metodo para mostrar todos los productos disponibles
    def MostrarTablaProductos():
        archivo = DirArchivo()
        if ExisteArchivo(archivo):
            print("\n" + "=" * 54)
            print(" " * 18 + "Tabla de productos" + " " * 18)
            print("=" * 54)
            for producto in ListaProductosDict():
                for clave, valor in producto.items():
                    print(f"{clave}: {valor}")
                print("=" * 54)
        else:
            print(f"\nError: El archivo '{archivo}' no existe .")

    # Defino metodo para verificar si un producto existe dentro del txt
    def ExisteProducto(prod_consulta):
        existe = False
        for producto in ListaProductosDict():
            if producto.get("Producto") == prod_consulta:
                existe = True
                break
        return existe

    # Defino metodo para consultar por un producto en especifico y lo muestro en pantalla
    def MostrarProductoConsulta(prod_consulta):
        if not ExisteProducto(prod_consulta):
            print("\n ⚠️  El producto ingresado no se encuentra dentro del catalogo.\n")
        else:
            for producto in ListaProductosDict():
                if producto.get("Producto") == prod_consulta:
                    print("=" * 54)
                    for clave, valor in producto.items():
                        print(f"{clave}: {valor}")
                    print("=" * 54)
                    break

    # Defino metodo para agregar stock a un producto (reutiliza ProductosListaFormato)
    def AgregarStock(prod_consulta):
        if not ExisteProducto(prod_consulta):
            print("\n ⚠️  El producto ingresado no se encuentra dentro del catalogo.\n")
        else:
            cantidad = PedirCantidad()
            productos_formateados = ProductosListaFormato()
            actualizado = False
            for i in range(len(productos_formateados)):
                partes = productos_formateados[i]
                if partes[0] == prod_consulta:
                    nuevo_stock = int(partes[2]) + cantidad
                    # Valido que no supere el stock maximo (100)
                    if nuevo_stock > 100:
                        print(f"\n ⚠️  La cantidad ingresada supera el limite máximo de stock (100).\n")
                    else:
                        partes[2] = str(nuevo_stock)
                        productos_formateados[i] = partes
                        actualizado = True
                    break
            if actualizado:
                archivo = DirArchivo()
                with open(archivo, "w") as productos:
                    for line in productos_formateados:
                        productos.write(",".join(line) + "\n")
                print(f"\n ✅ Se agregaron con exito {cantidad} unidades al producto {prod_consulta}")

                    
    # Defino metodo para sacar stock de un producto
    def SacarStock(prod_consulta):
        if not ExisteProducto(prod_consulta):
            print("\n ⚠️  El producto ingresado no se encuentra dentro del catalogo.\n")
        else:
            cantidad = PedirCantidad()
            productos_formateados = ProductosListaFormato()
            actualizado = False
            for i in range(len(productos_formateados)):
                partes = productos_formateados[i]
                if partes[0] == prod_consulta:
                    nuevo_stock = int(partes[2]) - cantidad
                                                                
                    if nuevo_stock < 0:
                        print(f"\n ⚠️  La cantidad ingresada supera el limite máximo de stock disponible ({partes[2]}).\n")
                    else:
                        partes[2] = str(nuevo_stock)
                        productos_formateados[i] = partes
                        actualizado = True
                    break
            if actualizado:
                archivo = DirArchivo()
                with open(archivo, "w") as productos:
                    for line in productos_formateados:
                        productos.write(",".join(line) + "\n")
                print(f"\n ✅ Se retiraron con exito {cantidad} unidades del producto {prod_consulta}")

    def ModificarPrecio(prod_consulta):
        if not ExisteProducto(prod_consulta):
            print("\n ⚠️  El producto ingresado no se encuentra dentro del catalogo.\n")
        else:
            nuevo_precio = PedirPrecio()
            productos_formateados = ProductosListaFormato()
            actualizado = False
            precio_viejo = None
            for i in range(len(productos_formateados)):
                partes = productos_formateados[i]
                if partes[0] == prod_consulta:
                    precio_viejo = partes[1]
                    partes[1] = str(nuevo_precio)
                    productos_formateados[i] = partes
                    actualizado = True
                    break
            if actualizado:
                archivo = DirArchivo()
                with open(archivo, "w") as productos:
                    for line in productos_formateados:
                        productos.write(",".join(line) + "\n")
                print(f"\n ✅ Se modifico con exito el precio del producto {prod_consulta} (Antes: {precio_viejo}$ | Ahora: {partes[1]}$)")


    # Defino metodo para editar stock de un producto
    def EditarStock():
        menu_editar_stock = ["1. Agregar stock",
                    "2. Sacar stock",
                    "3. Modificar precios",
                    "4. Ver catalogo",
                    "5. Salir"]
        while True:
            # Mostramos las opciones del menu al usuario
            print("\n"+"="*54)
            print("Elija la opción deseada")
            print("="*54)
            for opcion in menu_editar_stock:
                print(opcion)
            print("="*54)
            # Pedimos al usuario que seleccione una de las opciones
            seleccion = input("Opción seleccionada: ").strip()
            print("="*54)
            match seleccion:
                # En cada opcion debe permitir agregar 0, como metodo de salir del proceso sin modificaciones
                case "1":
                    # Logica para agregar stock
                    ## Si existe el producto, permitir agregar stock, maximo 100 de cada producto
                    ## Si no existe dar mensaje de que no existe el producto
                    AgregarStock(PedirNombre())
                case "2":
                    # Logica para sacar stock
                    SacarStock(PedirNombre())
                case "3":
                    # Logica para cambiar el precio de un producto:
                    ## Si existe el producto, permitir cambiar el precio, menor a 5 cifras
                    ## Si no existe dar mensaje de que no existe el producto
                    ModificarPrecio(PedirNombre())
                case "4":
                    MostrarTablaProductos()
                case "5":
                    print("Saliendo al menu principal...\n")
                    break
                # Opcion inválida
                case _:
                    print("⚠️  Opción inválida. Por favor, elija una opción del 1 al 5.\n")
                    continue            
#===================================================================================#

    def CrearTXT():
        # Defino lista lineas con las lineas con productos que va a contener el txt
        lineas = ["Remera,1500,15\n",
                "Pantalon,2000,15\n",
                "Campera,2500,20"]
        # Creo archivo txt con productos
        with open(DirArchivo(), "w") as productos_w:
            productos_w.writelines(lineas)
            
    menu_principal = ["1. Crear o sobreescribir archivo con lista de productos nuevos",
                    "2. Mostrar tabla de productos disponibles",
                    "3. Consultar precio y stock de un producto",
                    "4. Agregar producto",
                    "5. Modificar inventario (Stock,Precios)",
                    "6. Salir"]
    while True:
        # Mostramos las opciones del menu al usuario
        print("\n"+"="*54)
        print("Bienvenido al catálogo de productos, elija una opción")
        print("="*54)
        for opcion in menu_principal:
            print(opcion)
        print("="*54)
        # Pedimos al usuario que seleccione una de las opciones
        seleccion = input("Opción seleccionada: ").strip()
        print("="*54)
        match seleccion:
            case "1":
                CrearTXT()
            case "2":
                MostrarTablaProductos()
            case "3":
                MostrarProductoConsulta(PedirNombre())
            case "4":
                AgregarNuevoProducto()
            case "5":
                EditarStock()
            case "6":
                print("Saliendo del programa... ¡Hasta luego!\n")
                break
            # Opcion inválida
            case _:
                print("⚠️  Opción inválida. Por favor, elija una opción del 1 al 6.\n")
                continue            
    
#=========================================================================================#
#                              Ejecuto el programa principal                              #
#=========================================================================================#
programa_principal()
#=========================================================================================#