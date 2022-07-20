# Election_Analysis

## Overview of Election Audit

A task was given by a Calarado Board of Elections employee in order to create a python program that may tally election result of a local congresstional election.

The orginal design of this file was meant to obtain:

  * The total votes cast
  * The list of candidates
  * The total votes per candidate
  * The percentage of votes per candidate
  * The winner of the election

However, in addition to the orginal design, the election commission requestion more information:
  
  * The voter turnout per county
  * The percentage of voters per county
  * The county with the highest voter turnout
  
To perform these tasks, Python version 3.7 (64 bit) and Visual Studio Code version 1.69.1 were used; we were also given the list of the election results to work with (located in resources folder).


## Election-Audit Results 

Based on the votes recieved:

* There was a total of 369,711 votes casted in this election.

* The counties' contribution in this election are:
     - Jefferson county: contributing 10.5%, totaling 38,855 of the votes.
     - Denver county: contributing 82.8%, totaling 306,055 of the votes.
     - Arapahoe county: contributing 6.7%, totaling 24,801 of the votes.

* The largest county turnout is Denver, contributing 82.8% of the votes, casting 306,055 total votes.

* The candidates are:
     - Chareles Casper Stockham
     - Diana DeGette
     - Raymon Anthony Doane

* The candidates' vote results are as follows:
     - Chareles Casper Stockham: recieved 23.0% of the votes, totaling 85,213 votes.
     - Diana DeGette: recieved 73.8% of the votes, totaling 272,892 votes.
     - Raymon Anthony Doane: recieved 3.1% of the votes, totaling 11,606 votes.

* The winner is Diana DeGette who recieved 73.8% of the votes, a vote count of 272,892.

## Summary

Though this audit is useful now, there are a few improvements that may allow it to better address other elections. One suggestion would be to take into account larger or smaller election. In order to do this, diffrent size of area would need to be taken into account such as states for a larger election and zip codes for smaller elections. In addition to this, the diffrent ballot types so that the more popular ballot types may be determined. This could be useful on deciding which ballots are popular and may be used on how to proceed with future elections.
