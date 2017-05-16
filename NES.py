import pickle
import zipfile
import Improvements.Improvement as Improvement
import Hex
from NESCore import *
import os
import json


def print_menu():  ## Your menu design here
    print 30 * "-", "MENU", 30 * "-"
    print "1. List Players"
    print "2. Describe Nation"
    print "3. Manage Players"
    print "4. Dump World to Screen"
    print "5. Step World"
    print "7. Select Run"
    print "8. Exit"
    print 67 * "-"


# World loading

loop = True
path = "dsjfhasjklfghakslfg"
run = 0
world = World()


def addPlayer(name, nationname):
    if world.hasNation(nationname):
        return False


def listPlayers():
    print world.getPlayers()


def exortPlayer():
    name = raw_input("Player Name")
    exportpath = raw_input("Save where?")
    f = file(exportpath, 'w')
    json.dump(players[name], f)


def importPlayer():
    exportpath = raw_input("Load path?")
    f = file(exportpath, 'r')
    player = json.load(r)
    while (~addPlayer(player.getName(), player)):
        print "Player name in use please supply another one"


def upgradeWorld(path):
    # upgrade world to current format as necessay
    pass


def saveWorld(path):
    f = file(path, 'w')
    pickle.dump(world, f)
    f.close()


def initWorld(path):
    # create info file with version ifo etc
    # create world file with version
    saveWorld(path + '/world.pickle')


def loadWorld(path):
    world = pickle.load(file(path + "/world.pickle", "r"))


def dumpWorld():
    for player in players:
        name = player.getName()
        # dump nation
        # dump nation networks
        # dump network hexes


def preflight():
    # check if anything is amiss and report it.
    pass


def run_world():
    preflight()
    world.run()


# print "Welcome please provide a file by name in the \"runs\" directory \n- \"Runs\" must have an integer name, do not rename them.\n- They are named in sequential order, to make a backup duplicate the runs directory"


while True:
    print os.listdir('runs')
    if len(os.listdir('runs')) < 2:
        print "No runs, a new run will be created with name 0"
        os.mkdir('runs/0')
        initWorld('runs/0')
        break
    path = raw_input("Load which run?:")
    path = 'runs/' + path
    if os.path.isdir(path):
        data = loadWorld(path)
        run = int(os.path.basename(path))
        break
    else:
        print "Bad directory, try again"

while loop:  ## While loop which will keep going until loop = False
    print_menu()  ## Displays menu
    choice = input("Enter your choice [1-5]: ")

    if choice == 1:
        print "1:List players"
        listPlayers()
    elif choice == 2:
        id = raw_input("Nation name or id")
        print world.getNation(id)
        ## You can add your code or functions here
    elif choice == 3:
        print "3:Add/Remove Nation"
        choice = input("1.Add \n2.Remove ")
        if choice == 1:
            name = raw_input("Name: ")
            world.addNation(name)
        elif choice == 2:
            id = raw_input("Nation name or id:")
            if world.hasNation(id):
                targetNation = world.getNation(id)
                yes = raw_input(
                    "Nation:" + targetNation.getName() + " will be deleted, THIS CANNOT BE UNDONE. CONTINUE (y/n)?")
                if choice == 'y':
                    world.removeNation(name);
        else:
            print "Invalid choice"

    elif choice == 4:
        print "4:Dump world to screen"
        ## You can add your code or functions here
    elif choice == 5:
        print "5: Step world"
        run_world()
        ## You can add your code or functions here
        loop = False  # This will make the while loop to end as not value of loop is set to False
    elif choice == 6:
        print "6: Step world"
        ## You can add your code or functions here
        loop = False  # This will make the while loop to end as not value of loop is set to False
    elif choice == 7:
        print "7: Step world"
        ## You can add your code or functions here
        loop = False  # This will make the while loop to end as not value of loop is set to False
    elif choice == 8:
        print "8: Step world"
        ## You can add your code or functions here
        loop = False  # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        raw_input("Wrong option selection. Enter any key to try again..")
