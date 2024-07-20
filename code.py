
import board

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()


keyboard.modules = [
    Layers(),
    HoldTap(),
]

keyboard.extensions.append(MediaKeys())

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO



# fmt: off
keyboard.keymap = []
# fmt:on

if __name__ == "__main__":
    keyboard.go()
