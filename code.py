
from adafruit_blinka.board.beagleboard.beaglebone_ai import LED_USR3
import board

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()


keyboard.modules = [
    Layers(),
]


# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

L1 = KC.MO(1) # pyright: ignore
L2 = KC.MO(2) # pyright: ignore
L3 = KC.MO(3) # pyright: ignore


# fmt: off
      # _______, XXXXXXX, _______, XXXXXXX, _______, _______, XXXXXXX, _______, XXXXXXX, _______, XXXXXXX, _______,
keyboard.keymap = [
    [ # ASDF
         KC.ESC, _______, KC.LSFT, _______, KC.LCTL, KC.LWIN, _______, KC.LALT,  KC.TAB,  KC.SPC,  KC.GRV, KC.NUHS,
           KC.A,   KC.N1,    KC.S,   KC.N2,    KC.D,    KC.F,   KC.N3,    KC.G,   KC.N4,    KC.H,   KC.N5,    KC.J,    
           KC.K,   KC.N6,    KC.L,   KC.N7, KC.SCLN, KC.QUOT,   KC.N8, KC.NUHS,   KC.N9,      L1,   KC.N0,      L2,
        KC.BSPC, KC.MINS, KC.RALT,  KC.EQL,      L3,  KC.INS, KC.HOME, KC.LEFT, KC.PGUP, KC.DOWN,   KC.UP, KC.RGHT,
         KC.ENT,
    ],
    [ # 1 QUERTY
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
           KC.Q, _______,    KC.W, _______,    KC.E,    KC.R, _______,    KC.T, _______,    KC.Y, _______,    KC.U,    
           KC.I, _______,    KC.O, _______,    KC.P, KC.LBRC, _______, KC.RBRC, _______, _______, _______, _______,
        _______, _______, _______, _______, _______, KC.PSCR, KC.SLCK, _______, KC.PAUS, _______, _______, _______,
        _______,
    ],
    [ # 2 ZXCV
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
           KC.Z, _______,    KC.X, _______,    KC.C,    KC.V, _______,    KC.B, _______,    KC.N, _______,    KC.M,    
        KC.COMM, _______,  KC.DOT, _______, KC.SLSH, _______, _______, _______, _______, _______, _______, _______,
        _______, _______, _______, _______, _______,  KC.DEL,  KC.END, _______, KC.PGDN, _______, _______, _______,
        _______,
    ],
    [ # 3 F
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,
        _______,   KC.F1, _______,   KC.F2, _______, _______,   KC.F3, _______,   KC.F4, _______,   KC.F5, _______,
        _______,   KC.F6, _______,   KC.F7, _______, _______,   KC.F8, _______,   KC.F9, _______,  KC.F10, _______,
        _______,  KC.F11, _______,  KC.F12, _______, _______, _______, _______, _______, _______, _______, _______,
        _______,
    ],
]
# fmt:on

if __name__ == "__main__":
    keyboard.go()
