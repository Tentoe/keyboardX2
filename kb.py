
import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):

    col_pins = (
        board.GP10,
        board.GP12,
        board.GP13,
        board.GP14,
        board.GP18,
        board.GP19,
        board.GP20,
        board.GP21,
    )    
    row_pins = (
        board.GP2,
        board.GP3,
        board.GP4,
        board.GP5,
        board.GP6,
        board.GP7,
        board.GP8,
    )
    
    diode_orientation = DiodeOrientation.COL2ROW

