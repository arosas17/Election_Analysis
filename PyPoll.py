# #The data we need to retrieve

# # Import the datetime class from the datetime module.

# import datetime as dt
# # Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# # Print the present time.
# print("The time right now is ", now)


# #1. The total number of votes cast
# #2. A complete list of candidates
# #3. The percentage of votes each candidate won
# #4 The total number of votes each candidate won
# #5. The winer of the election based on popular votesss

# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'



# # Open the election results and read the file
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)


import csv
import os

#Assign a variable for the file to load and the path

file_to_load = os.path.join('Resources', 'election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# open election results and read file

with open(file_to_load) as election_data:

     #read the fie obj with the reader function
     file_reader = csv.reader(election_data)

     # #print each row in the CSV file
     # for row in file_reader:
     #      print(row)

     #print the header row
     headers = next(file_reader)
     print(headers)

  # Print each row in the CSV file.


# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, 'w')

# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")

# # Write three countries to the file
# outfile.write("Countries in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")


# # Close the file

# outfile.close()