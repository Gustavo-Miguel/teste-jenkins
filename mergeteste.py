import os
import git 
import requests

git_url = "https://github.com/Gustavo-Miguel/teste.git"
pull_url = "https://api.github.com/repos/Gustavo-Miguel/teste/pulls/4"
repo_dir = "teste"

if os.path.exists(repo_dir):
    cloned_repo = git.Repo.init(repo_dir)
    #os.remove(repo_dir)
    print("Directory already exist!")
else:
    cloned_repo = git.Repo.clone_from(git_url, repo_dir)
    print("Directory don't exist!")

desc = get_description()
print(desc)
