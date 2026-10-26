import can
import cantools

CAN_INTERFACE = "socketcan"
CAN_CHANNEL = "vcan0"
ENGINE_DATA_ID = 0x100

def main():
    # Load the CAN database dictionary
    db = cantools.database.load_file("car_data.dbc")

    print("CAN Translator Started")
    print(f"Listening on {CAN_CHANNEL} for ID 0x{ENGINE_DATA_ID:X}")
    print("Press Ctrl+C to stop.\n")

    try:
        with can.Bus(
            interface=CAN_INTERFACE,
            channel=CAN_CHANNEL
        ) as bus:

            # Continuously receive CAN messages
            for message in bus:
                if message.is_error_frame or message.is_remote_frame:
                    continue

                if message.arbitration_id == ENGINE_DATA_ID:
                    try:
                        decoded = db.decode_message(
                            message.arbitration_id,
                            message.data
                        )

                        speed = decoded["Speed"]

                        print(
                            f"EngineData | "
                            f"CAN ID: 0x{message.arbitration_id:X} | "
                            f"Speed: {speed} mph"
                        )

                    except (cantools.database.DecodeError, KeyError) as error:
                        print(f"Unable to decode message: {error}")

    except KeyboardInterrupt:
        print("\nCAN Translator stopped.")

if __name__ == "__main__":
    main()
