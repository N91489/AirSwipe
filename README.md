# AirSwipe
AirSwipe - Gesture-Based PPT Controller

AirSwipe is a computer vision-powered presentation controller that allows you to navigate through your slides using hand gestures. It leverages OpenCV and MediaPipe to detect swipe gestures and simulate keyboard key presses.

## Features & Use

- Swipe with open fist to simulate **left** or **right** key-press
- Closed fist do not simulate any key-press
- Uses **Python 3.11** with **opencv** & **mediapipe**

## Prerequisities
- Python 3.11
- A working webcam

## Demo

## Installation

**MAKE SURE TO USE PYTHON 3.11 !**

1. Clone the repository
   ```
   git clone https://github.com/N91489/AirSwipe.git
   cd AirSwipe
   ```
2. Create a virtual environment (optional but recommended)

   **Windows**
   ```
   python3.11m-m venv venv
    venv/Scripts/activate
   ```
   **macOS & Linux**
   ```
   python3.11 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

   ## Usage

   1. Run the script:
      ```
      python AirSwipe.py
      ```
   2. Exit by pressing **Ctrl/Command + Q** in the video feed
  
   # License
    MIT License. See LICENSE for details.












