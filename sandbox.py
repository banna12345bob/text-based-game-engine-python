from engine import engine

# This interfaces with application.
# It inherents all the functions from engine.application and then sets area and room correctly
class sandbox(engine.application):
    def __init__(self, area, room):
        self.roomFile = "sandbox/sandboxRooms.json"
        self.objectFile = "sandbox/sandboxObjects.json"
        super().__init__(area, room, self.roomFile, self.objectFile)
    
    def run(self):
        app = sandbox(self.area, self.room)
        print(app.printNameandDes())
        a = self.entryPoint()
        while a:
            engine.commandManager(self.area, self.room, self.roomsFile, self.objectFile, self.saveFile, self.player).mountCommand([engine.commands.help, engine.commands.look, engine.commands.use, engine.commands.quit, engine.commands.exit, engine.commands.inv, engine.commands.pickup, engine.commands.drop, engine.commands.save, engine.commands.load, engine.commands.dir, engine.commands.talk, engine.commands.kill])
            engine.commandManager(self.area, self.room, self.roomsFile, self.objectFile, self.saveFile, self.player).mountCommand([engine.commands.resetinv, engine.commands.give, engine.commands.open, engine.commands.debug], True)
            lCommand = a[1]
            a = globals()[lCommand[0]]
            print(a(self.area, self.room, self.roomsFile, self.objectFile, self.saveFile, self.player).run())
            a = self.entryPoint()

class testcmd(engine.command):
    def __init__(self, area, room, roomsFile, objectFile, saveFile, player):
        super().__init__(area, room, roomsFile, objectFile, saveFile, player)
        self.description = "Testing command"

    def run(self):
        return "Ran application command"

sandbox(1, 1).commandManager.mountCommand(testcmd)
sandbox(1, 1).run()