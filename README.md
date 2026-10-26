# Universal CAN Protocol Diagnostics and IDS

## Current Implementation: Virtual CAN Engine Simulator

This project uses Linux SocketCAN and a virtual CAN interface (`vcan0`) to simulate and monitor CAN bus messages without physical CAN hardware.

### Features
- Virtual CAN interface setup using `vcan0`
- Cyclic transmission of synthetic CAN frames
- Standard 11-bit CAN identifier (`0x100`)
- Eight-byte CAN payload
- CAN frame monitoring using `candump`

### Technologies
- Python 3
- python-can
- Linux SocketCAN
- can-utils
- WSL2 Ubuntu

### Setup

Install the required system utility:

    sudo apt update
    sudo apt install can-utils

Activate the Python virtual environment and install dependencies:

    source .venv/bin/activate
    pip install python-can cantools

### Configure the virtual CAN interface

    sudo ./setup_vcan.sh

### Monitor CAN messages

Open another terminal and run:

    candump vcan0

### Run the engine simulator

    python3 engine_sim.py

The simulator is configured to transmit a standard CAN frame with ID `0x100` and payload `41 00 00 00 00 00 00 00` once per second.

### Notes
- `vcan0` is a virtual interface and does not require physical CAN hardware.
- This is the initial simulation component of the broader diagnostics and intrusion detection project.
- Only tested functionality should be described as verified.
