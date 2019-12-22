# run using "python3 ex22.py {encoding type (utf-8, etc.)} {strict/replace}".

import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding, errors = errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding = "utf-8")

main(languages, input_encoding, error)


'''
raw_bytes = b'\xe6\x96\x87\xe8\x80'
utf_string = "文言"
raw_bytes.decode()
utf_string.encode()
raw_bytes == utf_string.encode()
utf_string == raw_bytes.decode()
'''
