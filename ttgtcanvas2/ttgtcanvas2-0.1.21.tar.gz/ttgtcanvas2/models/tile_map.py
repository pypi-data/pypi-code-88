DEFAULT_ASSET_URL="https://totogoto.com/assets/python_project/images/"
DEFAULT_OBJECTS = [
    'token', 
    'triangle', 
    'square', 
    'strawberry',
    'banana', 
    'orange', 
    'apple', 
    'leaf',
    'dandelion',
    'carrot',
    'tulip',
    'daisy',
    'star',
    "green_home_tile",
    'mud',
    'gravel',
    'pale_grass',
    'water',
    'ice',
    'grass',
    "house"
]


DEFAULT_TILE_MAP = {tile: "{}{}.png".format(DEFAULT_ASSET_URL, tile) for tile in DEFAULT_OBJECTS }

#if wall:
#    if removable?:
#        draw_removable
#    else:
#        draw_regular
#elif goal: 
#   draw_goal