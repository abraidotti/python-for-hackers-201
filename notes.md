
## install and use venv in windows

python -m venv .
source ./Scripts/activate


## when you want to scour the repo and remove some files/dirs
git filter-branch --tree-filter 'rm -rf Lib Scripts' --prune-empty --env-filter 'GIT_COMMITTER_DATE=$GIT_AUTHOR_DATE; export GIT_COMMITTER_DATE'
