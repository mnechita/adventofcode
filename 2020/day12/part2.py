import numpy as np


def get_2d_rotation_m(angle, clockwise):
    if np.abs(angle) > np.pi:
        angle = angle * np.pi / 180
    if clockwise:
        return np.array([np.cos(angle), np.sin(angle), -np.sin(angle), np.cos(angle)]).reshape(2, 2)
    else:
        return np.array([np.cos(angle), -np.sin(angle), np.sin(angle), np.cos(angle)]).reshape(2, 2)


ds = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

x = np.array([0.0, 0.0]).reshape(-1, 1)
w = np.array([10.0, 1.0]).reshape(-1, 1)
for line in open('in').read().split('\n'):
    d = line[0]
    val = int(line[1:])
    if d == 'L':
        w = np.dot(get_2d_rotation_m(val, False), w)
    elif d == 'R':
        w = np.dot(get_2d_rotation_m(val, True), w)
    elif d == 'F':
        x += w * val
    else:
        w = (w.flatten() + np.array(ds[d]) * val).reshape(-1, 1)

print(np.linalg.norm(x, ord=1))
