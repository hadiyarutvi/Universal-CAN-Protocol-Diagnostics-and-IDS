
import time
import can

def main():
    bus = can.Bus(interface="socketcan", channel="vcan0")

    print("Engine simulator running. Press Ctrl+C to stop.")

    try:
        while True:
            message = can.Message(
                arbitration_id=0x100,
                data=[65, 0, 0, 0, 0, 0, 0, 0],
                is_extended_id=False
            )

            bus.send(message)
            print("Sent ID=0x100 DATA=41 00 00 00 00 00 00 00")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nSimulator stopped.")

    finally:
        bus.shutdown()

if __name__ == "__main__":
    main()
