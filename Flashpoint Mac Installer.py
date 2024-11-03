# This is a Python program designed to install the BlueMaxima's Flashpoint application on a Mac.

# While users can already install BlueMaxima's Flashpoint on a Mac by following the website instructions,
# this application is designed to execute those instructions automatically so users don't have to.

# All original code not copied from the installation instructions or somewhere else noted, wrapping of those instructions,
# and comments explaining all of this have been written by me, Noah Kastin, in 2022 or later.

# The program will ensue below.


# This code block imports important modules, ensures that they work, and informs the user of this process.

import os # This imports the module that lets me write commands to the terminal, as these commands are required to install BlueMaxima's Flashpoint.
from pathlib import Path # This imports a submodule that lets me access the folder where Flashpoint will land.
downloads_path = str(Path.home() / "Downloads") # This sets a variable for that location where it'll land.
import lzma # This imports the module that lets me unpack the application so the user doesn't have to do it.
import tarfile # This imports the module that lets me decompress the app so the user doesn't have to.
print("BlueMaxima's Flashpoint Mac Installer launched!") # This line of code ensures that the program hasn't crashed yet by printing if the program's still running.

# This block checks to make sure that try comamnds are working right in the program. Under normal conditions, this block should always execute.
try:
    print("Seems to be working so far...") # A print command that should work, designed to test this function.
    # print(WISPLEEDIDYOUSETMYHAIRONFIREITHINKSOSDSDF) # An intentionally broken print command, also for testing this function.
except:
    print("Uh oh. My message to say this was working didn't work. Luckily this hasn't actually done anything on your computer yet. Please try running the program again or contact me for tech support help if the usual methods, e.g. turning your computer on and off again, don't work.")
else:
    print("All right, let's get this installation going. BD")

os.system("echo App installation in progress...") # This prints a message to ensure that the os module is working. This only renders in the terminal.


# This code block clones the BlueMaxima's Flashpoint repository onto the user's computer.

# print(os.path.isdir('/Applications')) # This is a test case to check if I understand how to check for directories.

# This installs BlueMaxima's Flashpoint on the user's computer. It used to check to make sure there wasn't already a copy there, but apparently the terminal does that already so this doesn't need to.
try:
     # print("Yes.") # A print command to start testing this try command.
     # print(erm) # An intentionally broken print command to finish testing this try command.

    # This actually installs the application on the user's computer.
    os.system("curl -fko ~/Downloads/fp13_mac_legacy.tar.xz https://download.unstable.life/upload/fp13_mac_legacy.tar.xz")
except:
    print("Oh no somehow I failed to install the app on your computer AAAAAAAAH\nahem\nPlease run the Uninstaller and then try this again. If it doesn't work, please contact me for tech support help.")
else:
    print("This all means the app is installed on your computer. Nice job! | ^ _ ^ |")
    print("Now, we just need to unpack the application so you can use it!")
    print("Hang in there, this can take a while.")
    # This code block tries to unpack the application so the user doesn't have to do it.
    try:
        # Decompress the .xz file
        xz_file = downloads_path + "/fp13_mac_legacy.tar.xz"
        tar_file = downloads_path + "/fp13_mac_legacy.tar"
        
        with lzma.open(xz_file, "rb") as f:
            with open(tar_file, "wb") as outF:
                outF.write(f.read())

        print("Okay, it's open. Now we just need to extract it!")
        
        # Extract the .tar file
        if tarfile.is_tarfile(tar_file):
            with tarfile.open(tar_file, "r") as tar:
                tar.extractall(path=downloads_path)

    except Exception as e:
        print(f"Hmm. That doesn't seem to have worked. Try right-clicking on the app in your Downloads folder and using the Archive Utility on it. Maybe you'll have more luck than I just did. Error: {e}")
    else:
        print("Yay, we're all done! Enjoy BlueMaxima's Flashpoint!")
