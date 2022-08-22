from FileRead import File
import commands

class inventory:
    def __init__(self):
        try:
            self.inventory = File().readFile("save.json")
        except:
            self.inventory = File().readFile("save.json")

    def getInventory(self):
        return self.inventory["inventory"]

    def addToInventory(self, slot, object):
        lInventory = self.inventory
        lInventory["inventory"][slot] = object
        File().writeFile("save.json", lInventory)

    def resetInventory(self, currentRoom):
        commands.commands(currentRoom).save()
        lInventory = File().readFile("save.json")
        lInventory["inventory"] = {"1":"","2":"","3":"","4":"","5":""}
        File().writeFile("save.json", lInventory)
        return