import numpy as np


def pp(piece):
    piece_s = piece.astype(str)
    piece_s[piece_s == '1'] = '#'
    piece_s[piece_s == '0'] = '.'
    print('\n'.join([''.join(row) for row in piece_s]))


def to_numpy(figure):
    if isinstance(figure, str):
        figure = figure.split('\n')
    arr = np.array([list(row) for row in figure])
    arr = (arr == '#').astype(int)
    return arr


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


def get_all_matches(pieces):
    pieces_l = list(pieces.items())
    matches = {k: [] for k in pieces}
    for i in range(len(pieces_l) - 1):
        title, piece = pieces_l[i]
        for j in range(i+1, len(pieces_l)):
            o_title, o_piece = pieces_l[j]
            for variation in get_all_variations(o_piece):
                if matches_top(piece, variation) or matches_bottom(piece, variation) or \
                        matches_left(piece, variation) or matches_right(piece, variation):
                    matches[title].append(o_title)
                    matches[o_title].append(title)
                    break
    return matches


pieces = {}
for piece in open('in').read().split('\n\n'):
    lines = piece.split('\n')
    title = int(lines[0].split()[1][:-1])
    pieces[title] = to_numpy(lines[1:])

matches = get_all_matches(pieces)
corners = []
p1_ans = 1
for title, others in matches.items():
    if len(others) == 2:
        corners.append(title)
        p1_ans *= title
print('p1', p1_ans)

# Part 2
# Get the corner orientation
start_corner_title = corners[0]
start_corner_piece = pieces[start_corner_title]
orientation = 0
for o_title in matches[start_corner_title]:
    o_piece = pieces[o_title]
    for variation in get_all_variations(o_piece):
        if matches_top(start_corner_piece, variation):
            orientation |= 1 << 1
            break
        elif matches_left(start_corner_piece, variation):
            orientation |= 1
            break

rotated_start_corner_piece = start_corner_piece.copy()
# Fix orientation so it's left top corner
# matched top
if orientation & (1 << 1):
    rotated_start_corner_piece = np.flipud(rotated_start_corner_piece)
# matched left
if orientation & 1:
    rotated_start_corner_piece = np.fliplr(rotated_start_corner_piece)


nr_pieces = int(len(pieces) ** 0.5)
fixed_pieces = set()
puzzle = [[-1] * nr_pieces for _ in range(nr_pieces)]
puzzle_pieces = [[-1] * nr_pieces for _ in range(nr_pieces)]


def fit_puzzle(i, j):
    left = top = None
    left_piece = top_piece = None
    candidates = set(pieces.keys()) - fixed_pieces
    if i != 0:
        top = puzzle[i-1][j]
        top_piece = puzzle_pieces[i-1][j]
        candidates.intersection_update(matches[top])
    if j != 0:
        left = puzzle[i][j-1]
        left_piece = puzzle_pieces[i][j-1]
        candidates.intersection_update(matches[left])
    for candidate in candidates:
        candidate_piece = pieces[candidate]
        for variation in get_all_variations(candidate_piece):
            ok = True
            if left is not None:
                ok &= matches_left(variation, left_piece)
            if top is not None:
                ok &= matches_top(variation, top_piece)
            if ok:
                puzzle[i][j] = candidate
                puzzle_pieces[i][j] = variation
                fixed_pieces.add(candidate)
                if j < nr_pieces - 1:
                    ret = fit_puzzle(i, j+1)
                elif i < nr_pieces - 1:
                    ret = fit_puzzle(i+1, 0)
                else:
                    return 0
                if ret == -1:
                    puzzle[i][j] = -1
                    puzzle_pieces[i][j] = -1
                    fixed_pieces.remove(candidate)
                else:
                    return 0
    return -1


puzzle[0][0] = start_corner_title
puzzle_pieces[0][0] = rotated_start_corner_piece
fixed_pieces.add(start_corner_title)
fit_puzzle(0, 1)

monster = open('monster').read()
monster_np = to_numpy(monster)
monster_mask = monster_np == 1

trimmed_puzzle = puzzle_pieces.copy()
for row in trimmed_puzzle:
    for j in range(len(row)):
        row[j] = row[j][1:-1, 1:-1]
trimmed_puzzle = np.block(trimmed_puzzle)

cnt = 0
for variation in get_all_variations(trimmed_puzzle):
    for i in range(variation.shape[0] - monster_np.shape[0] + 1):
        for j in range(variation.shape[1] - monster_np.shape[1] + 1):
            window = variation[i:i+monster_np.shape[0], j:j+monster_np.shape[1]]
            window_mask = window == 1
            if np.all((window_mask & monster_mask) == monster_mask):
                # print('Found monster at ', i, j)
                cnt += 1

print('p2', np.sum(trimmed_puzzle == 1) - cnt * np.sum(monster_mask))
