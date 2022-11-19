from PyPDF2 import PdfFileWriter, PdfFileReader


def encryption():
    """ this function encrypts the pdf file """


def decryption():
    """ this function decrypts pdf file """


def main():
    choose = input("[+] Enter 0 to  encrypt the file, enter 1 to the decrypt: ")
    encryption() if choose == "0" else decryption()


if __name__ == '__main__':
    main()