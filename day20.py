# %% Import data
import math
from collections import defaultdict
from re import match
from utils.io_util import read_file_raw

inputs = read_file_raw('inputs/day20_test.txt')
inputs = read_file_raw('inputs/day20.txt')
inputs = inputs.split('\n\n')
id_to_tiles = defaultdict(list)

# Process each tile ID
for input in inputs:
    input = input.split('\n')
    tile_id = int(input[0].split(' ')[1][:-1])

    id_to_tiles[tile_id] = input[1:]

# Find the dimension of tiles (NxN)
for id in id_to_tiles:
    N = len(id_to_tiles[id])
    M = len(id_to_tiles[id][0])
    assert N == M
    break
# %% Tile class
class Tile:
    def __init__(self, id, tile):
        self.id = id
        self.tile = tile
        self.N = len(tile)
    
    def print(self):
        for row in self.tile:
            print(row)

    def try_rotate(self):
        """Rotate clockwise by 90 deg"""
        tile_new = ['.'*self.N for _ in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                tile_new[j] = tile_new[j][:self.N-i-1] + self.tile[i][j] + tile_new[j][self.N-i:]
        return Tile(self.id, tile_new)

    def try_hflip(self):
        """flip horizontally"""
        tile_new = ['.'*self.N for _ in range(self.N)]
        for i in range(self.N):
            tile_new[i] = self.tile[i][::-1]
        return Tile(self.id, tile_new)

    def try_vflip(self):
        """flip vertically"""
        tile_new = ['.'*self.N for _ in range(self.N)]
        for i in range(self.N):
            tile_new[i] = self.tile[self.N-i-1]
        return Tile(self.id, tile_new)

    def try_transform(self, ort):
        tile_new = Tile(self.id, self.tile)
        if ort[0] == 'n':
            pass
        elif ort[0] == 'h':
            tile_new = tile_new.try_hflip()

        for _ in range(int(ort[1])):
            tile_new = tile_new.try_rotate()
            
        return tile_new
    
    def get_top(self):
        return self.tile[0]

    def get_bot(self):
        return self.tile[-1]

    def get_right(self):
        return ''.join([self.tile[i][-1] for i in range(self.N)])
    
    def get_left(self):
        return ''.join([self.tile[i][0] for i in range(self.N)])

    def get_edges(self):
        return (self.get_top(), self.get_right(), self.get_bot(), self.get_left())

    def get_content(self):
        img = []
        for row in self.tile[1:-1]:
            img.append(row[1:-1])
        return img

# %% Map each edge to ID and it's orientation
edges_to_id = defaultdict(list)

for id, tile in id_to_tiles.items():
    tile_obj = Tile(id, tile)
    for edge in tile_obj.get_edges():
        edges_to_id[edge].append(id)
        edges_to_id[edge[::-1]].append(id)

id_unmatched_edges_count = defaultdict(int)
for edge, id_list in edges_to_id.items():
    if len(id_list) == 1:
        id_unmatched_edges_count[id_list[0]] += 1

corners = []
for id, count in id_unmatched_edges_count.items():
    if count == 4:
        corners.append(id)        

print(f'Corners are: {corners}')

# %% Let's make the image, starting from the corner
id_start = corners[0]
tile_start = Tile(id_start, id_to_tiles[id_start])

M = int(math.sqrt(len(id_to_tiles)))
image = [[None] * M for _ in range(M)]
orients = ['n0', 'n1', 'n2', 'n3', 'h0', 'h1', 'h2', 'h3']

# Step 1, find the valid orientation for the (0, 0)
for ort in orients:
    tile = tile_start.try_transform(ort)
    left_edge = tile.get_left()
    top_edge = tile.get_top()
    if len(edges_to_id[left_edge]) == 1 and len(edges_to_id[top_edge]) == 1:
        tile_start = tile
        print(f'tile start is set at orientation {ort}')
        break

image[0][0] = tile_start

# %% Step 2, find the first row
id_chosen = set([id_start])
for j in range(1, M):
    edge_to_match = image[0][j-1].get_right()
    matched_id = sum(edges_to_id[edge_to_match]) - image[0][j-1].id
    tile = Tile(matched_id, id_to_tiles[matched_id])

    for ort in orients:
        tile_ = tile.try_transform(ort)
        if tile_.get_left() == edge_to_match and len(edges_to_id[tile_.get_top()]) == 1:
            image[0][j] = tile_
            break
    
# %% Step 3, find the first column
for i in range(1, M):
    edge_to_match = image[i-1][0].get_bot()
    matched_id = sum(edges_to_id[edge_to_match]) - image[i-1][0].id
    tile = Tile(matched_id, id_to_tiles[matched_id])

    for ort in orients:
        tile_ = tile.try_transform(ort)
        if tile_.get_top() == edge_to_match and len(edges_to_id[tile_.get_left()]) == 1:
            image[i][0] = tile_
            break    

# %% Step 4, find the rest
for i in range(1, M):
    for j in range(1, M):
        edge_to_match = image[i][j-1].get_right()
        matched_id = sum(edges_to_id[edge_to_match]) - image[i][j-1].id
        tile = Tile(matched_id, id_to_tiles[matched_id])

        for ort in orients:
            tile_ = tile.try_transform(ort)
            if tile_.get_left() == edge_to_match and tile_.get_top() == image[i-1][j].get_bot():
                image[i][j] = tile_
                break 

# %% Remove borders and build the image
K = (N-2) # the actual tile is KxK
image_content = ['.'*(K*M) for _ in range(K*M)]

for i in range(M):
    for j in range(M):
        img = image[i][j].get_content()
        for k in range(K):
            image_content[i*K+k] = image_content[i*K+k][:j*K] + img[k] + image_content[i*K+k][(j+1)*K+1:]

image_content = Tile(0, image_content)
# image_content.print()

# %% Build a monster
# monster is a 3 x 20 grid
monster = ['                  # ',
           '#    ##    ##    ###',
           ' #  #  #  #  #  #   ']
monster_map = defaultdict(list)
for i, row in enumerate(monster):
    for j, c in enumerate(row):
        if c == '#':
            monster_map[i].append(j)
        
# %% Search for sea monsters!
def find_monster(img):
    n_monsters = 0
    for i in range(K*M - 3 + 1):
        for j in range(K*M - 20 + 1):
            # determine if there is a monster
            find = True
            for i_sub in range(3):
                find *= all([img[i+i_sub][j+j_sub]=='#' for j_sub in monster_map[i_sub]])
            
            if find:
                n_monsters += 1
    return n_monsters

n_hashtags = 0
for row in image_content.tile:
    n_hashtags += sum([c=='#' for c in row])

for ort in orients:
    image_try = image_content.try_transform(ort)
    n_monsters = find_monster(image_try.tile)
    
    print(n_monsters, n_hashtags - n_monsters * 15)


# %%
