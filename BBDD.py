import sqlite3 

# Conexión a la base de datos SQLite
conexion = sqlite3.connect('masana.db')
cursor = conexion.cursor()

# Crear una tabla para guardar los ventas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
        id_producto INTEGER,
        fecha_venta TEXT, 
        cliente TEXT,
        medio_de_pago TEXT,
        descripcion_producto TEXT,
        cantidad_vendida REAL,
        subtotal REAL,
        vendedor TEXT,
        estatus TEXT,
    )
''')

# Crear una tabla para guardar los pedidos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pedidos (
        id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
        id_producto INTEGER,
        fecha_venta TEXT, 
        cliente TEXT,
        medio_de_pago TEXT,
        descripcion_producto TEXT,
        cantidad_vendida REAL,
        subtotal REAL,
        vendedor TEXT,
        estatus TEXT,
    )
''')

# Crear una tabla para guardar los clientes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        razon_social TEXT,
        tipo_cliente TEXT,    
        cuit LONG,
        email TEXT,
        direccion text,
        telefono TEXT,
        heladera_equipo TEXT,
        representante TEXT,
        fecha_alta TEXT,
        estatus TEXT,
    )
''')

# Crear una tabla para guardar los empleados
cursor.execute('''
    CREATE TABLE IF NOT EXISTS empleados (
        id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_completo TEXT,
        cuit LONG,
        email TEXT,
        telefono LONG,
        contacto_emergencia LONG,
        nombre_contacto_emergencia TEXT,
        direccion text,
        puesto_trabajo TEXT,
        descripcion_puesto TEXT,
        fecha_alta TEXT,
    )
''')

# Crear una tabla para guardar los productos

cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion_producto TEXT,
        categoria TEXT,
        precio_unit REAL,
        estatus TEXT,
    )
''')

# Crear una tabla para guardar los insumos
conn.execute('''
    CREATE TABLE IF NOT EXISTS insumos (
        id_insumo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_insumo TEXT,
        proveedor REAL,
        unidad_medida TEXT,
        stock REAL,
    )
''')

# Crear una tabla para guardar datos de abastecimiento
conn.execute('''
    CREATE TABLE IF NOT EXISTS abastecimiento (
        id_abastecimiento INTEGER PRIMARY KEY AUTOINCREMENT,
        id_insumo TEXT,
        cantidad adquirida REAL,
        unidad_medida TEXT,
        costo_unitario REAL,
        subtotal LONG,
        proveedor TEXT,
    )
''')

# Crear una tabla para guardar los proveedores
cursor.execute('''
    CREATE TABLE IF NOT EXISTS proveedor (
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        razon_social TEXT,
        nombre_completo TEXT,    
        cuit LONG,
        email TEXT,
        direccion text,
        telefono TEXT,
        productos_servicios TEXT,
        fecha_alta TEXT,
    )
''')

# Crear una tabla para guardar la produccion
conn.execute('''
    CREATE TABLE IF NOT EXISTS produccion (
        id_lote INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_produccion TEXT,
        id_producto TEXT,
        cantidad_producida REAL,
        id_empleado TEXT,
    )
''')

# Crear una tabla para guardar el stock
conn.execute('''
    CREATE TABLE IF NOT EXISTS stock (
        id_stock INTEGER PRIMARY KEY AUTOINCREMENT,
        id_lote TEXT,
        id_insumo TEXT,
        id_producto TEXT, 
        id_venta TEXT,
        id_abastecimiento TEXT,
        tipo_movimiento TEXT,
        cantidad REAL,
        unidad_medida TEXT,
        
    )
''')

# Crear una tabla para guardar la papelera, si se edita algo o se elimina (no terminada)
conn.execute('''
    CREATE TABLE IF NOT EXISTS papelera (
        id_papelera INTEGER PRIMARY KEY AUTOINCREMENT,
        id_lote TEXT,
        id_insumo TEXT,
        id_producto TEXT, 
        id_abastecimiento TEXT,
        tipo_movimiento TEXT,
        cantidad REAL,
        unidad_medida TEXT,
        
                id_lote INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_produccion TEXT,
        id_producto TEXT,
        cantidad_producida REAL,
        id_empleado TEXT,
        
                id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        razon_social TEXT,
        nombre_completo TEXT,    
        cuit LONG,
        email TEXT,
        direccion text,
        telefono TEXT,
        productos_servicios TEXT,
        fecha_alta TEXT,
        
        
                id_abastecimiento INTEGER PRIMARY KEY AUTOINCREMENT,
        id_insumo TEXT,
        cantidad adquirida REAL,
        unidad_medida TEXT,
        costo_unitario REAL,
        subtotal LONG,
        proveedor TEXT,
        
                id_insumo INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_insumo TEXT,
        proveedor REAL,
        unidad_medida TEXT,
        stock REAL,
        
                id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion_producto TEXT,
        categoria TEXT,
        precio_unit REAL,
        estatus TEXT,
        
        
                id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_completo TEXT,
        cuit LONG,
        email TEXT,
        telefono LONG,
        contacto_emergencia LONG,
        nombre_contacto_emergencia TEXT,
        direccion text,
        puesto_trabajo TEXT,
        descripcion_puesto TEXT,
        fecha_alta TEXT,
        
                id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        razon_social TEXT,
        tipo_cliente TEXT,    
        cuit LONG,
        email TEXT,
        direccion text,
        telefono TEXT,
        heladera_equipo TEXT,
        representante TEXT,
        fecha_alta TEXT,
        
                id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
        id_producto INTEGER,
        fecha_venta TEXT, 
        cliente TEXT,
        medio_de_pago TEXT,
        descripcion_producto TEXT,
        cantidad_vendida REAL,
        subtotal REAL,
        vendedor TEXT,
        estatus TEXT,
        
                id_venta INTEGER PRIMARY KEY AUTOINCREMENT,
        id_producto INTEGER,
        fecha_venta TEXT, 
        cliente TEXT,
        medio_de_pago TEXT,
        descripcion_producto TEXT,
        cantidad_vendida REAL,
        subtotal REAL,
        vendedor TEXT,
        estatus TEXT,
    )
''')

conexion.commit() 

