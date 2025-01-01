
## adding candidates via IO [serverGUI]
def add_candidate(candidate_name):
    with open("files/candidates.txt", "r") as file:
        for line in file:
            if line.strip() == candidate_name:
                print("Candidate already exists")
                return

    ## if the candidate doesnt exist, i will add him to the file
    print("Adding candidate")
    with open("files/candidates.txt", "a") as file:
        file.write(candidate_name + "\n")
        


# returns candidates from file [server+client GUI]
def get_candidate():
     candidates = []
     with open("files/candidates.txt", "r") as file:
        for line in file:
            candidates.append(line.strip())
     return candidates
        

# deletes the given candidate, if candidate doesnt exist [server GUI]
def delete_candidate(candidate_name):
    with open("files/candidates.txt", "r") as f:
        lines = f.readlines()
    with open("files/candidates.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != candidate_name:
                f.write(line)
    print("Candidate deleted")



# checks if the user already voted or not [server code]
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
    with open("votes.txt") as file:
        for line in file:
            line_list = line.split(":")
            line_list = [item.strip() for item in line_list]  
            if line_list[1] in candidates:
                 if line_list[1] not in votes:
                    votes[line_list[1]] = 0
                 votes[line_list[1]] += 1
    print(votes)
    return votes

    


count_votes()

## https://stackoverflow.com/questions/4710067/how-to-delete-a-specific-line-in-a-text-file-using-python 