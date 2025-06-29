# check_update.py
import git
import os

REPO_DIR = "/tmp/ci-cd-repo"
REPO_URL = "https://github.com/prafulkharat23/git_assignment_HeroVired.git"
BRANCH = "main"
HASH_FILE = ".commit_hash"

def clone_or_pull_repo():
    if not os.path.exists(REPO_DIR):
        print("Cloning repository...")
        repo = git.Repo.clone_from(REPO_URL, REPO_DIR, branch=BRANCH)
    else:
        print("Pulling latest changes...")
        repo = git.Repo(REPO_DIR)
        origin = repo.remotes.origin
        origin.pull()
    return repo

def get_latest_commit_sha(repo):
    return repo.head.commit.hexsha

def read_last_commit():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, 'r') as f:
            return f.read().strip()
    return ""

def write_last_commit(sha):
    with open(HASH_FILE, 'w') as f:
        f.write(sha)

def main():
    repo = clone_or_pull_repo()
    latest_sha = get_latest_commit_sha(repo)
    last_sha = read_last_commit()

    if latest_sha != last_sha:
        print("New commit detected. Deploying...")
        os.system("bash deploy.sh")
        write_last_commit(latest_sha)
    else:
        print("No new commit. Nothing to deploy.")

if __name__ == "__main__":
    main()
