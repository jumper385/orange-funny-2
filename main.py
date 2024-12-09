import logging
import argparse
import sys

logging.basicConfig(level=logging.INFO)

def main():
    # generate a cli that prints the os version and the python version
    parser = argparse.ArgumentParser(description='Print the os and python version')

    # EITHER an os, or python flag is required. both allowed too in which case both is printed...
    parser.add_argument('--os', '-o', action='store_true', help='Print the os version')
    parser.add_argument('--python', '-p', action='store_true', help='Print the python version')

    args = parser.parse_args()
    print(args)

    if args.os:
        os_ver = sys.platform
        logging.info(f'OS_VER: {os_ver}')

    if args.python:
        py_ver = sys.version
        logging.info(f"PYTHON_VER: {py_ver}")
    
    if not args.os and not args.python:
        logging.error('Please provide an argument')

if __name__ == '__main__':
    main()