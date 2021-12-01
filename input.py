#!/usr/bin/env python3

import json
import sys
import urllib
import urllib.request

def main(year, day, out=None):
    with open("cookie.json") as f:
        cookie = json.load(f)
        req = urllib.request.Request("https://adventofcode.com/{}/day/{}/input".format(year, day))
        req.add_header("Cookie", "session={}".format(cookie['session']))
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8").strip())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./input.py <year> <day>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
