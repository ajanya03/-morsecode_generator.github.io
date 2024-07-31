

morse_code_list = {
    'A': '.-','N': '-.',
    'B': '-...','O': '---',
    'C': '-.-.','P': '.--.',
    'D': '-..','Q': '--.-',
    'E': '.','R': '.-.',
    'F': '..-.','S': '...',
    'G': '--.','T': '-',
    'H': '....','U': '..-',
    'I': '..','V': '...-',
    'J': '.---','W': '.--',
    'K': '-.-','X': '-..-',
    'L': '.-..','Y': '-.--',
    'M': '--','Z': '--..'
}

def morse_code_generator():

    while True:
        user_input = input("Enter your alphabet to get morse code or enter (exit) to exit : ").upper()
        if len(user_input) != 4:
            morse_code = morse_code_list[user_input]
            print("Corresponding morse code \n ",user_input," = ",morse_code)
        else:
            break
    print("Thank you for using our system :) ")

morse_code_generator()