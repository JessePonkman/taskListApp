import json


class Task():
    def __init__(self, id, name="", date="", due=""):
        self.path = "ToDoApp/tasks/task%s.json" % id
        self.id = id
        self.name = name
        self.date = date
        self.due = due
        self.storeData()

    def storeData(self):
        json.dump(self.__dict__, open(self.path, "w"))
