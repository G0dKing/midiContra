# Windows OS

MIDI_MAPPING = {
    'cc': {
        # CC messages
        1: 'mousemove',    # Example: Move mouse
        2: 'click',        # Example: Click mouse
        3: 'scrollup',     # Example: Scroll up
        4: 'scrolldown',   # Example: Scroll down
        # Add more CC mappings as needed
    },
    'notes': {
        # Note keys (white keys)
        60: 'win',      # Press Windows key
        62: 'd',        # Show Desktop (Win + D)
        64: 'tab',      # Switch Window (Alt + Tab)
        65: 'alt',      # Press Alt key
        67: 'f4',       # Close Window (Alt + F4)
        69: 'up',       # Arrow Up
        71: 'down',     # Arrow Down

        # Black keys (sharp/flat notes)
        61: 'lwin',     # Lock screen (Win + L)
        63: 'rwin',     # Open Run dialog (Win + R)
        66: 'enter',    # Enter key
        68: 'esc',      # Escape key

        # Additional white keys
        72: 'shift',    # Shift key
        74: 'ctrl',     # Ctrl key
        76: 'alt',      # Alt key (again, for completeness)
        77: 'space',    # Spacebar

        # Additional black keys
        73: 'backspace',    # Backspace
        75: 'delete',       # Delete
        78: 'pageup',       # Page Up
        80: 'pagedown',     # Page Down
    },
    'pc': {
        # Program Change messages (for presets or configurations)
        0: 'preset_1',    # Example: Switch to preset 1
        1: 'preset_2',    # Example: Switch to preset 2
        # Add more PC mappings as needed
    }
}

MIDI_TO_KEY_MAPPING = {
    # Note-on messages mapped to system functions
    60: 'volumeup',          # C4 - Increase Volume
    61: 'volumedown',        # C#4 - Decrease Volume
    62: 'mute',              # D4 - Mute/Unmute
    63: 'playpause',         # D#4 - Play/Pause Media
    64: 'nexttrack',         # E4 - Next Track
    65: 'prevtrack',         # F4 - Previous Track
    66: 'brightnessup',      # F#4 - Increase Brightness
    67: 'brightnessdown',    # G4 - Decrease Brightness
    68: 'screenshot',        # G#4 - Take Screenshot
    69: 'lockscreen',        # A4 - Lock Screen
    70: 'open_browser',      # A#4 - Open Web Browser
    71: 'close_window',      # B4 - Close Current Window

    # Control Change messages mapped to range functions
    10: 'volume',         # CC10 - Control Volume (0-127)
    11: 'brightness',     # CC11 - Control Brightness (0-127)
    12: ('mousemove', 10, 0),   # CC12 - Move Mouse Right (value: speed)
    13: ('mousemove', -10, 0),  # CC13 - Move Mouse Left (value: speed)
    14: ('mousemove', 0, 10),   # CC14 - Move Mouse Down (value: speed)
    15: ('mousemove', 0, -10),  # CC15 - Move Mouse Up (value: speed)
    16: 'launch_program1',  # CC16 - Launch Program 1
    17: 'launch_program2',  # CC17 - Launch Program 2
    # Add more CC mappings as needed
}
