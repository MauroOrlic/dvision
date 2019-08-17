SOURCE_ID = 'source_id'
ALL_ID = 'all_id'
DICE_ID = 'dice_id'
NUMBERS_ID = 'numbers_id'
NUMBERS_D4_ID = 'numbers_d4_id'
NUMBERS_D6_ID = 'numbers_d6_id'
NUMBERS_D8_ID = 'numbers_d8_id'
NUMBERS_D10_ID = 'numbers_d10_id'
NUMBERS_D12_ID = 'numbers_d12_id'
NUMBERS_D20_ID = 'numbers_d20_id'
NUMBERS_D100_ID = 'numbers_d100_id'
POSITION_X = 'position_x'
POSITION_Y = 'position_y'
WIDTH_X = 'width_x'
HEIGHT_Y = 'height_y'
CROP_AREA = 'crop_area'
CROPPED_IMG = 'cropped_img'
IMAGE_EXTENSIONS = ['JPG', 'JPEG', 'jpg', 'jpeg']
DIES = {'d4': 0, 'd6': 1, 'd8': 2, 'd10': 3, 'd12': 4, 'd20': 5, 'd100': 6}
GROUPS = ['train', 'test']
IMAGE_COUNTER = {die: {group: 0 for group in GROUPS} for die in DIES.keys()}
DARKNET_OBJ_NAME = 'dice'
NUMBER_MAP = \
    {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25,
    }

