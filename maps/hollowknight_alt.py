# hollowknight.py

MIDI_TO_KEY_MAPPING = {
    # Control Change messages mapped to game actions
    'cc': {
        # Pads
        2: 'space',          # CC0 - Jump
        6: 'z',        # CC1 - Attack
        26: 'left_ctrl',          # CC2 - Dash
        10: 'e',          # CC3 - Heal

        # Joystick X-axis (left and right movement)
        1: ('d', 10),    # CC10 - Move Right (value: speed)
        0: ('a', -10),    # CC11 - Move Left (value: speed)

        # Joystick Y-axis (up and down movement)
       22 : ('w', 10),       # CC20 - Look Up (value: speed)
        3: ('s', -10),    # CC21 - Look Down (value: speed)

        # Additional CC mappings
       7: 'c',
       5: 'tab',
       6: 'esc'
    }
}
