import os

"""
run as sudo

you can use this script on unix base os


before run this script , update whatismyip directory
"""

os.system("rm /bin/whatismyip")


script = ("cp dist/whatismyip /bin")
os.system(script)

print("The whatismyip script was update in bin dir")