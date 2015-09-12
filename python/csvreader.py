__author__ = 'Sean'

import itertools
import csv


with open('citations.csv', 'rb') as data:
    with open('dbsetup.txt', "w") as output:
        fields = csv.reader(data, dialect='excel').next()

        for i in range(len(fields)):
            output.write(" " + fields[i] + " + ")