#!/usr/bin/env python3
# SPDX-License-Identifier: 0BSD

from argparse import ArgumentParser
from make_password import make_password

def main() -> None:
    epilog = ("https://cheatsheetseries.owasp.org/cheatsheets"
              "/Authentication_Cheat_Sheet.html")
    parser = ArgumentParser(description="make a password",
                            epilog=epilog)
    parser.add_argument("-d", "--no_punctuation", action="store_true",
                        help="do not use default punctuation chars")
    parser.add_argument("-o", "--custom_chars", help="set custom chars")
    parser.add_argument("-w", "--passphrase", action="store_true",
                        help="make a passphrase")
    parser.add_argument("-n", "--length", type=int, help="set the length")
    args = parser.parse_args()

    passphrase = args.passphrase
    length = args.length or (14 if passphrase else 40)
    if length < 4:
        parser.error("Too short length")
    else:
        password = make_password(length, passphrase, args.no_punctuation,
                                 args.custom_chars)
        print(password)

if __name__ == "__main__":
    main()
