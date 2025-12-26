import subprocess
import sys
import time
packages = ['pywinauto', 'pywin32', 'comtypes', 'pyautogui']
print("Checking dependencies...")

try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)
except subprocess.CalledProcessError as e:
    print(f"Error installing packages: {e}")
    sys.exit(1)

print("All dependencies installed.")

import pyautogui
import os

# --- CONFIG ---
CLICK_X, CLICK_Y = 1100, 725
WAIT_TIME = 30
SCREENSHOT_DIR = "screenshots"

os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def take_screenshot(name):
    path = os.path.join(SCREENSHOT_DIR, name)
    pyautogui.screenshot(path)
    print(f"Screenshot saved: {path}")

# --- 1. DEPENDENCY CHECK ---
packages = ['pywinauto', 'pywin32', 'comtypes', 'pyautogui']
print("Checking dependencies...")

try:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + packages)
except subprocess.CalledProcessError as e:
    print(f"Error installing packages: {e}")
    sys.exit(1)

print("Dependencies installed.")
take_screenshot("01_after_install.png")

# --- 2. RUN kryptex.exe ---
kryptex_path = os.path.join(os.getcwd(), "kryptex.exe")

if not os.path.exists(kryptex_path):
    print(f"Error: kryptex.exe not found at {kryptex_path}")
    sys.exit(1)

print("Launching Kryptex...")
subprocess.Popen(kryptex_path, shell=True)

time.sleep(5)  # short delay to let window appear
take_screenshot("02_after_launch.png")

# --- 3. WAIT 30 SECONDS ---
print(f"Waiting {WAIT_TIME} seconds...")
time.sleep(WAIT_TIME)
take_screenshot("03_after_wait.png")

# --- 4. MOVE MOUSE AND DOUBLE CLICK ---
print("Moving mouse and double-clicking...")
pyautogui.moveTo(CLICK_X, CLICK_Y, duration=0.5)
pyautogui.doubleClick()

time.sleep(1)
take_screenshot("04_after_double_click.png")
time.sleep(30)
take_screenshot("05_after_wait.png")

print("All actions completed.")
