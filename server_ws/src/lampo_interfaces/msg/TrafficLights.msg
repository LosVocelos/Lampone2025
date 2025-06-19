# How many Traffic Lights to set
uint8 num

# IDs of Traffic Lights to apply these settings (length = num)
uint8[] ids

# How the traffic lights are to be set (Always all lights together):
# 0 (0b000) - no lights
# 1 (0b001) - red
# 2 (0b010) - yellow                                1. bit - red
# 3 (0b011) - red, yellow                           2. bit - yellow
# 4 (0b100) - green                                 3. bit - green
uint8[] lights