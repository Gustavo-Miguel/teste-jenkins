import os
import git 
import requests

git_url = "https://github.com/Gustavo-Miguel/teste.git"
pull_url = "https://api.github.com/repos/Gustavo-Miguel/teste/pulls/4"
repo_dir = "teste"

def get_description():
    pullObject = requests.get(pull_url)
    description = pullObject.json().get('body')
    return description

if os.path.exists(repo_dir):
    cloned_repo = git.Repo.init(repo_dir)  
    cloned_repo.index.reset('--hard')
    print("Directory already exist!")
else:
    cloned_repo = git.Repo.clone_from(git_url, repo_dir)
    print("Directory don't exist!")

desc = get_description()

f = open("teste//CHANGELOG.md", "a")
f.write("\n\n")
f.write(desc)
f.write("\n\n")
f.close()

cloned_repo.index.add("*")
cloned_repo.index.commit("Changelog commit")
origin = cloned_repo.remote(name='origin')
origin.push()

print("END")
