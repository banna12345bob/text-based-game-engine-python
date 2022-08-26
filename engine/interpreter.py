from engine.FileRead import File
from engine.debugger import debugger


class room:
    file = "rooms.json"

    def __init__(self, room = 1, dFile = file):
        self.file = File().readFile(dFile)
        if self.file == 0:
            debugger().fatal(f"Failed to read {dFile}")
        self.room = room

    def getName(self):
        try:
            return self.file[str(self.room)]["name"]
        except:
            debugger().error(f"Room {self.room} not found")
            return 0
        


    def getDesciption(self):
        rFile = self.file
        room = self.room
        try:
            return rFile[str(room)]["description"]
        except:
            debugger().error(f"Room {room} not found")
            return 0


    def getFurnature(self):
        rFile = self.file
        room = self.room
        furnatures = []
        try:
            for furnature in rFile[str(room)]["furnature"]:
                furnatures.append(furnature)
            return furnatures
        except:
            debugger().error(f"Room {room} not found")
            return 0

    def getFurnatureDescription(self, furnature):
        rFile = self.file
        room = self.room
        description = ""
        furnature = furnature.lower()
        try:
            if furnature in self.getFurnature():
                description = rFile[str(room)]["furnature"][furnature]["description"]
            return description
        except:
            debugger().error(f"Room {room} not found")
            return 0

    def getFunratureObjects(self, furnature):
        rFile = self.file
        room = self.room
        objects = []
        furnature = furnature.lower()
        try:
            if furnature in self.getFurnature():
                for i in rFile[str(room)]["furnature"][furnature]["objects"]:
                    objects.append(i)
            return objects
        except:
            debugger().error(f"Room {room} not found")
            return 0

    def getFunratureObjectDescriptions(self, furnature, object):
        rFile = self.file
        room = self.room
        furnature = furnature.lower()
        des = "No object description found"
        object = object.lower()
        try:
            if object in self.getFunratureObjects(furnature):
                des = rFile[str(room)]["furnature"][furnature]["objects"][object]
            return des
        except:
            debugger().error(f"Room {room} not found")
            return 0

    def getDirections(self):
        rFile = self.file
        room = self.room
        rDirections = []
        try:
            for direction in rFile[str(room)]["directions"]:
                rDirections.append(direction)
            return rDirections
        except:
            debugger().error(f"Room {room} not found")
            return 0

    def getDirection(self, direction):
        rFile = self.file
        room = self.room
        rDirections = ""
        direction = direction.lower()
        try:
            if direction in self.getDirections():
                rDirections = rFile[str(room)]["directions"][direction]
            return rDirections
        except:
            # Just a quick error catcher 
            # NOTE: this is not a "quick" error cathcer as I build a debug interface for it
            debugger().error(f"Room {room} not found")
            return 0

class object:
    file = "objects.json"

    def __init__(self, room = 0, dFile = file):
        self.file = File().readFile(dFile)
        if self.file == 0:
            debugger().fatal(f"Failed to read {dFile}")

    def getObjects(self):
        objects = []
        for i in self.file:
            objects.append(i)
        return objects
    
    def getDescription(self, object):
        rFile = self.file
        object = object.lower()
        if object in self.getObjects():
            return rFile[object]["description"]
        else:
            return "Object not found"

    def getColour(self, object):
        rFile = self.file
        object = object.lower()
        if object in self.getObjects():
            return rFile[object]["colour"]
        else:
            return "Object not found"