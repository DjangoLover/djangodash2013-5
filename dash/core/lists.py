# Musical Styles Choices
NO_STYLE        = 0
JAZZ_STYLE      = 1
FOLK_STYLE      = 2
ROCK_STYLE      = 3
BLUES_STYLE     = 4
ALT_STYLE       = 5
CLASSICAL_STYLE = 6
OTHER_STYLE     = 98
ANY_STYLE       = 99

STYLE_CHOICES = (
    ('NO_STYLE',        'none'),
    ('JAZZ_STYLE',      'jazz'),
    ('FOLK_STYLE',      'folk'),
    ('ROCK_STYLE',      'rock'),
    ('BLUES_STYLE',     'blues'),
    ('ALT_STYLE',       'alternative'),
    ('CLASSICAL_STYLE', 'classical'),
    ('OTHER_STYLE',     'other'),
    ('ANY_STYLE',       'any'),
)

# A general list of instruments, not all encompassing
# maybe use this wiltonelder.com/list-of-music-instruments
VOCAL_INST          = 0
GUITAR_INST         = 1
ELECTRIC_BASS_INST  = 2
DRUMSET_INST        = 3
PERCUSSION_INST     = 4
PIANO_INST          = 5
VIOLIN_INST         = 6
VIOLA_INST          = 7
CELLO_INST          = 8
UPRIGHT_BASS_INST   = 9
FLUTE_INST          = 10
CLARINET_INST       = 11
SOPRANO_SAX_INST    = 12
ALTO_SAX_INST       = 13
TENOR_SAX_INST      = 14
BARI_SAX_INST       = 15
TRUMPET_INST        = 16
OTHER_INST          = 17
HARP_INST           = 18
ELEC_KEYBOARD_INST  = 19

INSTRUMENT_CHOICES  = (
    (ALTO_SAX_INST,     '1'),
    (BARI_SAX_INST,     '2'),
    (CELLO_INST,        '3'),
    (CLARINET_INST,     '4'),
    (DRUMSET_INST,      '5'),
    (ELEC_KEYBOARD_INST,'6'),
    (ELECTRIC_BASS_INST,'7'),
    (FLUTE_INST,        '8'),
    (GUITAR_INST,       '9'),
    (HARP_INST,         '10'),
    (OTHER_INST,        '11'),
    (PERCUSSION_INST,   '12'),
    (PIANO_INST,        '13'),
    (SOPRANO_SAX_INST,  '14'),
    (TENOR_SAX_INST,    '15'),
    (TRUMPET_INST,      '16'),
    (UPRIGHT_BASS_INST, '17'),
    (VIOLA_INST,        '18'),
    (VIOLIN_INST,       '19'),
    (VOCAL_INST,        '20'),
)
