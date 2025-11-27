import bpy
import bmesh

# Crear nueva malla
mesh = bpy.data.meshes.new("PuntosMesh")
obj = bpy.data.objects.new("PuntosObject", mesh)

# Crear bmesh y añadir vértices
bm = bmesh.new()

# Añadir vértices (puntos)
v1 = bm.verts.new((0, 0, 0))
v2 = bm.verts.new((1, 0, 0))
v3 = bm.verts.new((0, 1, 0))
v4 = bm.verts.new((1, 1, 0))

# Crear aristas
edge1 = bm.edges.new([v1, v2])
edge2 = bm.edges.new([v2, v4])  # Conecta con v4 en lugar de v3
edge3 = bm.edges.new([v4, v3])
edge4 = bm.edges.new([v3, v1])

# Crear cara (los vértices deben estar en orden circular)
face = bm.faces.new([v1, v2, v4, v3])

# Actualizar malla
bm.to_mesh(mesh)
bm.free()

# Añadir a escena
bpy.context.collection.objects.link(obj)