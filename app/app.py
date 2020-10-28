import os, sys, shutil, random

def readPath(): # Read .app.config file to get the folder we want to copy. 
    file = open("path", "r")
    folderName = file.readline()
    return folderName

def copyFolder(folderName):
    appPath = os.getcwd()

    folderPath = "C:/xampp/htdocs/" + folderName
    folderFinalName = appPath + "/" + folderName
    
    # Check if the folder exists
    if os.path.isdir(folderFinalName):
        n = str(random.randint(1, 100))
        folderFinalName = folderFinalName + "-" + n
        
        shutil.copytree(folderPath, folderFinalName)
    else:
        shutil.copytree(folderPath, folderFinalName)
        

# ---------------------------------------
# App starts here.
# ---------------------------------------

folderName = readPath() # Get the folder path
copyFolder(folderName); # Copy the folder to destination