import mido
import pyautogui
import importlib.util
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
MIDI_PORT_NAME = 'MPK mini 3 0'

# Load Mappings
def load_mapping(file_path):
    try:
        spec = importlib.util.spec_from_file_location("mapping_module", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.MIDI_TO_KEY_MAPPING
    except Exception as e:
        logging.error(f"Error loading mapping from {file_path}: {e}")
        return {}

# Load Initial Mapping
current_mapping = load_mapping('maps/windows.py')

# Open MIDI Port
try:
    port = mido.open_input(MIDI_PORT_NAME)
    logging.info(f"Opened MIDI port: {MIDI_PORT_NAME}")
except IOError:
    logging.error(f"Error opening MIDI port: {MIDI_PORT_NAME}")
    exit()

# Capture MIDI
logging.info("Awaiting Input...")

while True:
    try:
        for msg in port.iter_pending():
            logging.info(f"{msg}")
            if msg.type == 'note_on':
                note = msg.note
                if note in current_mapping:
                    key = current_mapping[note]
                    pyautogui.keyDown(key)
                    logging.info(f"Note ON: {note} -> Key Down: {key}")
            elif msg.type == 'note_off':
                note = msg.note
                if note in current_mapping:
                    key = current_mapping[note]
                    pyautogui.keyUp(key)
                    logging.info(f"Note OFF: {note} -> Key Up: {key}")
            elif msg.type == 'control_change':
                control = msg.control
                value = msg.value
                if control in current_mapping['cc']:
                    command = current_mapping['cc'][control]
                    if isinstance(command, str):
                        pyautogui.keyDown(command)
                        logging.info(f"Control Change: {control} -> Command: {command}")
            elif isinstance(command, tuple) and command[0] == 'mousemove':
                        x, y = command[1:]
                        pyautogui.moveRel(x, y)
                        logging.info(f"Control Change: {control} -> Mouse Move: ({x}, {y})")
            elif msg.type == 'program_change':
                program = msg.program
                if program in current_mapping['pc']:
                    command = current_mapping['pc'][program]
                    logging.info(f"Program Change: {program} -> Command: {command}")
        time.sleep(0.01)
    except Exception as e:
        logging.error(f"Error processing MIDI message: {e}")

# Close Port on Exit
port.close()
