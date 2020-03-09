"""
===========================
Pipeline seedvicious
===========================

Overview
========

A short description (one paragraph).

Usage
=====

	python pipeline_seedvicious.py make full -v 5

Configuration
=============

	python pipeline_seedvicious.py config

Input files
===========

/path/file

	Description of the file.

Requirements
============

* python (≥ 3.6.7)
* cgatcore (≥ 0.5.15)
    * ruffus (≥ 2.8.3)
* seedVicious (≥ 1.3)

Pipeline output
===============

/path/file

	Description of the file.

Glossary
========

term

	Description of the term.

"""

import os
import sys

from ruffus import *
from cgatcore import pipeline as P

# Load options from the config file
PARAMS = P.get_parameters(
    ["%s/pipeline.yml" % os.path.splitext(__file__)[0],
     "../pipeline.yml",
     "pipeline.yml"])


@files(None, ["test.out", "test.err"])
def test(infile, outfiles):
    '''Run seedViciousTest'''
    
    stdout = outfiles[0]
    stderr = outfiles[1]

    statement = '''seedViciousTest 1>%(stdout)s 2> %(stderr)s'''

    P.run(statement)


@follows(test)
def full():
    pass


def main(argv=None):
    if argv is None:
        argv = sys.argv
    P.main(argv)


if __name__ == "__main__":
    sys.exit(P.main(sys.argv))
