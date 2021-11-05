import os
import git 
import requests

git_url = "https://github.com/Gustavo-Miguel/teste.git"
pull_url = "https://api.github.com/repos/Gustavo-Miguel/teste/pulls/4"
repo_dir = "teste"

cloned_repo = git.Repo.clone_from(git_url, repo_dir)
print("Cloned Repo!")
