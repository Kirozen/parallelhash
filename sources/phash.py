""" phash.py """

__author__ = "Etienne Faisant"
__date__ = "2014-10-20"

import hashlib
import multiprocessing as mp
import ctypes
import os

HASH_ALGO = {'md5': hashlib.md5, 'sha1': hashlib.sha1, 'sha256': hashlib.sha256, 'sha512': hashlib.sha512}
COUNTER = None


def init(args):
    global COUNTER
    COUNTER = args


class BaseCounter(object):

    def __init__(self, total=0, total_files=0, initval=0, initfval=0):
        self.val = mp.Value(ctypes.c_size_t, initval)
        self.total = total
        self.interval = total * 0.01 / 100
        self.total_files = total_files
        self.fval = mp.Value(ctypes.c_size_t, initfval)
        self.actual = 0
        self.lock = mp.Lock()

    def set_total(self, total):
        self.total = total
        self.interval = total * 0.01 / 100

    def increment_files(self):
        with self.lock:
            self.fval.value += 1

    def increment(self, amount=1):
        with self.lock:
            self.val.value += amount
            if self.val.value > self.actual + self.interval or self.val.value >= self.total:
                self.actual = self.val.value
                self.show_increment()

    def show_increment(self):
        pass

    def increment_count(self, amount=1):
        with self.lock:
            self.val.value += amount
            if self.val.value > self.actual + self.interval or self.val.value >= self.total:
                self.actual = self.val.value
                self.show_increment_count()

    def show_increment_count(self):
        pass


def format_size(size):
    if size < 1025:
        return "{:.2f} B".format(size)
    elif size < 1048577:
        return "{:.2f} KB".format(size / 1024)
    elif size < 1073741825:
        return "{:.2f} MB".format(size / 1048576)
    elif size < 1099511627777:
        return "{:.2f} GB".format(size / 1073741824)
    else:
        return "{:.2f} TB".format(size / 1099511627776)


def buf_size(file_size):
    if file_size < 16777217:
        return 8192
    if file_size < 1073741825:
        return 16384
    return 32768


class KeyboardInterruptError(Exception):
    pass


def write_output_file(output, algo, total_size, nfiles, hashlist):
    if not output:
        return
    output.write("%s#%d#%d\n" % (algo, total_size, nfiles))
    for digest, fname in hashlist:
        if digest:
            output.write("%s - %s\n" % (digest, fname))


def read_input_file(fname):
    hashes = []
    algo = None
    total_size = 0
    nfiles = 0
    with open(fname) as hashreader:
        header = hashreader.readline().split('#')
        algo = header[0]
        total_size = int(header[1])
        nfiles = int(header[2])
        for line in hashreader:
            hashes.append(line.split(' - '))
    return algo, total_size, nfiles, hashes


def file_hash(the_file, quiet, hash_alg):
    try:
        block_size = buf_size(os.path.getsize(the_file))
        hasher = HASH_ALGO[hash_alg]()
        global COUNTER
        with open(the_file, 'rb') as fr:
            if COUNTER:
                COUNTER.increment_files()
            buf = fr.read(block_size)
            while len(buf) > 0:
                hasher.update(buf)
                if COUNTER:
                    COUNTER.increment(len(buf))
                buf = fr.read(block_size)
        if not quiet:
            print(hasher.hexdigest(), "-", the_file)
        return (hasher.hexdigest(), the_file)
    except KeyboardInterrupt:
        raise KeyboardInterruptError
    except PermissionError:
        print("PermissionError: %s" % the_file)
        return (None, the_file)


def file_hash_compare(hashdata, quiet, hash_alg):
    hashed = hashdata[0]
    the_file = hashdata[1].rstrip()
    try:
        block_size = buf_size(os.path.getsize(the_file))
        hasher = HASH_ALGO[hash_alg]()
        global COUNTER
        with open(the_file, 'rb') as fr:
            buf = fr.read(block_size)
            while len(buf) > 0:
                hasher.update(buf)
                buf = fr.read(block_size)
        if COUNTER:
            COUNTER.increment_count()
        if not quiet:
            print(the_file, ':', ['OK', 'KO'][hashed != hasher.hexdigest()], ' ' * 10)
        return hashed == hasher.hexdigest()
    except KeyboardInterrupt:
        raise KeyboardInterruptError
    except PermissionError:
        print("PermissionError: %s" % the_file)
        return False


def build_list(paths):
    files_list = []
    total_size = 0
    for path in paths:
        print(path)
        for root, _, files in os.walk(path):
            print("%d files discovered -" %
                  len(files_list), format_size(total_size), " " * 4, end="\r")
            for file in files:
                total_size += os.path.getsize(os.path.join(root, file))
                files_list.append(os.path.join(root, file))
    print("%d files discovered -" % len(files_list), format_size(total_size))
    return files_list, total_size
