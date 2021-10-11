# Election-Analysis: Creating an automated process to analyze election results in Python.

## Project Overview
The Colorado Board of Elections is interested in automating the vote count process. The objective is to write a script that provides the following:
- The number of votes cast
- The number of and percentage of votes cast in each county
- The county that cast the most votes
- Number of votes received by each candidate and the percentage of the total vote earned
- The winner of the election based on popular vote

## Results
   - Total Votes: 369,711
- Volume of votes by county:
   - Jefferson: 38,855 votes (10.5%)
   - Denver: 306,055 votes (82.8%)
   - Arapahoe: 24,801 votes (6.7%)
- Denver had the largest vote volume at the county level.
- Candidate Results:
   - Charles Casper Stockham: 85,213 votes (23.0%)
   - Diana DeGette: 272,892 votes (73.8%)
   - Raymon Anthony Doane: 11,606 votes (3.1%)
- Election Winner:
   - Diana DeGette: 272,892 votes (73.8%)

![Election_Results](https://user-images.githubusercontent.com/88675415/136824388-3bac5577-db01-406a-909a-58238394a7e3.PNG)

**Figure 1:** 

## Summary
This script is ready for most county elections. It is highly adaptable. It may have difficulty adjusting to a different jurisdiction, for example the city level. Often there is voting on specific referendums and this script would have to be modified to accommodate that. This may be achieved by using the column headers to label the outputs in the code. This code only gives output based on what populates the second and third columns of the data set. The code may need to be modified to loop through all columns of the data to have success in creating greater variability in the output statistics.
