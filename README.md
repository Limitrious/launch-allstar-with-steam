
# Launch Allstar with Steam

This repository provides a way to launch the Allstar application with Steam, bypassing the typical autostart process for faster loading. You can choose to use the executable file provided in the Release tab or run the Python script directly.

The executable was created from the Python script using PyInstaller. If you'd like to modify the script and rebuild the executable, follow the instructions below.

You can choose whether to keep the Allstar application running after Steam closes by modifying the `KEEP_ALLSTAR_RUNNING` variable in the `launch_allstar_with_steam.py` script. Set it to true to keep Allstar running, or `false` to `close` it when Steam exits.

## Building the Executable

To build the executable from the Python script, you’ll need [PyInstaller](https://pyinstaller.org/en/stable/). Install PyInstaller using:

```bash
pip install pyinstaller
```

Then, use one of the following commands:

- **With console:**  
  ```bash
  pyinstaller --onefile launch_allstar_with_steam.py
  ```

- **Without console:**  
  ```bash
  pyinstaller --onefile --noconsole launch_allstar_with_steam.py
  ```

The built executable will be located in the `dist` folder.

## Adding to Windows Startup

To run the Allstar application automatically when Windows starts, you can only add the executable file (`launch_allstar_with_steam.exe`) to the Startup folder; the Python script cannot be set to run at startup. Follow these steps:

1. Press `Win + R` to open the Run dialog.
2. Type `shell:startup` and press Enter. This will open the Startup folder.
3. Create a shortcut of the executable and place it in the Startup folder.

The application will now start automatically each time you log into Windows.

## Running the Python Script

If you prefer running the Python script directly, install the required dependencies with:

```bash
pip install -r requirements.txt
```

## Requirements

- **Python Version:** Python 3.11.0
