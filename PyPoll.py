#dependencies added

import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")


# intialize the vote counter and created candidate list and votes
total_votes = 0
candidate_options = []
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

#Open election results and read the file
with open(file_to_load) as election_data:

     #read the fie obj with the reader function
     file_reader = csv.reader(election_data)

     #print the header row
     headers = next(file_reader)

     #print each row in the CSV file, searching rows for candidate names
     for row in file_reader:
          total_votes += 1

          #get candidate name from each row
          candidate_name = row[2]

          #adding candidates to list( excluding repeats)
          if candidate_name not in candidate_options:

               candidate_options.append(candidate_name)

               #initaling votes per candidate 
               candidate_votes[candidate_name] = 0
          #adding vote counter
          candidate_votes[candidate_name] += 1

     #Save results to text file
with open(file_to_save, "w") as txt_file:

     #Print the final count to the terminal
     election_results = (
          f'\nElection Results\n'
          f'-------------------------\n'
          f'Total votes: {total_votes:,}\n'
          f'-------------------------\n')
     print(election_results, end='')

     

     #save the final vote count to the text file
     txt_file.write(election_results)         

     #percentage calculation
     #1 interate though candidate list
     for candidate_name in candidate_votes:

          #retrieve vote count of candidate
          votes = candidate_votes[candidate_name]

          #calculate % of votes
          vote_percentage = float(votes) / float(total_votes) * 100


          #determine the winning candidate
          #which vote is higher is inserted
          candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

          # Print each candidate, their voter count, and percentage to the terminal.
          print(candidate_results)
          #save the candidates to our text file
          txt_file.write(candidate_results)

          if (votes > winning_count) and (vote_percentage > winning_percentage):

               winning_count = votes

               winning_percentage = vote_percentage

               winning_candidate = candidate_name

     #creating winner statement          
     winning_candidate_summary = (
          f'-------------------------\n'
          f'Winner: {winning_candidate}\n'
          f'Winning Vote Count: {winning_count:,}\n'
          f'Winning Percentage: {winning_percentage:.1f}%\n'
          f'-------------------------\n')

     #printing winner
     print(winning_candidate_summary)

     # Save the winning candidate's name to the text file.
     txt_file.write(winning_candidate_summary)
