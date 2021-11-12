import os
from git import Repo

local_repo_directory = ""
destination = 'main'

def clone_repo():
    if os.path.exists(local_repo_directory):
        print("Directory exists, pulling changes from main branch")
        repo = Repo(local_repo_directory)
        origin = repo.remotes.origin
        origin.pull(destination)
    else:
        print("Directory does not exists, cloning")
        Repo.clone_from("https://github.com/Gustavo-Miguel/teste-jenkins.git",
                        local_repo_directory, branch=destination)

def chdirectory(path):
    os.chdir(path)

def create_branch(repo, branch_name):
    print("Creating a new branch with id name " + branch_name)
    current = repo.create_head(branch_name)
    current.checkout()

def update_file():
    print("Modifying the file")
    archive = "CHANGELOG.md"
    opened_file = open(archive, "a")
    opened_file.write("\n\n")
    opened_file.write("TESTETESTETESTESTESTE")
    opened_file.write("\n\n")
    opened_file.close()


def add_and_commit_changes(repo):
    print("Commiting changes")
    repo.index.add("*")
    repo.index.commit("Adding a new line to the file.text file")


def push_changes(repo):
    print("Push changes")
    repo.git.push("--set-upstream", 'origin', destination)
    origin = repo.remotes.origin
    origin.push(destination)


#clone the repository
#clone_repo()

repo = Repo.init()
branch_name = destination

#create a new branch
create_branch(repo, branch_name)

# update file
update_file()

# add and commit changes
add_and_commit_changes(repo)

# push changes
push_changes(repo)
