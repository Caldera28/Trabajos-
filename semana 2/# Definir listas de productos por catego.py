# Definir listas de productos por categoría
articulos_enlatados = ["Atún", "Sardinas", "Maíz"]
productos_limpieza = ["Detergente", "Jabón", "Desinfectante"]
carnes = ["Pollo", "Res", "Pescado"]
granos = ["Arroz", "Frijoles", "Lentejas"]

# Función para mostrar todos los productos
def mostrar_productos():
    print("Articulos enlatados:")
    for i, producto in enumerate(articulos_enlatados, start=1):
        print(f"  Producto {i}: {producto}")
    print()
    
    print("Productos de limpieza:")
    for i, producto in enumerate(productos_limpieza, start=1):
        print(f"  Producto {i}: {producto}")
    print()
    
    print("Carnes:")
    for i, producto in enumerate(carnes, start=1):
        print(f"  Producto {i}: {producto}")
    print()
    
    print("Granos:")
    for i, producto in enumerate(granos, start=1):
        print(f"  Producto {i}: {producto}")
    print()

# Función para agregar un producto
def agregar_producto(categoria, producto):
    lista_categoria = globals()[categoria]  # Obtiene la lista de la categoría por su nombre
    if producto in lista_categoria:
        print("El producto ya existe.")
    else:
        lista_categoria.append(producto)
        print(f"Se agregó {producto} a {categoria}.")
        mostrar_productos()

# Función para eliminar un producto
def eliminar_producto(categoria, producto):
    lista_categoria = globals()[categoria]
    if producto in lista_categoria:
        lista_categoria.remove(producto)
        print(f"Se eliminó {producto} de {categoria}.")
        mostrar_productos()
    else:
        print("El producto no existe en esa categoría.")

# Función para actualizar un producto
def actualizar_producto(categoria, producto_viejo, producto_nuevo):
    lista_categoria = globals()[categoria]
    if producto_viejo in lista_categoria:
        index = lista_categoria.index(producto_viejo)
        lista_categoria[index] = producto_nuevo
        print(f"Se actualizó {producto_viejo} a {producto_nuevo} en {categoria}.")
        mostrar_productos()
    else:
        print("El producto no existe en esa categoría.")

# Mostrar productos antes de cualquier acción
print("Productos antes de cualquier acción:")
mostrar_productos()

# Ejemplos de acciones
agregar_producto("articulos_enlatados", "Champiñones")
eliminar_producto("carnes", "Pescado")
actualizar_producto("granos", "Arroz", "Quinoa")
