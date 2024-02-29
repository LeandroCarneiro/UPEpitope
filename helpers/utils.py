import io
import glob


def find_files(path):
    return glob.glob(path)


def read_lines(fileName):
    lines = io.open(
        fileName, encoding='utf-8').read().upper().strip().split('\n')
    return lines
