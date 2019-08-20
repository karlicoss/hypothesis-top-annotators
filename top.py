#!/usr/bin/env python3
import json
import sys
from pathlib import Path
from time import sleep

from kython.misc import import_file

hypothesis = import_file(Path('/L/repos/Hypothesis/hypothesis.py'), 'hypothesis')

# https://hypothes.is/account/developer
from hypothesis_secrets import HYPOTHESIS_USER, HYPOTHESIS_TOKEN

def download():
    h = hypothesis.Hypothesis(
        username=HYPOTHESIS_USER,
        token=HYPOTHESIS_TOKEN,
        max_search_results=100000, # None would set it to 2000 (hardcoded in Hypothesis class)
    )
    # TODO use search_after instead... https://h.readthedocs.io/en/latest/api-reference/#tag/annotations/paths/~1search/get

    data = []

    def dump():
        fo = sys.stdout
        with open('res.json', 'w') as fo:
            json.dump(data, fo, indent=2, ensure_ascii=False)

    from pprint import pprint
    for a in h.search_all():
        if len(data) > 9000:
            # TODO 9800 limit
            break
        data.append(a)
        print(f'downloaded {len(data)}')
        if len(a) % 100 == 0:
            dump()

    dump()

def main():
    download()

if __name__ == '__main__':
    main()
