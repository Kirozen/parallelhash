""" phash_console.py """

__author__ = "Etienne Faisant"
__date__ = "2015-03-11"

import multiprocessing as mp
import functools
import sys
import phash
from phash import format_size, read_input_file, write_output_file, file_hash_compare, file_hash, build_list, BaseCounter
import argparse


argparser = argparse.ArgumentParser(description='Parallel hasher.')
argparser.add_argument('paths', metavar='path', type=str, nargs='*', default=None, help='a path or file path')
argparser.add_argument('--version', action='version', version='%(prog)s 1.0')
argparser.add_argument('-d', '--direct', action='store_true', help='direct mode')
argparser.add_argument('-v', '--verify', action='store_true', help='verify files')
argparser.add_argument('-q', '--quiet', action='store_true', help='quiet mode (to be used with -o <file>')
argparser.add_argument(
    '-o', metavar='<output file>', type=argparse.FileType('w', encoding='UTF-8'), default=None, help='where to print')
argparser.add_argument('-j', metavar='n', choices=range(128), type=int, default=None,
                       help='number of processes, default: all available')

argparser.add_argument('-a', '--algo', metavar='alg', choices=['md5', 'sha1', 'sha256', 'sha512'],
                       default='md5', help='algorithm: md5, sha1, sha256, sha512, default: md5')


class ConsoleCounter(BaseCounter):

    def __init__(self, total=0, total_files=0, initval=0, initfval=0):
        BaseCounter.__init__(self, total, total_files, initval, initfval)

    def show_increment(self):
        print("Progression :", self.fval.value, "/", self.total_files, "files ", format_size(self.val.value),
              "/", format_size(self.total), "%.2f%%" % (self.val.value / self.total * 100.0), " " * 10, end="\r")

    def show_increment_count(self):
        print("Progression :", self.val.value, "/", self.total, "files %.2f%%" %
              (self.val.value / self.total * 100.0), " " * 10, end="\r")


def verify_files(args):
    if len(args.paths) != 1:
        print("Error : a file with hashes is required")
        sys.exit(-1)
    algo, total_size, nfiles, hashes = read_input_file(args.paths[0])
    phash.COUNTER = ConsoleCounter(nfiles)
    verif_pool = mp.Pool(args.j, initializer=phash.init, initargs=(phash.COUNTER,))
    try:
        results = verif_pool.map(
            functools.partial(file_hash_compare, quiet=args.quiet, hash_alg=algo), hashes)
        for res in results:
            if not res:
                print("\nComparison failed")
                break
        else:
            print("\nComparison passed")

        verif_pool.close()
    except KeyboardInterrupt:
        verif_pool.terminate()
    finally:
        verif_pool.join()


def hash_files(args):
    if args.quiet and not args.o:
        print("Error : an output file must be defined")
        sys.exit(-1)
    if args.direct:
        pass
    else:
        file_list, total_size = build_list(args.paths)
        file_list.sort()
        nfiles = len(file_list)
        phash.COUNTER = ConsoleCounter(total_size, nfiles)
        hash_pool = mp.Pool(args.j, initializer=phash.init, initargs=(phash.COUNTER,))
        try:
            hashlist = hash_pool.map(
                functools.partial(file_hash, quiet=args.quiet, hash_alg=args.algo), file_list)
            write_output_file(args.o, args.algo, total_size, nfiles, hashlist)
            hash_pool.close()
        except KeyboardInterrupt:
            hash_pool.terminate()
        finally:
            hash_pool.join()


if __name__ == '__main__':
    args = argparser.parse_args()
    if not args.paths:
        argparser.print_help()
        print("\n\nError: a path argument is required")
        sys.exit(-1)
    if args.verify:
        verify_files(args)
    else:
        hash_files(args)
