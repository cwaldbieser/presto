#! /usr/bin/python

import argparse
import codecs
import os.path


def main(args):
    fname = args.file
    base, ext = os.path.splitext(fname)
    source = fname
    if ext == ".rot13":
        dest = base
    else:
        dest = "{}.rot13".format(fname)
    with open(source, "r") as f:
        data = f.read()
    data = codecs.encode(data, "rot_13")
    with open(dest, "w") as f:
        f.write(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Encode / Decode Notes")
    parser.add_argument(
        "file",
        action="store",
        help="File to encode/decode.")
    args = parser.parse_args()
    main(args)
