# Goal is to extract MD&A section from 10-K documents
# Author: Benedict Meyer
# Date: 22/04/07

import glob
import os
import re

# Define function to process 10k documents
def process_file(filename):
    mda = []
    with open(filename, "r") as file:
        lines = file.readlines()
    mda_started = False
    end_of_file = False
    i = 0
    num_lines = len(lines)
    while not mda_started:
        line = lines[i]
        if re.match(r"(Item)?\n*?\s*?7\.?:?-?\n*?\s*?management", line.lower(), re.I):
            mda_started = True
            i-=1
        i+=1
        if i >= num_lines:
            end_of_file = True
            break

    if not end_of_file:
        mda_ended = False
        while not mda_ended:
            line = lines[i]
            mda.append(line)
            if re.match(r"(Item)?\n*?\s*?8\.?:?-?\n*?\s*?financial", line.lower(), re.I):
                mda_ended = True
            i+=1
            if i >= num_lines:
                break
    return mda

# Define function to write new mda files
def process_folder(foldername):
    create_folder(foldername)
    filenames = glob.glob(foldername + "/*.txt")
    num_files = len(filenames)
    for i, filename in enumerate(filenames):
        print("processing file {}/{}".format(i, num_files))
        mda_lines = process_file(filename)
        if not mda_lines:
            continue
        else:
            new_filename = filename.replace(foldername, foldername + "/mda/")
            new_filename = new_filename.replace(".txt", "_mda.txt")

            with open(new_filename, "w") as file:
                for line in mda_lines:
                    file.write("%s\n" % line)

# Define function to create new subfolder for mda documents
def create_folder(foldername):
    script_path = os.path.realpath(foldername)
    new_abs_path = os.path.join(script_path, "mda")
    if not os.path.exists(new_abs_path):
        os.mkdir(new_abs_path)

# Execute program
directory = "C:/Username/10K" #todo change to your working directory
foldernames = [x[0] for x in os.walk(directory)]
for name in foldernames:
    print("="*50)
    print(name)
    print("=" * 50)
    process_folder(name)
