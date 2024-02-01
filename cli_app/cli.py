import argparse
from argparse import Namespace

from cli_app import __app_name__


def say_something(args: Namespace):
    print(f'you are saying the following: {args.speak}')


def main():
    parser = argparse.ArgumentParser(prog=__app_name__,
                                     description='This program is only to test packaging and deployment',
                                     epilog="Dev. Carlos Correa")

    parser.add_argument('-s',
                        '--speak',
                        type=str,
                        help='Type something you wanna say')

    parser.set_defaults(func=say_something)

    args = parser.parse_args()
    args.func(args)
