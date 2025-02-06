# Git checkout is awesome

```bash 

$ echo some text > file.txt

$ echo something else > file.txt

$ cat file.txt
~ something else

$ git checkout file.txt

$ cat file.txt
~ some text

$ echo from commit before > file.txt

$ cat file.txt
~ from commit before

$ git add file.txt && git commit -m "change file.txt"

$ echo from now > file.txt

$ cat file.txt
~ from now

$ git log --oneline
~ 68ab219 (HEAD -> main, origin/main, origin/HEAD) change file.txt
~ b89a9e8 something else
~ 49979d9 something else
...

$ git add file.txt && git commit -m "change file.txt (2nd time)"

$ git log --oneline
~ 12ab443 (HEAD -> main, origin/main, origin/HEAD) change file.txt (2nd time)
~ 68ab219 change file.txt
~ b89a9e8 something else

$ git ckeckout 68ab219 file.txt
#               commit 
#                 id

$ cat file.txt
~ from commit before

$ git checkout HEAD file.txt

$ cat file.txt
~ from now

```


