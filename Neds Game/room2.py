
class Room:

    def __init__(self, name: str, image_filepath: str):
        """
        A Room in the Room Adventure game.

        name: str - a name for the room
        image_filepath: str - the relative filepath to the image
        """
        self.name = name
        self.image = image_filepath
        self.exits: dict[str, 'Room'] = {}
        self.items: dict[str, str] = {}
        self.grabbables = []

    def add_exit(self, location: str, room: 'Room | None')-> None:
        """
        
        Adds an exit to the room.
        
        location: str - a direction such as "north", "south", "east", "west", "up", "down", etc...
        room: Room | None - a room object that the `location` leads to.
        """

        self.exits[location] = room

    def add_item(self, label: str, desc:str) -> None:
        self.items[label] = desc

    def add_grabbable(self, item:str) -> None:
        self.grabbables.append(item)

    def deleta_grabbable(self, item: str) -> None:
        self.grabbales.remove(item)

    def __str__(self) -> str:
        result = f"you are in {self.name}\n"

        result += "You see:"
        for item in self.items.keys():
            result += item + " "
        result += "\n"
        
        result += "Exits: "
        for exit in self.exits.keys():
            result += exit + " "
        result += "\n"

        return result


    