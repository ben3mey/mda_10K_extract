# Goal is to extract MD&A section from 10-K documents
# Author: Benedict Meyer
# Date: 22/04/22

import glob
import os
import re


# Define function to process 10k documents
def process_file(filename):
    mda = []
    with open(filename, "r") as file:
        text = file.read()
        text = text[6000:]  # start after table of contents
        item7 = re.search(r"Item?\n*?\s*?(6)?7?\s*?\.?\s*?:?\s*?-*?\n*?\s*?management?\s*?'?(s)?\s*(discussion)",
                          text, re.I)
        if item7:
            mda_begin = item7.span()[0]
            item8 = re.search \
                (r"Item?\n*?\s*?(7)?8?\s*?\.?\s*?:?\s*?-*?\n*?\s*?(index)?\s*?(to)?\s*?(consolidated)?\s*?financial\s"
                 r"*?statements",
                 text, re.I)
            if item8:
                mda_end = item8.span()[0]
            else:
                print("Item 8 not found in " + filename)
                item9 = re.search(r"Item?\n*?\s*?(8)?9?\s*?\.?\s*?:?\s*?-*?\n*?\s*?changes?\s*?in\s*?and",
                                  text, re.I)
                if item9:
                    mda_end = item9.span()[0]
                else:
                    print("Item 9 not found either in " + filename)
        else:
            print("Item 7 not found in " + filename)
        if item7 and item8:
            mda = text[mda_begin:mda_end]
    return mda


# Define function to write new mda files
def process_folder(foldername):
    create_folder(foldername)
    filenames = glob.glob(foldername + "/*.txt")
    num_files = len(filenames)
    for i, filename in enumerate(filenames):
        print("processing file {}/{}".format(i, num_files))
        mda = process_file(filename)
        if not mda:
            continue
        else:
            new_filename = filename.replace(foldername, foldername + "/mda/")
            new_filename = new_filename.replace(".txt", "_mda.txt")

            with open(new_filename, "w") as file:
                file.write(mda)


# Define function to create new subfolder for mda documents
def create_folder(foldername):
    script_path = os.path.realpath(foldername)
    new_abs_path = os.path.join(script_path, "mda")
    if not os.path.exists(new_abs_path):
        os.mkdir(new_abs_path)


# Execute program
directory = "C:/Users/username/yourfolder" #todo Update to your directory necessary
foldernames = [x[0] for x in os.walk(directory)]
for name in foldernames:
    print("=" * 50)
    print(name)
    print("=" * 50)
    process_folder(name)
