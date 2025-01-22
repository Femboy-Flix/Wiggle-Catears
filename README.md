# Wiggle-Cat Ears

## Project Overview
This project involves creating wiggling cat ears using a Raspberry Pi Pico or any compatible MicroPython development board. The setup is simple and involves minimal hardware and software requirements.

---

## Requirements

### Hardware
- **1x Development Board**: Raspberry Pi Pico (used in this project, other MicroPython-compatible boards should work).
- **2x Servo Motors**: 0-180 degrees range.
- **1x External Button**: e.g., an old PC power switch.
- **A Few Jumper Cables**: To connect the components.

### What I use
- **Affiliate Links**:
  - [Raspberry Pi Pico](https://amzn.to/4jtGd9k)
  - [Servo Motors](https://amzn.to/4h3CU74)
  - [Cat Ears](https://amzn.to/4h5Rta0)


### Software
- **MicroPython Editor**: Thonny IDE (recommended). Download from [https://thonny.org](https://thonny.org).
---

## Installation and Setup

### Step 1: Install Thonny IDE
1. Download and install Thonny from [https://thonny.org](https://thonny.org).
2. Ensure Thonny is set up for MicroPython.

### Step 2: Download the Files
1. Download the following Python files:
   - `servo.py`
   - `main.py`

### Step 3: Upload Files to the Development Board
1. Connect your development board to your computer via USB.
2. Open Thonny and set the interpreter to "MicroPython (Raspberry Pi Pico)".
3. Upload the `servo.py` and `main.py` files to the Raspberry Pi Pico:
   - In Thonny, navigate to `File` > `Save as...`.
   - Choose the Raspberry Pi Pico as the destination.

### Step 4: Wiring the Hardware
- **Button Connection**:
  - Connect one pin of the button to GPIO14 on the Raspberry Pi Pico.
  - Connect the other pin to GND.
- **Servo Motor Connection** (for a Raspberry Pi Pico):
  - Power/VCC (Red wire): Connect to PIN 5V (VBUS).
  - Ground (Black/Brown wire): Connect to GND.
  - Signal (Yellow/Orange/White wire): Connect to GPIO 0 (or another PWM-capable pin).

### Step 5: Run the Code
1. Open `main.py` in Thonny.
2. Click the **Run** button in Thonny to start the program.
3. Observe the servo motors moving as expected when interacting with the button.

---

## Future Enhancements
- **3D-Printed Parts**:
  - Designs for 3D-printed cat ears and mechanisms will be available in 2025.

---


