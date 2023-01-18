from pyglet.gl import *
import numpy as np
from math import pow, degrees
from utils import *

window = pyglet.window.Window(resizable=True)

p = []
dp = []
axis = []
angle = []
ax = [0, 0, 1]
t = 0


def cross_prod(a, b):
    result = [a[1] * b[2] - a[2] * b[1],
            a[2] * b[0] - a[0] * b[2],
            a[0] * b[1] - a[1] * b[0]]
    return result


def calculate_bspline_segment(s, t, p_i):
    T = np.array([pow(t, 3), pow(t, 2), t, 1])
    p_i.append((np.dot(T, 1/6) @ b_i3) @ s)


def calculate_orientation(s, t, p_i, dp_i, axis_i):
    global ax
    dT = np.array([3 * pow(t, 2), 2 * t, 1])
    dp_i.append((np.dot(dT, 1/6) @ db_i3) @ s)
    axis_i.append(cross_prod(ax, p_i[0]))


def calculate_rotation(dp_i, angle_i):
    cos_angle = np.divide(np.dot(ax, dp_i[-1]), np.linalg.norm(ax) * np.linalg.norm(dp_i))
    angle_i.append(degrees(np.arccos(cos_angle)))


def define_segment(s, p, dp, axis, angle, t=0):
    global ax
    p_i = []
    dp_i = []
    axis_i = []
    angle_i = []
    while 0 <= t <= 1:
        calculate_bspline_segment(s, t, p_i)
        calculate_orientation(s, t, p_i, dp_i, axis_i)
        calculate_rotation(dp_i, angle_i)
        t += 0.05
        ax = dp_i[-1] + p_i[-1]
    p.append(p_i)
    dp.append(dp_i)
    axis.append(axis_i)

    angle.append(angle_i)


def define_movement():
    for i in range(1, len(spiral) - 2):
        curr_seg = [spiral[i - 1], spiral[i], spiral[i + 1], spiral[i + 2]]
        define_segment(curr_seg, p, dp, axis, angle)


def object(t):
    flat_p = flatten(p)
    flat_angle = flatten(angle)

    glRotatef(flat_angle[t], flat_p[t][0], flat_p[t][1], flat_p[t][2])
    glTranslatef(flat_p[t][0], flat_p[t][1], flat_p[t][2])

    glColor3f(0, 0.5, 1)
    glLineWidth(0.1)
    glBegin(GL_LINE_LOOP)

    for polygon in polygons:
        for i in polygon:
            glVertex3f(vertices[i][0], vertices[i][1], vertices[i][2])

    glEnd()


def spline():
    flat_p = flatten(p)

    glColor3f(1, 0.2, 0.5)
    glLineWidth(10)
    glBegin(GL_LINE_STRIP)

    for i, p_i in enumerate(flat_p):
        glVertex3f(p_i[0], p_i[1], p_i[2])
    glEnd()


def tangents():
    flat_p = flatten(p)
    flat_dp = flatten(dp)

    glColor3f(1, 1, 0)
    glLineWidth(0.1)
    glBegin(GL_LINES)

    for i, p_i in enumerate(flat_p):
        glVertex3f(p_i[0], p_i[1], p_i[2])
        glVertex3f(p_i[0] + flat_dp[i][0], p_i[1] + flat_dp[i][1], p_i[2] + flat_dp[i][2])
    glEnd()


@window.event
def on_draw():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50.0, 1.5, 0.1, 100)
    glMatrixMode(GL_MODELVIEW)


def update(x, y):
    global t
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glTranslatef(-15, -10, -50)
    glRotatef(45, 15, 100, 160)

    tangents()
    spline()
    object(t)

    if t < len(flatten(p)) - 1:
        t += 1


def main():
    file = open(filepath, 'r')
    read_lines(file)
    define_movement()
    pyglet.clock.schedule(update, 1 / 100)
    pyglet.app.run()


if __name__ == "__main__":
    main()
