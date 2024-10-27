import time
import psutil
import subprocess
import os
import logging
from datetime import datetime

# Generate a timestamp for the log file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file_name = f'debug_{timestamp}.log'

# Set up logging to both console and file
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_name),  # Log to file with timestamp
        logging.StreamHandler()                # Log to console
    ]
)

# Expand the local app data path for Allstar
ALLSTAR_APP_PATH = os.path.join(os.environ['LOCALAPPDATA'], 'Programs', 'Allstar', 'Allstar Desktop Application.exe')

# User toggle to keep Allstar running after Steam closes
KEEP_ALLSTAR_RUNNING = True  # Change to False if you want to stop Allstar when Steam closes

def log_process_changes(previous_processes, current_processes):
    """Log any processes that have started or stopped since the last check."""
    added_processes = current_processes - previous_processes
    removed_processes = previous_processes - current_processes

    if added_processes:
        for process in added_processes:
            logging.debug(f"Process started: {process}")
    
    if removed_processes:
        for process in removed_processes:
            logging.debug(f"Process stopped: {process}")

def get_running_processes():
    """Return a set of currently running process names."""
    return {process.info['name'] for process in psutil.process_iter(['name'])}

def is_steam_running():
    """Check if steamwebhelper.exe is running."""
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'steamwebhelper.exe':
            logging.debug("Steam Web Helper is running.")
            return True
    logging.debug("Steam Web Helper is not running.")
    return False

def launch_allstar():
    """Launch the Allstar application."""
    if os.path.exists(ALLSTAR_APP_PATH):
        # Launch Allstar in a new console window
        subprocess.Popen(ALLSTAR_APP_PATH, creationflags=subprocess.CREATE_NEW_CONSOLE)
        logging.debug("Allstar.gg launched.")
    else:
        logging.error(f"Allstar.gg path not found: {ALLSTAR_APP_PATH}")

def is_allstar_running():
    """Check if the Allstar application is currently running."""
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'Allstar Desktop Application.exe':
            logging.debug("Allstar.gg is currently running.")
            return True
    logging.debug("Allstar.gg is not running.")
    return False

# Main loop
previous_processes = get_running_processes()  # Get initial running processes
already_launched = False

while True:
    current_processes = get_running_processes()  # Get the current running processes
    log_process_changes(previous_processes, current_processes)  # Log any changes

    if is_steam_running():
        if not already_launched:
            launch_allstar()
            already_launched = True
    else:
        if KEEP_ALLSTAR_RUNNING:
            logging.debug("Steam is closed, but Allstar is still running.")
        else:
            already_launched = False

    previous_processes = current_processes  # Update the previous processes for the next check
    time.sleep(5)