CLASS_ID_MAPPING = \
    [
        {SOURCE_ID: 0, ALL_ID: 0, DICE_ID: 0, NUMBERS_ID: 0},
        {SOURCE_ID: 1, ALL_ID: 1, DICE_ID: 0, NUMBERS_ID: 1},
        {SOURCE_ID: 2, ALL_ID: 2, DICE_ID: 0, NUMBERS_ID: 2},
        {SOURCE_ID: 3, ALL_ID: 3, DICE_ID: 0, NUMBERS_ID: 3},
        {SOURCE_ID: 4, ALL_ID: 4, DICE_ID: 1, NUMBERS_ID: 0},
        {SOURCE_ID: 5, ALL_ID: 5, DICE_ID: 1, NUMBERS_ID: 1},
        {SOURCE_ID: 6, ALL_ID: 6, DICE_ID: 1, NUMBERS_ID: 2},
        {SOURCE_ID: 7, ALL_ID: 7, DICE_ID: 1, NUMBERS_ID: 3},
        {SOURCE_ID: 8, ALL_ID: 8, DICE_ID: 1, NUMBERS_ID: 4},
        {SOURCE_ID: 9, ALL_ID: 9, DICE_ID: 1, NUMBERS_ID: 5},
        {SOURCE_ID: 10, ALL_ID: 10, DICE_ID: 2, NUMBERS_ID: 0},
        {SOURCE_ID: 11, ALL_ID: 11, DICE_ID: 2, NUMBERS_ID: 1},
        {SOURCE_ID: 12, ALL_ID: 12, DICE_ID: 2, NUMBERS_ID: 2},
        {SOURCE_ID: 13, ALL_ID: 13, DICE_ID: 2, NUMBERS_ID: 3},
        {SOURCE_ID: 14, ALL_ID: 14, DICE_ID: 2, NUMBERS_ID: 4},
        {SOURCE_ID: 15, ALL_ID: 15, DICE_ID: 2, NUMBERS_ID: 5},
        {SOURCE_ID: 16, ALL_ID: 16, DICE_ID: 2, NUMBERS_ID: 6},
        {SOURCE_ID: 17, ALL_ID: 17, DICE_ID: 2, NUMBERS_ID: 7},
        {SOURCE_ID: 18, ALL_ID: 18, DICE_ID: 3, NUMBERS_ID: 0},
        {SOURCE_ID: 19, ALL_ID: 19, DICE_ID: 3, NUMBERS_ID: 1},
        {SOURCE_ID: 20, ALL_ID: 20, DICE_ID: 3, NUMBERS_ID: 2},
        {SOURCE_ID: 21, ALL_ID: 21, DICE_ID: 3, NUMBERS_ID: 3},
        {SOURCE_ID: 22, ALL_ID: 22, DICE_ID: 3, NUMBERS_ID: 4},
        {SOURCE_ID: 23, ALL_ID: 23, DICE_ID: 3, NUMBERS_ID: 5},
        {SOURCE_ID: 24, ALL_ID: 24, DICE_ID: 3, NUMBERS_ID: 6},
        {SOURCE_ID: 25, ALL_ID: 25, DICE_ID: 3, NUMBERS_ID: 7},
        {SOURCE_ID: 26, ALL_ID: 26, DICE_ID: 3, NUMBERS_ID: 8},
        {SOURCE_ID: 27, ALL_ID: 27, DICE_ID: 3, NUMBERS_ID: 9},
        {SOURCE_ID: 28, ALL_ID: 28, DICE_ID: 4, NUMBERS_ID: 0},
        {SOURCE_ID: 29, ALL_ID: 29, DICE_ID: 4, NUMBERS_ID: 1},
        {SOURCE_ID: 30, ALL_ID: 30, DICE_ID: 4, NUMBERS_ID: 2},
        {SOURCE_ID: 31, ALL_ID: 31, DICE_ID: 4, NUMBERS_ID: 3},
        {SOURCE_ID: 32, ALL_ID: 32, DICE_ID: 4, NUMBERS_ID: 4},
        {SOURCE_ID: 33, ALL_ID: 33, DICE_ID: 4, NUMBERS_ID: 5},
        {SOURCE_ID: 34, ALL_ID: 34, DICE_ID: 4, NUMBERS_ID: 6},
        {SOURCE_ID: 35, ALL_ID: 35, DICE_ID: 4, NUMBERS_ID: 7},
        {SOURCE_ID: 36, ALL_ID: 36, DICE_ID: 4, NUMBERS_ID: 8},
        {SOURCE_ID: 37, ALL_ID: 37, DICE_ID: 4, NUMBERS_ID: 9},
        {SOURCE_ID: 38, ALL_ID: 38, DICE_ID: 4, NUMBERS_ID: 10},
        {SOURCE_ID: 39, ALL_ID: 39, DICE_ID: 4, NUMBERS_ID: 11},
        {SOURCE_ID: 40, ALL_ID: 40, DICE_ID: 5, NUMBERS_ID: 0},
        {SOURCE_ID: 41, ALL_ID: 41, DICE_ID: 5, NUMBERS_ID: 1},
        {SOURCE_ID: 42, ALL_ID: 42, DICE_ID: 5, NUMBERS_ID: 2},
        {SOURCE_ID: 43, ALL_ID: 43, DICE_ID: 5, NUMBERS_ID: 3},
        {SOURCE_ID: 44, ALL_ID: 44, DICE_ID: 5, NUMBERS_ID: 4},
        {SOURCE_ID: 45, ALL_ID: 45, DICE_ID: 5, NUMBERS_ID: 5},
        {SOURCE_ID: 46, ALL_ID: 46, DICE_ID: 5, NUMBERS_ID: 6},
        {SOURCE_ID: 47, ALL_ID: 47, DICE_ID: 5, NUMBERS_ID: 7},
        {SOURCE_ID: 48, ALL_ID: 48, DICE_ID: 5, NUMBERS_ID: 8},
        {SOURCE_ID: 49, ALL_ID: 49, DICE_ID: 5, NUMBERS_ID: 9},
        {SOURCE_ID: 50, ALL_ID: 50, DICE_ID: 5, NUMBERS_ID: 10},
        {SOURCE_ID: 51, ALL_ID: 51, DICE_ID: 5, NUMBERS_ID: 11},
        {SOURCE_ID: 52, ALL_ID: 52, DICE_ID: 5, NUMBERS_ID: 12},
        {SOURCE_ID: 53, ALL_ID: 53, DICE_ID: 5, NUMBERS_ID: 13},
        {SOURCE_ID: 54, ALL_ID: 54, DICE_ID: 5, NUMBERS_ID: 14},
        {SOURCE_ID: 55, ALL_ID: 55, DICE_ID: 5, NUMBERS_ID: 15},
        {SOURCE_ID: 56, ALL_ID: 56, DICE_ID: 5, NUMBERS_ID: 16},
        {SOURCE_ID: 57, ALL_ID: 57, DICE_ID: 5, NUMBERS_ID: 17},
        {SOURCE_ID: 58, ALL_ID: 58, DICE_ID: 5, NUMBERS_ID: 18},
        {SOURCE_ID: 59, ALL_ID: 59, DICE_ID: 5, NUMBERS_ID: 19},
        {SOURCE_ID: 60, ALL_ID: 60, DICE_ID: 6, NUMBERS_ID: 0},
        {SOURCE_ID: 61, ALL_ID: 61, DICE_ID: 6, NUMBERS_ID: 1},
        {SOURCE_ID: 62, ALL_ID: 62, DICE_ID: 6, NUMBERS_ID: 2},
        {SOURCE_ID: 63, ALL_ID: 63, DICE_ID: 6, NUMBERS_ID: 3},
        {SOURCE_ID: 64, ALL_ID: 64, DICE_ID: 6, NUMBERS_ID: 4},
        {SOURCE_ID: 65, ALL_ID: 65, DICE_ID: 6, NUMBERS_ID: 5},
        {SOURCE_ID: 66, ALL_ID: 66, DICE_ID: 6, NUMBERS_ID: 6},
        {SOURCE_ID: 67, ALL_ID: 67, DICE_ID: 6, NUMBERS_ID: 7},
        {SOURCE_ID: 68, ALL_ID: 68, DICE_ID: 6, NUMBERS_ID: 8},
        {SOURCE_ID: 69, ALL_ID: 69, DICE_ID: 6, NUMBERS_ID: 9},
    ]
