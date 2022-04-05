#!/usr/bin/env python3

import sys
import pprint as pp
import re
import pandas as pd
from unidecode import unidecode

from typing import *

def get_lyrics_from_file(file_name: str) -> List[str]:

    song_lyrics = []
    with open(file_name, "r", errors="replace") as f:
        song_lyrics = f.readlines()

    return song_lyrics

def parse_songs(songs_list: List[str]) -> List[str]:
    pass


def main():
    if not sys.argv[1]:
        print("Usage: proclyrics.py <LYRICS.TXT>")
        return 1

    file_name = sys.argv[1]
    em_lyrics = get_lyrics_from_file(file_name)
    if not len(em_lyrics):
        print("[FATAL] The list of lyrics seems to be empty.")

    print("[+] Successfully loaded lyrics for processing")

    # Tokenize each song into lines....
    # Output csv file.

    # DEBUG
    pp.pprint(em_lyrics)



    return 0

if __name__ == "__main__":
    main()
