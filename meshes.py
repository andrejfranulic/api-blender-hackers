import bpy
import bmesh

# Limpiar escena actual (opcional)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# ============ 1. CREAR LA MALLA BASE (DATOS) ============
mesh = bpy.data.meshes.new("TrianguloMesh")

# Crear bmesh para construir geometría
bm = bmesh.new()

# Crear 3 vértices para un triángulo
v1 = bm.verts.new((0, 0, 0))
v2 = bm.verts.new((2, 0, 0))
v3 = bm.verts.new((1, 2, 0))

# Crear cara triangular (el orden importa para la normal)
bm.faces.new([v1, v2, v3])

# Transferir geometría a la malla
bm.to_mesh(mesh)
bm.free()

# ============ 2. CREAR 3 OBJETOS QUE REFERENCIAN LA MISMA MALLA ============
# Objeto 1 (posición original)
obj1 = bpy.data.objects.new("Triangulo_1", mesh)
obj1.location = (0, 0, 0)

# Objeto 2 (desplazado en X)
obj2 = bpy.data.objects.new("Triangulo_2", mesh)
obj2.location = (3, 0, 0)

# Objeto 3 (desplazado en Y)
obj3 = bpy.data.objects.new("Triangulo_3", mesh)
obj3.location = (0, 3, 0)

# ============ 3. AÑADIR OBJETOS A LA ESCENA ============
collection = bpy.context.collection
collection.objects.link(obj1)
collection.objects.link(obj2)
collection.objects.link(obj3)

# ============ 4. VERIFICAR QUE COMPARTEN LA MISMA MALLA ============
print("=" * 50)
print("DEMOSTRACIÓN DE REFERENCIAS COMPARTIDAS")
print("=" * 50)

print(f"\n1. Malla creada: {mesh.name}")
print(f"   Vértices: {len(mesh.vertices)}")
print(f"   Caras: {len(mesh.polygons)}")

print(f"\n2. Objetos que referencian esta malla:")
for obj in [obj1, obj2, obj3]:
    print(f"   - {obj.name}: posición {obj.location}")

print(f"\n3. ¿Son la misma malla en memoria?")
print(f"   obj1.data is obj2.data: {obj1.data is obj2.data}")  # True
print(f"   obj2.data is obj3.data: {obj2.data is obj3.data}")  # True
print(f"   Todos apuntan a: {obj1.data.name}")

# ============ 5. DEMOSTRAR QUE MODIFICAR LA MALLA AFECTA A TODOS ============
print(f"\n4. Modificando la malla compartida...")

# Volver a crear bmesh desde la malla existente
bm2 = bmesh.new()
bm2.from_mesh(mesh)  # Cargar la malla actual

# Añadir un cuarto vértice en el centro
center = bm2.verts.new((1, 1, 0))

# Añadir 3 nuevas caras para crear una pirámide
bm2.faces.new([v1, v2, center])
bm2.faces.new([v2, v3, center])
bm2.faces.new([v3, v1, center])

# Actualizar la malla original
bm2.to_mesh(mesh)
bm2.free()

print(f"   ¡Malla actualizada! Ahora tiene:")
print(f"   - Vértices: {len(mesh.vertices)} (antes 3)")
print(f"   - Caras: {len(mesh.polygons)} (antes 1)")
print(f"   Los 3 objetos se actualizan automáticamente")

# ============ 6. CREAR UN OBJETO CON COPIA INDEPENDIENTE ============
print(f"\n5. Creando un objeto con COPIA INDEPENDIENTE...")

# Hacer una COPIA de la malla (no referencia)
mesh_copia = mesh.copy()
mesh_copia.name = "TrianguloMesh_Copia"

obj4 = bpy.data.objects.new("Triangulo_Independiente", mesh_copia)
obj4.location = (3, 3, 0)
obj4.scale = (0.5, 0.5, 0.5)  # Hacerlo más pequeño para diferenciar
collection.objects.link(obj4)

print(f"   Objeto independiente creado: {obj4.name}")
print(f"   ¿Usa la misma malla?: {obj4.data is mesh}")  # False
print(f"   ¿Usa una copia?: {obj4.data is mesh_copia}")  # True

# ============ 7. SELECCIONAR Y ACTIVAR OBJETOS ============
# Seleccionar todos los objetos
for obj in [obj1, obj2, obj3, obj4]:
    obj.select_set(True)

# Hacer activo el primer objeto
bpy.context.view_layer.objects.active = obj1

print(f"\n6. Resumen final:")
print(f"   - 3 objetos comparten la MISMA malla")
print(f"   - 1 objeto tiene COPIA INDEPENDIENTE")
print(f"   - Modificar {mesh.name} afecta a obj1, obj2, obj3")
print(f"   - Modificar {mesh_copia.name} solo afecta a obj4")
print("=" * 50)