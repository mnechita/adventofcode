import numpy as np


def pp(piece):
    piece_s = piece.astype(str)
    piece_s[piece_s == '1'] = '#'
    piece_s[piece_s == '0'] = '.'
    print('\n'.join([''.join(row) for row in piece_s]))


def get_all_variations(piece):
    rotated = [np.rot90(piece, k=i) for i in range(4)]
    flipped_rotated = [np.rot90(np.fliplr(piece), k=i) for i in range(4)]
    return rotated + flipped_rotated


def matches_top(piece, other):
    return all(piece[0] == other[-1])


def matches_bottom(piece, other):
    return all(piece[-1] == other[0])


def matches_left(piece, other):
    return all(piece[:, 0] == other[:, -1])


def matches_right(piece, other):
    return all(piece[:, -1] == other[:, 0])


def find_corners():
    pieces_l = list(pieces.items())
    cnts = {}
    for i in range(len(pieces_l) - 1):
        title, piece = pieces_l[i]
        for j in range(i+1, len(pieces_l)):
            o_title, o_piece = pieces_l[j]
            for variation in get_all_variations(o_piece):
                if matches_top(piece, variation):
                    # print(title, "top", o_title)
                    cnts[title] = cnts.get(title, 0) + 1
                    cnts[o_title] = cnts.get(o_title, 0) + 1
                if matches_bottom(piece, variation):
                    # print(title, "bottom", o_title)
                    cnts[title] = cnts.get(title, 0) + 1
                    cnts[o_title] = cnts.get(o_title, 0) + 1
                if matches_left(piece, variation):
                    # print(title, "left", o_title)
                    cnts[title] = cnts.get(title, 0) + 1
                    cnts[o_title] = cnts.get(o_title, 0) + 1
                if matches_right(piece, variation):
                    # print(title, "right", o_title)
                    cnts[title] = cnts.get(title, 0) + 1
                    cnts[o_title] = cnts.get(o_title, 0) + 1
    ans = 1
    for title, cnt in cnts.items():
        if cnt == 2:
            ans *= title
            print("Corner", title)
    print(ans)


pieces = {}
for piece in open('in').read().split('\n\n'):
    lines = piece.split('\n')
    title = int(lines[0].split()[1][:-1])
    arr = np.array(list(map(list, lines[1:])))
    arr = (arr == '#').astype(int)
    pieces[title] = arr

find_corners()
