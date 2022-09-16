import hopsworks

project = hopsworks.login()

git_api = project.get_git_api()

REPO_URL="https://github.com/robzor92/Hopsworks-CI-CD.git" # git repository
HOPSWORKS_FOLDER="Resources" # path in hopsworks filesystem to clone to
PROVIDER="GitHub"
BRANCH="master" # optional branch to clone

examples_repo = git_api.clone(REPO_URL, HOPSWORKS_FOLDER, PROVIDER, branch=BRANCH)
