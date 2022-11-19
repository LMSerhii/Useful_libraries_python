from stegano import lsb


def first_method_encoding():
    """ encrypt to image with lsb """
    secret = lsb.hide("img/1.png", "secret text")
    secret.save("img/1_secret.png")


def first_method_decoding():
    """ decrypt to image with lsb """
    result = lsb.reveal("img/1_secret.png")
    print(result)


def main():
    # first_method_encoding()
    first_method_decoding()


if __name__ == '__main__':
    main()