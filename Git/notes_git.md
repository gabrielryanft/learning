# Git notes - Notes i make while i learn git ( FreeCodeCamp video with @HiteshCodeLab )

## repo (short for repository)

a directory

## git status

show if the current repository is a git repository.

## git init

make the current dir a git repo

## Commit (checkpoint)

### git add

adds the file(s)/dir(s) to a "commit bag" (this is not commited yet)

If you have two files, x and y, and you want to track only x, do:

`$ git add x ( not the whole dir with . (dot) )`

### git commit

commit what you've put inside the "commit bag"

always with the -m flag, to commit with a message:

`$ git commit -m "add file x"`

### git push

send to cloud, github, gitlab *et citera*

## git log

log the details about commits

## .gitignore

a file that tells git what not to include in the repo.

## creating branch (ramification)

`$ git branch name_of_branch`

### swich branches

`$ git checkout name_of_branch`

goes to branch name_of_branch

running `git branch`, the pointer will point to name_of_branc, not to master.

What you commit im a branch will stay in that branch (if you dont merge with other branch)

If the branch does not exist, use `git checkout -b name_of_new_branch` or `git switch -c name_of_new_branch` and it will create a branch and move you there.

### merging branches

merge current branch with other:
`$ git merge other_branch` 

#### merge conflicts

if the same file is diferent in the merged branches(conflicts can occur in and out of the master branch.), it gives a "error":
HEAD = current branch (can be seen in .git/HEAD, i.e. show the name of current branch.)

```
<<<<<<< HEAD 
<tbody>			\
	<tr>1</tr>   |      
	<tr>2</tr>    \  file in the 
	<tr>3</tr>    /   current branch   
	<tr>4</tr>   |      
</tbody>		/ 
=======         
<ul>				\
	<li>this</li>    |
	<li>p</li>        > file in the
	<li>p</li>       |   other branch
	<li>p</li>      /   
</ul>         
>>>>>>> other_branch
```

### delete branch 

`git branch -d branch_name` (-d stands for delete.)

## git diff

### diffing branches: 

to see the diference between branches, do `git diff branchname` it comparess the currrent branch with the other one.


or `git diff branc1 branch2` to compare 2 branches (not necessarily the one you are in and an other one)

\* if you are in an old version of git use:

`git diff branc1..branch2`

Ex. output: ( inside parentheses are my observations )
```
diff --git a/index.html b/index.html
index 37fb774..ffdaed4 100644
--- a/index.html ( -/a = the doc in the other branch )
+++ b/index.html ( +/b = the doc in the current branch )
@@ -1,4 +1,5 @@
 <!DOCTYPE html>
+<!-- this is a comment-->
 <html lang="en">
 <head>
        <meta charset="UTF-8">
@@ -6,12 +7,11 @@
        <title>this was made in the "wrong" branch</title>
 </head>
 <body>
-       <p>not right</p>
-       <ul>
-               <li>this</li>
-               <li>p</li>
-               <li>p</li>
-               <li>p</li>
-       </ul>
+               <tbody>
+                       <tr>1</tr>
+                       <tr>2</tr>
+                       <tr>3</tr>
+                       <tr>4</tr>
+               </tbody>
 </body>
 </html>
```

### diffing staged and not staged files (past and present of current branch)

`git diff --staged`

Ex. output: ( inside parentheses are my observations )
```
diff --git a/index.html b/index.html
index dcd00ea..ffdaed4 100644
--- a/index.html ( -/a = the past doc )
+++ b/index.html ( +/b = the current doc )
@@ -1,4 +1,5 @@
 <!DOCTYPE html>
+<!-- this is a comment--> ( + (in the beggining of the line) = the current doc )
 <html lang="en">
 <head>
        <meta charset="UTF-8">
@@ -6,7 +7,6 @@
        <title>this was made in the "wrong" branch</title>
 </head>
 <body>
-       <p>not right</p> ( - (in the beggining of the line) = the past doc
                <tbody>
                        <tr>1</tr>
                        <tr>2</tr>
```

