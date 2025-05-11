# Size of the map in "pixels", other messages, like position of robots in map corresponds with these values.
uint64 height
uint64 width

# Number of tiles in the map, how the map is segmented
uint32 tiles_y
uint32 tiles_x

# Each element refers to one tile, which directions do roads go (length = tiles_y * tiles_x)
# When converted to binary, it says which direction road goes and which does not, for example:
#   0 (0b0000) - no road
#   2 (0b0010) - east only (probably shouldn't happen)                  1. bit
#   3 (0b0011) - north, east                                     4. bit  -|-   2.bit
#  10 (0b1010) - west, east                                             3. bit
uint8[] roads