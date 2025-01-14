"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2

def ValidatePregnum(resp):
    preg = nsfg.ReadFemPreg()
    preg_map = nsfg.MakePregMap(preg)

    for index, pregnum in resp.pregnum.iteritems():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]

        if len(indices) != pregnum:
            return False

    return True

def main(script):
    """Tests the functions in this module.

    script: string script name
    """

    resp = nsfg.ReadFemResp()

    print(resp.pregnum.value_counts().sort_index())

    assert(ValidatePregnum(resp))

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
