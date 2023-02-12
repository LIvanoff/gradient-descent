

def fread(filename: str):
    with open("coordinates.txt") as coord_file:
        line_list = coord_file.readlines()

    line_list = list(map(lambda it: it.replace("\n", ""), line_list))
    coords_array = list(map(lambda it: it.split(), line_list))

    for coord_id in range(len(coords_array)):
        coords_array[coord_id] = list(map(float, coords_array[coord_id]))
    print(coords_array)
    return coords_array
