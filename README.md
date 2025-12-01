# api-blender
```
bpy.data  (ALMACÉN CENTRAL)
├── meshes  (GEOMETRÍAS)
│   ├── "Cube" ←───────────────┐
│   ├── "Sphere"               │
│   └── "PuntosMesh" ←─────────┐
│                              │
├── objects  (OBJETOS/ENTIDADES)│
│   ├── "Cube" ────────────────┘ (data = meshes["Cube"])
│   ├── "Sphere" ─────────────── (data = meshes["Sphere"])
│   └── "PuntosObject" ─────────┘ (data = meshes["PuntosMesh"])
│
├── materials  (MATERIALES)
├── textures   (TEXTURAS)
├── images     (IMÁGENES)
└── ... etc.
```

# DATA
```
## Objetos 3D (entidades en la escena)
bpy.data.objects          # Todos los objetos (meshes, cámaras, luces, etc.)
bpy.data.meshes           # Geometrías de malla
bpy.data.curves           # Curvas (Bézier, NURBS)
bpy.data.armatures        # Armaduras/Esqueletos
bpy.data.lattices         # Lattices (deformadores)
bpy.data.metaballs        # Metaballs
bpy.data.speakers         # Altavoces (audio)
bpy.data.grease_pencils   # Lápiz graso (2D/3D)
bpy.data.hair_curves      # Curvas de pelo (nuevo en Blender 3.0+)
bpy.data.pointclouds      # Nubes de puntos
bpy.data.volumes          # Volúmenes (niebla, fuego)

## Materiales y Apariencia
bpy.data.materials        # Materiales
bpy.data.textures         # Texturas
bpy.data.images           # Imágenes (texturas, fondos)
bpy.data.brushes          # Pinceles (sculpt, paint)
bpy.data.palettes         # Paletas de colores
bpy.data.paint_curves     # Curvas de pintura

## Animación y rigging
bpy.data.actions          # Acciones (animaciones)
bpy.data.shape_keys       # Shape keys (morph targets)
bpy.data.node_groups      # Grupos de nodos (Geometry Nodes, Shader)
bpy.data.particle_settings # Configuraciones de partículas
bpy.data.collections      # Colecciones (grupos de objetos)

## World y Entorno
bpy.data.worlds           # Mundos (sky, environment)
bpy.data.lights           # Luces
bpy_data.lightprobes      # Light probes (reflejos)
bpy.data.cameras          # Cámaras
bpy.data.scenes           # Escenas (puedes tener múltiples)
bpy.data.screens          # Pantallas (layouts de interfaz)

## Texto y Scripting
bpy.data.texts            # Textos/bloques de notas
bpy.data.fonts            # Fuentes tipográficas
bpy.data.movieclips       # Clips de video (tracking)
bpy.data.masks            # Máscaras (composición)
bpy.data.cache_files      # Archivos en caché (simulaciones)
bpy.data.libraries        # Bibliotecas enlazadas

## Simulaciones y física
bpy.data.cloth            # Configuraciones de tela
bpy.data.fluids           # Fluidos
bpy.data.smoke            # Humo
bpy.data.soft_body        # Cuerpo suave
```
