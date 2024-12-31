
## adding candidates via IO
## haykoon feh label w a button 3ashan a-invoke this function
## hakhod el kalam el fl label w a-pass it as a parameter
def add_candidate(candidate_name):
## first thing ill do is to check whether that candidate name alr exisits or not
    with open("files/candidates.txt", "r") as file:
        for line in file:
            if line.strip() == candidate_name:
                print("Candidate already exists")
                return

    ## if the candidate doesnt exist, i will add him to the file
    print("Adding candidate")
    with open("files/candidates.txt", "a") as file:
        file.write(candidate_name + "\n")


# returns candidates from file
def get_candidate():
     candidates = []
     with open("files/candidates.txt", "r") as file:
        for line in file:
            candidates.append(line.strip())
        

def delete_candidate(candidate_name):
    with open("files/candidates.txt", "r") as f:
        lines = f.readlines()
    with open("files/candidates.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != candidate_name:
                f.write(line)


## https://stackoverflow.com/questions/4710067/how-to-delete-a-specific-line-in-a-text-file-using-python 