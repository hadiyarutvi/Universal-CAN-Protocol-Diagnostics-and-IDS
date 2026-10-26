# Universal CAN Protocol Diagnostics and IDS

A Python-based project for simulating CAN bus communication and decoding vehicle signals using Linux SocketCAN, `python-can`, and `cantools`.

## Features

- Virtual CAN interface setup using `vcan0`
- Periodic transmission of simulated CAN frames
- Standard 11-bit CAN identifier (`0x100`)
- Raw CAN frame monitoring using `candump`
- DBC-based CAN message decoding
- Human-readable engine speed output in mph

## Project Structure

| File | Description |
|---|---|
| `setup_vcan.sh` | Configures the virtual CAN interface |
| `engine_sim.py` | Transmits simulated engine data |
| `car_data.dbc` | Defines the CAN message and Speed signal |
| `translator.py` | Receives and decodes CAN messages |
| `candump_output.png` | Raw CAN monitoring screenshot |
| `translator_output.png` | Decoded CAN output screenshot |

## How It Works

1. Configure the virtual CAN interface.
2. Run the engine simulator to transmit a CAN frame every second.
3. Monitor raw CAN traffic using `candump`.
4. Decode the received payload using the DBC file.
5. Display the decoded engine speed in mph.

### Example CAN Frame

- **CAN ID:** `0x100` (decimal 256)
- **Payload:** `41 00 00 00 00 00 00 00`
- **Message:** `EngineData`
- **Decoded speed:** `65 mph`

The DBC defines `Speed` as an unsigned 8-bit signal starting at bit 0, with a scale of 1 and offset of 0.

## Requirements

- Ubuntu/Linux or Ubuntu on WSL2
- Python 3
- `can-utils`
- `python-can`
- `cantools`

## Installation

Install the system dependency:

```bash
sudo apt update
sudo apt install -y can-utils
```

Activate the Python virtual environment and install the Python packages:

```bash
source .venv/bin/activate
python -m pip install python-can cantools
```

## Configure Virtual CAN

```bash
sudo ./setup_vcan.sh
ip link show vcan0
```

## Run the Project

Use separate terminals for the simulator, raw monitor, and translator.

### Terminal 1: Engine Simulator

```bash
cd ~/can_project
source .venv/bin/activate
python3 engine_sim.py
```

### Terminal 2: Raw CAN Monitor

```bash
candump vcan0
```

### Terminal 3: DBC Translator

```bash
cd ~/can_project
source .venv/bin/activate
python3 translator.py
```

Expected decoded output:

```text
CAN Translator Started
Listening on vcan0 for ID 0x100
Press Ctrl+C to stop.

EngineData | CAN ID: 0x100 | Speed: 65 mph
```

The decoded speed should appear repeatedly while the simulator is transmitting.

## Troubleshooting

- **`vcan0` not found:** Run `sudo ./setup_vcan.sh`.
- **No messages received:** Confirm the simulator is running and all programs use `vcan0`.
- **DBC file not found:** Run the translator from the project directory.
- **Python import errors:** Activate `.venv` and install the required packages.

## Roadmap

- Add more CAN messages and signals.
- Expand diagnostic checks and signal validation.
- Develop and evaluate intrusion-detection rules using simulated CAN traffic.

## Disclaimer

This is a learning and prototyping project using synthetic data on a virtual CAN interface. The current implementation does not connect to a real vehicle and is not a production-ready intrusion detection system.
