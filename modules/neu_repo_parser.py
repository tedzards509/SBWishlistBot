import json
import os
from git import Repo


repo_path = "./NEU_Repo/"
repo_link = "https://github.com/NotEnoughUpdates/NotEnoughUpdates-REPO"


def sync_repo():
    if os.path.exists(repo_path):
        repo = Repo.clone_from(repo_link, repo_path)
        assert repo.__class__ is Repo
    return


def update_repo():
    return


def check_up_to_date():
    up_to_date = True
    return up_to_date


def parse_json(path: str):
    return


def parse_repo():
    sync_repo()
