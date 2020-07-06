from task import Task
import json
from os import listdir, remove


class TaskService():
    def __init__(self):
        self.path = "ToDoApp/tasks"

# [Asigna un id de forma automatica]
    def assingId(self):
        attempt = 0
        idList = []
        for i in listdir(self.path):
            filePath = "ToDoApp/tasks/%s" % i
            task = json.load(open(filePath))
            idList.append(task["id"])
        for i in range(len(idList)+1):
            if attempt in idList:
                attempt += 1
        return attempt

# [Crea un objeto de la clase Task y lo retorna]
    def addTask(self, id=None, data=[]):
        if id is None:
            id = self.assingId()
        task = Task(id, data[0], data[1], data[2])
        return task

# [Carga las tareas almacenadas en el directorio "tasks"]
    # Esto lo hace iterando dentro del directorio especificado
    # en la variable "path" cada archivo listado con "listdir"
    # luego lo agrega a una lista que es retornada
    def loadTasks(self):
        taskList = []
        for i in listdir(self.path):
            filePath = "ToDoApp/tasks/%s" % i
            task = json.load(open(filePath))
            taskList.append(task)
        return taskList

# [Modifica una tarea especifica segun el id]
    def editTask(self, id, data):
        editTask = json.load(open(self.searchId(id)))
        self.deleteTask(id)
        editTask['name'] = data[0]
        editTask['date'] = data[1]
        editTask['due'] = data[2]
        newFile = open(editTask['path'], 'x')
        json.dump(editTask, newFile)

# [Borra una tarea en particular segun el id]
    def deleteTask(self, id):
        remove(self.searchId(id))

# [Busca una tarea en particular dado un id]
    def searchId(self, id):
        for i in listdir(self.path):
            filePath = "ToDoApp/tasks/%s" % i
            task = json.load(open(filePath))
            if task["id"] == id:
                return filePath


if __name__ == "__main__":
    service = TaskService()
    service.loadTasks()
