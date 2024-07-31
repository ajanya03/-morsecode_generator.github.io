

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
        user_input = input("Enter your alphabet to get morse code or enter (0) to exit : ").upper()
        if user_input == '0':
            print("Thank you for using our system :) ")
        else:
            morse_code = morse_code_list[user_input]
            print("Corresponding morse code \n ",user_input," = ",morse_code)
   
morse_code_generator()