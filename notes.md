# Python 201 for Hackers

https://academy.tcm-sec.com/courses/python-201-for-hackers/lectures/36465555
https://www.udemy.com/course/python-201-for-hackers/

## install and use venv in windows

```bash
python -m venv .
source ./Scripts/activate
```


## apps used:

https://processhacker.sourceforge.io/

https://dependencywalker.com/


## misc git and linux stuff

### when you want to scour the repo and remove some files/dirs

```bash
git filter-branch --tree-filter 'rm -rf Lib Scripts' --prune-empty --env-filter 'GIT_COMMITTER_DATE=$GIT_AUTHOR_DATE; export GIT_COMMITTER_DATE'
```

### change dashes to underscores in file names:

```bash
for file in *; do mv "$file" `echo $file | tr ' ' '_'` ; done
```
