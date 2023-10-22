from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.string_substitution import StringSubstitution
from kmk.modules.combos import Chord

keyboard = KMKKeyboard()

keyboard.modules.append(
    StringSubstitution(dictionary = {
        ':sc': 'Sertan Canpolat',
        ':gh': 'https://github.com/scnplt',
    })
)

_______ = KC.TRNS
XXXXXXX = KC.NO

NUMNAV = KC.MO(1)
SYMBL = KC.MO(2)
FN = KC.MO(3)
MOUSE_TG = KC.TG(4)

TAB_LSFT = KC.HT(KC.TAB, KC.LSFT)
QUOT_RSFT = KC.HT(KC.QUOT, KC.RSFT)
BSLS_MEH = KC.HT(KC.BSLS, KC.MEH)
DEL_FN = KC.HT(KC.DEL, FN)

keyboard.combos.combos = [
    Chord((KC.ESC, KC.Q), KC.CAPS),
    Chord((KC.Y, KC.U), KC.LCTRL(KC.Z)),
    Chord((KC.U, KC.I), KC.LCTRL(KC.Y)),
    Chord((KC.F, KC.G), KC.LGUI),
    Chord((KC.H, KC.J), KC.RGUI),
    Chord((KC.F, KC.V), KC.LGUI(KC.V)),
]

keyboard.keymap = [
    # BASE
    [
        KC.ESC,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,               KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.BSPC,
        TAB_LSFT,   KC.A,       KC.S,       KC.D,       KC.F,       KC.G,               KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    QUOT_RSFT,
        KC.LCTRL,   KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,               KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,    BSLS_MEH,
                                            KC.LALT,    SYMBL,      KC.SPC,             KC.ENT,     NUMNAV,     DEL_FN
    ],

    # NUMNAV
    [
        XXXXXXX,    KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,              KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      _______,
        KC.LSFT,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,            KC.LEFT,    KC.DOWN,    KC.UP,      KC.RGHT,    XXXXXXX,    KC.RSFT,
        _______,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,            KC.HOME,    KC.PGDN,    KC.PGUP,    KC.END,     XXXXXXX,    XXXXXXX,
                                            _______,    XXXXXXX,    _______,            XXXXXXX,    _______,    KC.APP
    ],

    # SYMBL
    [
        XXXXXXX,    KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,            KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.MINS,    KC.EQL,     KC.TILD,
        XXXXXXX,    XXXXXXX,    XXXXXXX,    KC.LCBR,    KC.LBRC,    KC.LPRN,            XXXXXXX,    XXXXXXX,    XXXXXXX,    KC.UNDS,    KC.PLUS,    KC.GRV,
        XXXXXXX,    XXXXXXX,    XXXXXXX,    KC.RCBR,    KC.RBRC,    KC.RPRN,            XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
                                            XXXXXXX,    _______,    XXXXXXX,            XXXXXXX,    XXXXXXX,    XXXXXXX
    ],

    # FN
    [
        XXXXXXX,    KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,              KC.F6,      KC.F7,      KC.F8,      KC.F9,      KC.F10,     MOUSE_TG,
        XXXXXXX,    KC.F11,     KC.F12,     XXXXXXX,    XXXXXXX,    XXXXXXX,            KC.MPRV,    KC.VOLD,    KC.VOLU,    KC.MNXT,    XXXXXXX,    XXXXXXX,
        _______,    KC.RESET,   KC.DEBUG,   XXXXXXX,    XXXXXXX,    XXXXXXX,            KC.MPLY,    KC.MUTE,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
                                            _______,    XXXXXXX,    XXXXXXX,            KC.PSCR,    KC.INS,     _______
    ],

    # MOUSE
    [
        XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,            KC.MW_UP,   KC.MB_BTN4, KC.MS_UP,   KC.MB_BTN5, XXXXXXX,    MOUSE_TG,
        XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,            KC.MW_DN,   KC.MS_LT,   KC.MS_DN,   KC.MS_RT,   XXXXXXX,    XXXXXXX,
        XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,            XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,    XXXXXXX,
                                            XXXXXXX,    XXXXXXX,    XXXXXXX,            KC.MB_LMB,  KC.MB_MMB,  KC.MB_RMB
    ], 
]

if __name__ == '__main__':
    keyboard.go()
