 # Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
 
 #path to file 
 #Resources/election_results.csv
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

 # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
 # Print each row in the CSV file.
    for row in file_reader:
        print(row)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
  
 # Write three counties to the file.
    txt_file.write("Arapahoe, Denver, Jefferson")
     # Read the file object with the reader function.
    

# Close the file
election_data.close() 
txt_file.close()