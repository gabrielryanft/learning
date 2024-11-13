def terrainsize(width, height):
    terrain = width * height
    print(f'The terrain with the size if {width}x{height} is {terrain}m².')

    
w = float(input('Terrain width: '))
h = float(input('Terrain height: '))
terrainsize(w, h)