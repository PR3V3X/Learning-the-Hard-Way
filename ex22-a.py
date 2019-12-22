import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    text = line.strip()
    decoded = text.decode(encoding, errors = errors)

    print(decoded)


languages = open("lang.txt", 'rb')

main(languages, input_encoding, error)
