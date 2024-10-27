import time
import psutil
import subprocess
import os

ALLSTAR_APP_PATH = os.path.join(os.environ['LOCALAPPDATA'], 'Programs', 'Allstar', 'Allstar Desktop Application.exe')
KEEP_ALLSTAR_RUNNING = True  # Change to False if you want to stop Allstar when Steam closes

def get_running_processes():
    return {process.info['name'] for process in psutil.process_iter(['name'])}

def is_steam_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'steamwebhelper.exe':
            return True
    return False

def launch_allstar():
    if os.path.exists(ALLSTAR_APP_PATH):
        if not is_allstar_running():
            subprocess.Popen(ALLSTAR_APP_PATH, creationflags=subprocess.CREATE_NEW_CONSOLE)
            return True
    return False

def is_allstar_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'Allstar Desktop Application.exe':
            return True
    return False

already_launched = False

while True:
    if is_steam_running():
        if not already_launched:
            launch_allstar()
            already_launched = True
    else:
        if not KEEP_ALLSTAR_RUNNING:
            already_launched = False
            if is_allstar_running():
                for process in psutil.process_iter(['name']):
                    if process.info['name'] == 'Allstar Desktop Application.exe':
                        process.terminate()
    time.sleep(5)
