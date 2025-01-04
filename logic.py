## GUI colors
background_color = "#F9E6CF"
text_color = "#69247C"




## adding candidates to file
def add_candidate(candidate_name):
    with open("files/candidates.txt", "r") as file:
        for line in file:
            if line.strip() == candidate_name:
                print("Candidate already exists")
                return

    print("Adding candidate...")
    with open("files/candidates.txt", "a") as file:
        file.write(candidate_name + "\n")
        


# returns a list of candidates
def get_candidate():
     candidates = []
     with open("files/candidates.txt", "r") as file:
        for line in file:
            candidates.append(line.strip())
     return candidates
        

# deletes the given candidate, if candidate doesnt exist 
def delete_candidate(candidate_name):
    with open("files/candidates.txt", "r") as f:
        lines = f.readlines()
    with open("files/candidates.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != candidate_name:
                f.write(line)
    print("Candidate deleted")



# checks if the user already voted or not
def already_voted(user_id):
    with open("votes.txt", "r") as file:
        for line in file:
            line_list = line.split(":")
            line_list = [item.strip() for item in line_list] 
            if(line_list[0] == user_id):
                return True

    return False

def count_votes():
    votes = {}
    candidates = get_candidate()
    for candidate in candidates:
        votes[candidate] = 0
    with open("votes.txt") as file:
        for line in file:
            line_list = line.split(":")
            line_list = [item.strip() for item in line_list]  
            if line_list[1] in candidates:
                 votes[line_list[1]] += 1
    # print(votes)
    return votes

    