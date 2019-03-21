import request
import argparse
import os

# Defines netloc
def getBaseURL():
    pass

# Defines argument parser
def parserFunc():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", help="Increase output verbosity.")
    parser.add_argument("--dry-run", help="Don't make any real calls.")
    pass
