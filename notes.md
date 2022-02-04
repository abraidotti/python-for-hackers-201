
## install and use venv in windows

```bash
python -m venv .
source ./Scripts/activate
```

## when you want to scour the repo and remove some files/dirs

```bash
git filter-branch --tree-filter 'rm -rf Lib Scripts' --prune-empty --env-filter 'GIT_COMMITTER_DATE=$GIT_AUTHOR_DATE; export GIT_COMMITTER_DATE'
```

# change dashes to underscores in file names:

```bash
for file in *; do mv "$file" `echo $file | tr ' ' '_'` ; done
```



apt install mingw-w64
