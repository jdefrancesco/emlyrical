#!/usr/bin/env python

"""proclyrics.py: This processes the eminem lyrics into a dataset
that we can use to train a LSTM-NN.
"""

import sys
import re
from typing import *

import pprint as pp
import numpy as np
from unidecode import unidecode


def get_lyrics_from_file(file_name: str) -> List[str]:
    """Grab all eminem lyrics from text file, store in a list."""
    song_lyrics = []
    with open(file_name, "r", errors="replace") as f:
        song_lyrics = f.readlines()

    return song_lyrics


def merge_lyrics(song_lyrics: List[str]) -> str:
    """Merge all the lyrics into one large string."""
    lyrics_text = ""
    for s in song_lyrics:
        # Each song begins and ends with these hash tokens.
        # We don't want these in our dataset..
        if s.startswith('###"') and s.endswith('"###'):
            continue
        else:
            lyrics_text += str(s).lower()

    return lyrics_text


def one_hot_encoding(lyrics: str) -> List[List]:
    """Encode the data set using one-hot-encoding.

    One-hot encoding is explained well in a hackernoon.com post.
    The link is a bit too long for the doc string, use google.

    NOTE: This code I mostly lifted the Drake lyric generator I
    saw on a Medium post by Ruslan Nikolaev.
    LINK:  https://nikolaevra.com
    """

    # Find unique chars.
    chars = sorted(list(set(lyrics)))
    print(f"Total unique characters: {len(chars)}")

    # Create two mappings. char -> indices and indices -> char
    char_indices = dict((c, i) for i, c in enumerate(chars))
    indices_char = dict((i, c) for i, c in enumerate(chars))

    # Cut text into sequences.
    max_len = 20
    step = 1 # step size at each iteration
    sentences = [] # list of sequences
    next_chars = [] # list of next characters our model should predict

    # ......

def main():

    if not sys.argv[1]:
        print("Usage: proclyrics.py <LYRICS.TXT>")
        return 1

    file_name = sys.argv[1]
    em_lyrics = get_lyrics_from_file(file_name)
    if not len(em_lyrics):
        print("[FATAL] The list of lyrics seems to be empty.")
        return 1

    print("[+] Successfully loaded lyrics for processing")

    # Tokenize each song into lines....
    all_lyrics = ""
    all_lyrics = merge_lyrics(em_lyrics)
    print(f"Lyric string length: {len(all_lyrics)}")

    # Create charater model...

    # Output csv file. (final Dataset we use to train emlyrical NN)

    # DEBUG



    return 0

if __name__ == "__main__":
    main()
