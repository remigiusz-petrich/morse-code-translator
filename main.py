import argparse
import colorama

# Parser for command-line options, arguments and sub-commands
prog = 'Morse code translator'
version = '0.01'
parser = argparse.ArgumentParser(prog=prog)
parser.add_argument('-V', '--version', action='version', version=version)
parser.add_argument('-m', '--message', help='message to translate')
args = parser.parse_args()

colorama.init(autoreset=True)

space_between_letters = ' '
space_between_words = ' / '
morse_code_signals = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
    'z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
}
reversed_morse_code_signals = {value: key for key, value in morse_code_signals.items()}


def encode_message(message):
    encoded_message = ''
    words = message.lower().split()
    for word in words:
        for letter in word:
            if letter in morse_code_signals:
                encoded_message += morse_code_signals[letter] + space_between_letters
        encoded_message = encoded_message.rstrip(space_between_letters)  # remove last
        encoded_message += space_between_words
    encoded_message = encoded_message.rstrip(space_between_words)  # remove last
    return encoded_message


def decode_message(message):
    decoded_message = ''
    words = message.split(space_between_words)
    for word in words:
        letters = word.split(space_between_letters)
        for letter in letters:
            if letter in reversed_morse_code_signals:
                decoded_message += reversed_morse_code_signals[letter]
        decoded_message += ' '
    return decoded_message


def translate(message):
    if message.lower().split()[0] in reversed_morse_code_signals:
        print(decode_message(message))
    else:
        print(encode_message(message))


def main():
    print(colorama.Fore.CYAN + prog + ' ' + version)
    if args.message is None:
        message = input('Input message to translate:\n')
    else:
        message = args.message
    translate(message)


if __name__ == '__main__':
    main()
