from typing import Iterable, Any
import csv
from os.path import exists


class LoadCSV:

    def __init__(self, path) -> None:
        self.path = path


    def is_exist(self):
        if exists(self.path):
            return True
        else:
            return False


    def lines(self):
        with open(self.path, 'r', newline='') as f:
            for line in csv.reader(f):
                yield line


    def write(self, lines: Iterable[Iterable[Any]], fields=None):
        """filds: None | Iterable[Any]"""
        #
        with open(self.path, "w")as file:
            csvwriter = csv.writer(file, lineterminator="\n")
            if fields:
                csvwriter.writerow(fields)
            csvwriter.writerows(lines)


    def append(self, lines: Iterable[Iterable[Any]]):
        #
        with open(self.path, "a")as file:
            csvwriter = csv.writer(file, lineterminator="\n")
            csvwriter.writerows(lines) 


    def create(self):
        with open(self.path, "x")as file:
            file.close()


