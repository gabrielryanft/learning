> Notes and tests I made while watching the 'Versionamento de Código com Git e GitHub' session by DIO, as part of the 'Criando Prompts Inteligentes' bootcamp. 

# undoing things with git

## git init in the wrong dir:

just remove the dir that stores the git info in that dir ( i.e. .git/ )

```bash 
$ git init  # current dir is a git dir

$ rm -rf .git/ # cirrent dir is not a git dir anymore

```

## changing last commit message

to ghange the commit message of the last commit, do:

```bash 
$ git commit --amend -m "new commit msg"
```
for editing in the terminal, or:

```bash 
$ git commit --amend
```
for changing commit msg in the editor. 

## unchanging files

```bash
$ git commit -m "create file.txt"
$ cat file.txt
~ some text
$ echo different text > file.txt
```

now, to restore to the state of file.txt in the *last commit*, we can use:
for example:
```bash
ed1970c (HEAD -> master) last commit <----- the file will be restored to the state it was in this commit.
2b3a37e 1
89fe1fc 0
```

```bash
$ git restore file.txt
```
or
```bash
$ git checkout file.txt
```
give the same result:

```bash
$ cat file.txt
~ some text
```

## reset flags

reseting the repo to some earlier commit state and still having the current files (in some cases).

### soft

```bash
git reset --soft <commit_id>
```

go back to <commit_id> and put existing files (that exist in the current commit) in the stage area.

ex:
**commit log:**
```bash
4a35ffc (HEAD -> master) add three.txt
b1803d7 add two.txt
e5b6f95 add one.txt
```
current dir have one.txt, two.txt and and three.txt

doing git reset to the first comit ("add one.txt"):
```bash
git reset --hard e5b6f95
```
only the files in the 
we can see that with git status:
```bash
$ git status
~On branch master
~Changes to be committed:
~  (use "git restore --staged <file>..." to unstage)
~        new file:   two.txt
~        new file:   three.txt
```

**\* going back, the files in the current commit will not change ( get the content of that file in the current commit.) but will still have their content from HEAD.**

### mixed

same as soft, but the files are not staged when you go back.

### hard

files that did not exist in the target commit are deleted.


```bash
git reset --hard <commit_id>
```

**commit log:**
```bash
4a35ffc (HEAD -> master) add three.txt
b1803d7 add two.txt
e5b6f95 add one.txt
```
current dir have one.txt, two.txt and and three.txt

doing git reset to the first comit ("add one.txt"):
```bash
git reset --soft e5b6f95
```

current dir have one.txt, two.txt and and three.txt
the diference is that two.txt and and three.txt are in the stage area.

we can see that with git status:
```bash
$ git status
~On branch master
~Changes to be committed:
~  (use "git restore --staged <file>..." to unstage)
~        new file:   two.txt
~        new file:   three.txt
```

### reset to unstage:

to unstage a file, just do:

```bash
git reset file/to/unstage
```
