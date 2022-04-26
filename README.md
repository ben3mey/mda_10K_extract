# Extraction of MD&A section
This repository is developed to promote MD&A (Management's Discussion and Analysis) extraction from 10-K and 10-K/A filings. <br>
This is a dirty version based on regex to cut out the section from *Item 7: Management’s Discussion and Analysis* until *Item 8: Financial Statements*. <br>
Including the 10-K/A documents, the current algorithm has an accuracy between 50% and 60%.<br>
As most 10-K/A documents are only short amendments without the above-mentioned sections, this is fine for now.<br>
Please use mda_extract.py to create a subfolder *mda* in the year-folder of your 10-K and 10-K/A files.<br>
The 10-Ks you must download by yourself.

## Set up
Store all your 10-K files in subfolders for the years of the report accordingly.<br>
These subfolders should be in one folder called e.g., *10K*.<br>
Download mda_extract.py and paste it into the folder *10K*.<br>

## Run program
Use shell/terminal and set your working directory:<br>
`cd C:/Username/10K`<br>
Run the downloaded python program through shell/terminal:<br>
`python mda_extract.py`

## Result
After finishing the program should have created the subfolders *mda* in the year-folders of the 10-K documents.<br>

## Branches
1. Main branch. First attempt, which is based on checking the lines in 10K document. Around 50% accurate. 
2. Version2 branch. Second attemt, which is based on checking the text file itself and not each line individually. More accurate. Around 75%, since regex is now able to match over several rows. Helpful when item 7 header is not only in one line.

## Inquiries
Please feel free to check my code for your application needs.<br>
I will check issues and pull requests periodically.
