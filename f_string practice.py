my_votes = float(input("How many votes did you get in the election? "))
total_votes = float(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("1","I received " + str(percentage_votes)+"% of the total votes.")


my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print("2.",f"I received {my_votes / total_votes * 100}% of the total votes.")


candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print("last :",message_to_candidate)


