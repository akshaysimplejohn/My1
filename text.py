import pyautogui
import time
import os

# Optional: small delay so you can switch to the target screen
time.sleep(2)

# List of 5 (x, y) screen coordinates
coordinates = [
    (100, 100),
    (400, 200),
    (800, 300),
    (600, 600),
    (300, 500)
]

# Create a folder for screenshots
output_dir = "screenshots"
os.makedirs(output_dir, exist_ok=True)

for i, (x, y) in enumerate(coordinates, start=1):
    # Move mouse to the coordinate
    pyautogui.moveTo(x, y, duration=0.5)

    # Small pause to ensure screen is stable
    time.sleep(0.5)

    # Take screenshot
    screenshot_path = os.path.join(output_dir, f"screenshot_{i}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)

    print(f"Moved to ({x}, {y}) and saved {screenshot_path}")

print("Done.")
