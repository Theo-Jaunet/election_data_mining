import argparse
import csv

from Commune import *
from Candidat import *
from Line import *


# TODO : Progress bar ?
# TODO : No absolute path
# TODO : No 11 Cands hypothesis ?
# TODO : remove hardcoded nb of rows : 390919


def main():
    data = []

    with open(FLAGS.file, "r") as file:  # file with data
        with open('Result.json', 'w') as f:  # file with results
            f.write("{rows: [")

            spamreader = csv.reader(file, delimiter=';', quotechar='|')  # set reader parameters ( iterator)
            i = 0
            index = 0

            next(spamreader)  # skip Header

            for row in spamreader:  # loop on rows
                id = next((i for i, item in enumerate(data) if
                           item.Commune.hash == hash(row[2] + "|" + row[7] + "|" + row[9])),
                          -1)  # find if Commune was previously made and get ID if so (return - otherwise)
                if id == -1: # if Row not found
                    data.append(Line(index, Commune(row[2], row[7], row[9]), []))
                    id = len(data) - 1 #set new ID & insert new row
                    index += 1
                #test if Candidat name is already in list of Cands in given row, add him otherwise
                if not next((x for x in data[id].Candidats if x.name == row[10]), None):
                    data[id].Candidats.append(Candidat(row[10], row[14]))
                    data[id].nbCand += 1
                i += 1

                # Optimisation -> write directly the Commune if it contains all cands
                if data[id].nbCand == 11:
                    f.write(str(data[id]))
                    f.write(",")
                    data.pop(id)

                print("Progress :", round((i/390919)*100),"%")

            # Remove Last Char of the result file
            f.seek(0, 2)
            size = f.tell()
            f.truncate(size - 1)
            #close the JSON
            f.write("]}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, default="/home/theo/data/election-presidentielle-2017.csv",
                        help='Set input file location')


    FLAGS, unparsed = parser.parse_known_args()
    main()
