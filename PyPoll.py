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

#dependencies added

import csv
import os

#Assign a variable for the file to load and the path

file_to_load = os.path.join('Resources', 'election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# intialize the vote counter and created candidate list
total_votes = 0
candidate_options = []
# open election results and read file

# inserting candidate dictionary
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 


with open(file_to_load) as election_data:

     #read the fie obj with the reader function
     file_reader = csv.reader(election_data)

     #print the header row
     headers = next(file_reader)

     #print each row in the CSV file, searching rows for candidate names
     for row in file_reader:
          total_votes += 1


          candidate_name = row[2]

          #adding candidates to list( excluding repeats)
          if candidate_name not in candidate_options:

               candidate_options.append(candidate_name)

               #initaling votes per candidate 
               candidate_votes[candidate_name] = 0
          #adding vote counter
          candidate_votes[candidate_name] += 1         

#percentage calculation
#1 interate though candidate list
for candidate_name in candidate_votes:

     #retrieve vote count of candidate
     votes = candidate_votes[candidate_name]

     #calculate % of votes
     vote_percentage = float(votes) / float(total_votes) * 100


     #determine the winning candidate
     #which vote is higher is inserted

     if (votes > winning_count) and (vote_percentage > winning_percentage):

          winning_count = votes

          winning_percentage = vote_percentage

          winning_candidate = candidate_name

     #creating winner statement
     print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
     
     winning_candidate_summary = (f'-------------------------\n'
     f'Winner: {winning_candidate}\n'
     f'Winning Vote Count: {winning_count:,}\n'
     f'Winning Percentage: {winning_percentage:.1f}%\n'
     f'-------------------------\n')

#printing winner
print(winning_candidate_summary)

#print the votes
print(total_votes)










# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, 'w')

# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")

# # Write three countries to the file
# outfile.write("Countries in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")


# # Close the file

# outfile.close()