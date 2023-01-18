import numpy as np

filepath = "./palm.obj"
vertices = []
polygons = []
b_i3 = np.array([[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 0, 3, 0], [1, 4, 1, 0]])
db_i3 = np.array([[-1, 3, -3, 1], [2, -4, 2, 0], [-1, 0, 1, 0]])
spiral = np.array([[0, 0, 0], [0, 10, 5], [10, 10, 10], [10, 0, 15],[0, 0, 20],
          [0, 10, 25], [10, 10, 30], [10, 0, 35], [0, 0, 40], [0, 10, 45],
          [10, 10, 50], [10, 0, 55]])


def read_lines(file):
    for line in file:
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('g'):
            continue
        if line.startswith('v'):
            vertices.append([float(x) for x in line.split(' ')[1:]])
        elif line.startswith('f'):
            polygons.append([int(x) - 1 for x in line.split(' ')[1:]])

    xmax = max([float(vertices[i][0]) for i in range(0, len(vertices))])
    ymax = max([float(vertices[i][1]) for i in range(0, len(vertices))])
    zmax = max([float(vertices[i][2]) for i in range(0, len(vertices))])

    xmin = min([float(vertices[i][0]) for i in range(0, len(vertices))])
    ymin = min([float(vertices[i][1]) for i in range(0, len(vertices))])
    zmin = min([float(vertices[i][2]) for i in range(0, len(vertices))])

    s = [(xmax + xmin) / 2, (ymax + ymin) / 2,(zmax + zmin) / 2]
    M = max(xmax - xmin, ymax - ymin, zmax - zmin)

    for v in vertices:
        v[0] = 10 * (v[0] - s[0]) / M
        v[1] = 10 * (v[1] - s[1]) / M
        v[2] = 10 * (v[2] - s[2]) / M



def flatten(list):
    return [item for sublist in list for item in sublist]