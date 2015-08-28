#!/usr/bin/env python

import os
import fnmatch
import argparse


def make_arg_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-d', '--path',
        dest='dir',
        default='.',
        type=str,
        action='store',
        help='path to dirrectory'
        )

    parser.add_argument(
        '-m', '--mask',
        dest='mask',
        default='*',
        type=str,
        action='store',
        help='mask for files'
        )

    parser.add_argument(
        '-s', '--summary',
        dest='summary',
        default=False,
        action='store_true',
        help='show only summary'
        )
    return parser


def parse_args(parser, args):
    try:
        args = parser.parse_args(args)
    except Exception, e:
        print e
        # parser.print_help()
        os.sys.exit(0)
    return args


def get_file_sloc(filepath):
    try:
        with open(filepath, 'rt') as f:
            return len(f.readlines())
    except:
        return -1


def analize_path(path, mask, summary):
    matches = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, mask):
            # print root, dirnames, filename
            filepath = os.path.join(root, filename)
            sloc = get_file_sloc(filepath)
            if not summary:
                print '{0:<80} [{1:>4}]'.format(filepath, sloc)
            if sloc > 0:
                matches.append(sloc)
    print 'Total size = %s' % sum(matches)


def main():
    parser = make_arg_parser()
    args = parse_args(parser, os.sys.argv[1:])
    analize_path(args.dir, args.mask, args.summary)


if __name__ == "__main__":
    main()