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
        # Regex to search for Item 7 as first appearance - probably table of contents
        item7_toc = re.search(
            r'Item?\n*?\s*?(6)?7?\s*?\.?\s*?:?\s*?-*?\n*?\s*?management?\s*?(\')?\s*(s)?\s*(discussion)',
            text, re.I)
        if item7_toc:
            # Set start for the search of the heading after the table of content appearance
            item7_toc_start = item7_toc.span()[1] + 1
            # Search for the second appearance after toc
            item7 = re.search(
                r"Item?\n*?\s*?(6)?7?\s*?\.?\s*?:?\s*?-*?\n*?\s*?management?\s*?(')?\s*(s)?\s*(discussion)",
                text[item7_toc_start:], re.I)
            # When both are found that set start of MDA and look for Item 8
            if item7_toc and item7:
                item7_chap = item7_toc_start + item7.span()[0]  # position in text von file.read()
                mda_begin = item7_toc.span()[1] + 1 + item7.span()[0]
                item8 = re.search(r"Item?\n*?\s*?(7)?8?\s*?\.?\s*?:?\s*?-*?\n*?\s*?(index)?\s*?(to)?\s*?"
                                  r"(consolidated)?\s*?financial\s*?statements",
                                  text[item7_chap:], re.I)
                # When Item 8 is found we can set the end of MDA section and print the MDA document
                if item8:
                    mda_end = mda_begin + item8.span()[0]
                    mda = text[mda_begin:mda_end]
                else:
                    print("Item 8 not found in " + filename)
            # This will take action when no second appearance of item 7 is found, so first appearance will be the start
            else:
                mda_begin = item7_toc.span()[0]
                item8 = re.search(r"Item?\n*?\s*?(7)?8?\s*?\.?\s*?:?\s*?-*?\n*?\s*?(index)?\s*?(to)?\s*?"
                                  r"(consolidated)?\s*?financial\s*?statements",
                                  text[mda_begin:], re.I)
                if item8:
                    mda_end = mda_begin + item8.span()[0]
                    mda = text[mda_begin:mda_end]
                else:
                    print("Item 8 not found in " + filename)
        else:
            print("Item 7 not found in " + filename)
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
directory = "C:/Users/bmeyer01/10K/10K"
foldernames = [x[0] for x in os.walk(directory)]
for name in foldernames:
    print("=" * 50)
    print(name)
    print("=" * 50)
    process_folder(name)