### diff commits

`git diff commit_id1 commit_id2`

Ex.:
´$ git log --oneline`
output:
```
cf46bbb (HEAD -> master) change index	(compare this one with...)
2e57c4a Merge branch 'change'
01575e4 updated index
652a907 change index.html
9b7ef17 fackd ap index					(... this one)
3325d73 change index
a93ab77 Merge branch 'change'
ab9b4e3 updete inde.html
7d57126 change index.html
5f334ed Merge branch 'not_master'
2b6c31f add this.md
ce6ac7f add index
1b5dd68 change branch not_master. edit index (nc) create not_master
c85694e update .gitignore
7aeb373 add file new_thing.txt
3aa6734 first commit
```
`git diff cf46bbb 9b7ef17` 

\* if you are in a old version of git, use:

`git diff cf46bbb..9b7ef17`

output:
```
diff --git a/index.html b/index.html
index 37fb774..7e28d11 100644
--- a/index.html
+++ b/index.html
@@ -7,11 +7,7 @@
 </head>
 <body>
        <p>not right</p>
-       <ul>
-               <li>this</li>
-               <li>p</li>
-               <li>p</li>
-               <li>p</li>
-       </ul>
+               popopopopopo
+       <p>made in the chande branch</p>
 </body>
 </html>
```

## git stash

### archiving changes

"archive" the uncommited changes so you can do something. (without losing your changes.)

when you stash your changes, they are taken out from the files.

`git stash`

\* this command stashes the changes in the current branch.

### list stashes

before stashing anything, run `git stash list`, to see if some thing is already stashed in the current branch

### unstashing / popping

stashed changes can be pop(d? i don't know how to write), unstashed, with:

`git stash pop`

\* stashes change branch with you, so, pay atention with what you are pop(ing?). unstashing in the wrong place can cause the same "problem" as a merge conflict.

### apply specific stash

`git stash apply stash@{n}`

## make experiments on past commits without affecting the current state of branch

`git checkout commit_id`

this creates a new banch separated from the parent branch.

to keep something you do in the "test branch" make a branch from inside the copy one.

or use head and the number of commits you want to go back.

`git checkout HEAD~2`

Ex.:
`git log --oneline`

output: 

```
2c77f9b (HEAD -> change) change index
5e557f1 Merge branch 'master' into change
cf46bbb change index
1be733a change index
2e57c4a Merge branch 'change'
01575e4 updated index
652a907 change index.html
9b7ef17 fackd ap index
```

with the command `git checkout HEAD~1` you get:

2c77f9b (HEAD -> change) change index		from here,
5e557f1 Merge branch 'master' into change	to here

but with the command `git checkout HEAD~2` you get:

2c77f9b (HEAD -> change) change index		from here, 
5e557f1 Merge branch 'master' into change
cf46bbb change index
1be733a change index						to here

but with the command `git checkout HEAD~3` you get:

2c77f9b (HEAD -> change) change index		from here,
5e557f1 Merge branch 'master' into change
cf46bbb change index
1be733a change index
2e57c4a Merge branch 'change'				to here.

## git reflog

see witch branches you were before (jump history.).

## git rebase

files in branches: 

branch master:
	index: "this is a file"

branch bran2: 
	index: "this is another file"

branches:

```
o | -> some other commit in master
| 0 -> commit in bran2
|/
o ->initial cmt (branch = master)
```

to rebase the current branch with an other one branch: 

do not rebase the master first. start with the other one.

in the bran2:

`git rebase master`

branches:

```
| 0 -> commit in bran2	\
|/			 | the bran2 synchronized with the head of the master branch.
o -> some other commit  /
|    in master 
|
o ->initial cmt (branch = master)
```

now, in the master branch, 

`git rebase bran2`

```
0 -> commit in bran2	\
|			 | the bran2 and master are now, one.
o -> some other commit  /
|    in master 
|
o ->initial cmt (branch = master)
```







