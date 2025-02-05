print(__name__)

# this wil print __main__ because it is being executed in it's originla file, without baing imported in another file.
# in this same dir, there is a file called other.py thar does not return __main__ bacause it imports this file you are reading. 

# the "other" file will return index (the name of the file it is importing from)

# so:

if __name__ == "__main__":
    print("Main file") # returns this if index file is run
else:
    print("Not main file") # returns this if any other file runs it.
