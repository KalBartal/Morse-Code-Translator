# This code is a Morse Code Translator program written in Python using the Tkinter library. It creates a window
# object, configures the window size and title, and then creates a frame, label, input field, button, and a text
# field for output to the user. The program contains a dictionary for all the Morse Code elements,
# and the encode_morse function takes in the user's input message and then encodes it using the morse_code
# dictionary. The function then deletes any existing output text in the fixed text field and inserts the encoded
# message into it. Finally, the enc_button is bound to the encode_morse function so once clicked it will return the
# encoded message to the user.

import tkinter as tk

# create a window object
window = tk.Tk()

# set window size
window.config(padx=30, pady=30, bg="#243763")

# set window title
window.title("Morse Code Translator")

# dictionary for morse code elements
morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
              'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
              'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
              'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
              'Z': '--..', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...', '8': '---..',
              '9': '----.', '0': '-----', ', ': '--..--',
              '.': '.-.-.-', '?': '..--..', '/': '-..-.',
              '-': '-....-', '(': '-.--.', ')': '-.--.-'}

# create a frame
frame = tk.Frame(window, bg="#243763")

# set frame background color
frame.configure(background="#FF6E31")

# set the frame grid
frame.grid()  # add 'columnspan=2' inside bracket

# Text label
wel_label = tk.Label(frame, text="Welcome to the Morse Code Translator!", fg="#FFEBB7", font=("Helvetica", 24))
wel_label.grid(row=1, column=0, padx=50, pady=10, columnspan=2)

# Input Label
inp_label = tk.Label(frame, text="Enter a message: ", font=("Helvetica", 18))
inp_label.grid(row=2, column=0, padx=5, sticky='w')

# Input field
inp_field = tk.Entry(frame, width=25, bg="#AD8E70", font=("Helvetica", 18))
inp_field.grid(row=2, column=1, pady=5)

# Button
enc_button = tk.Button(frame, text="Encode Message", bg="#FFEBB7", font=("helvetica", 18))
enc_button.grid(row=3, column=1, padx=5)

# Output Label
out_label = tk.Label(frame, text="Encoded message:", font=("Helvetica", 18))
out_label.grid(row=4, column=0, padx=5, pady=20, sticky='w')

# fixed text field
fixed_text_field = tk.Text(frame, width=25, height=2, bg="#AD8E70", font=("Helvetica", 18))
fixed_text_field.grid(row=4, column=1, columnspan=2, padx=5, pady=20)


def encode_morse(message_):
    # empty string to store the result
    encoded_message = ""

    # iterating the message string
    for letter in message_:

        # checks for space
        if letter == " ":
            # adds space
            encoded_message += "  "
        else:
            # adds the corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            encoded_message += morse_code[letter.upper()] + " "

    fixed_text_field.delete('1.0', tk.END)  # Remove existing output text
    fixed_text_field.insert('1.0', encoded_message)  # Insert encoded message


# bind an action to the button click
enc_button.configure(command=lambda: encode_morse(inp_field.get()))

window.mainloop()