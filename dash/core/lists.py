
NONE_CHOICE = 0

# Musical Styles Choices
JAZZ_STYLE      = 1
FOLK_STYLE      = 2
ROCK_STYLE      = 3
BLUES_STYLE     = 4
ALT_STYLE       = 5
CLASSICAL_STYLE = 6
OTHER_STYLE     = 98
ANY_STYLE       = 99

STYLE_CHOICES = (
    (NONE_CHOICE,     '----'),
    (JAZZ_STYLE,      'jazz'),
    (FOLK_STYLE,      'folk'),
    (ROCK_STYLE,      'rock'),
    (BLUES_STYLE,     'blues'),
    (ALT_STYLE,       'alternative'),
    (CLASSICAL_STYLE, 'classical'),
    (OTHER_STYLE,     'other'),
    (ANY_STYLE,       'any'),
)

# A general list of instruments, not all encompassing
# maybe use this wiltonelder.com/list-of-music-instruments

ALTO_SAX_INST = 1
BARI_SAX_INST = 2
BASS_ELECTRIC_INST = 3
BASS_UPRIGHT_INST = 4
CELLO_INST = 5
CLARINET_INST = 6
DRUMSET_INST = 7
ELEC_KEYBOARD_INST = 8
FLUTE_INST = 9
GUITAR_ACOUSTIC_INST = 10
GUITAR_ELECTRIC_INST = 11
HARP_INST = 12
OTHER_INST = 13
PERCUSSION_INST = 14
PIANO_ACOUSTIC_INST = 15
SOPRANO_SAX_INST = 16
TENOR_SAX_INST = 17
TRUMPET_INST = 18
VIOLA_INST = 19
VIOLIN_INST = 20
VOCAL_INST = 21

INSTRUMENT_CHOICES  = (
    (NONE_CHOICE,       '-----'),
    (ALTO_SAX_INST,     'saxophone, alto'),
    (BARI_SAX_INST,     'saxophone, baritone'),
    (CELLO_INST,        'cello'),
    (CLARINET_INST,     'clarinet'),
    (DRUMSET_INST,      'drumset'),
    (ELEC_KEYBOARD_INST,'piano, electric'),
    (BASS_ELECTRIC_INST,'bass, electric'),
    (FLUTE_INST,        'flute'),
    (GUITAR_ACOUSTIC_INST,       'guitar, acoustic'),
    (GUITAR_ELECTRIC_INST,       'guitar, electric'),
    (HARP_INST,         'harp'),
    (OTHER_INST,        'other'),
    (PERCUSSION_INST,   'percussion'),
    (PIANO_ACOUSTIC_INST,        'piano, acoustic'),
    (SOPRANO_SAX_INST,  'saxophone, soprano'),
    (TENOR_SAX_INST,    'saxophone, tenor'),
    (TRUMPET_INST,      'trumpet'),
    (BASS_UPRIGHT_INST, 'bass, upright'),
    (VIOLA_INST,        'viola'),
    (VIOLIN_INST,       'violin'),
    (VOCAL_INST,        'vocals'),
)
