# Extraction of MD&A section
This repository is developed to promote MD&A (Management's Discussion and Analysis) extraction from 10-K and 10-K/A filings. <br>
This is now the fifth version based on regex to cut out the section from *Item 7: Management’s Discussion and Analysis* until *Item 8: Financial Statements*. <br>
Including the 10-K/A documents, the current algorithm has an accuracy of over 90%.<br>
As most 10-K/A documents are only short amendments without the above-mentioned sections, this is acceptable.<br>
You can use mda_extract.py to create a subfolder *mda* in the year-folder of your 10-K and 10-K/A files.<br>
The 10-Ks you must download by yourself.<br>
You can find some aggregated files here: https://sraf.nd.edu/sec-edgar-data/ 

## Set up
Store all your 10-K files in subfolders for the years of the report accordingly.<br>
These subfolders should be in one folder called e.g., *10K*.<br>
It should look somehow like this:
1. 10K
  1.2. 2000
    a. *file 1*
    b. *file 2*
    c. ...
  1.3. 2001
  1.4. 2002
  1.5. ...
Download mda_extract.py and paste it into the folder *10K*.<br>

## Run program
Use shell/terminal and set your working directory:<br>
`cd C:/Username/10K`<br>
Run the downloaded python program through shell/terminal:<br>
`python mda_extract.py`
Of course, you can use PyCharm or any other IDE as well.

## Result
After finishing the program should have created the subfolders *mda* in the year-folders of the 10-K documents.<br>

## Inquiries
Please feel free to check my code for your application needs.<br>
I will check issues and pull requests periodically. <br>
Hit me up for recommendations, improvements, and questions! :) 
