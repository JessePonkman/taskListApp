import tkinter as tk
from taskService import TaskService
from addTaskWindow import AddTaskWindow
from idWindow import IdWindow
from editTaskWindow import EditTaskWindow


class App(tk.Frame):
    def __init__(self, master=None, service=None):
        super().__init__(master)
        self.master = master
        self.service = service
        self.pack()
        self.addButtons()
        self.addLabels()
        self.loadTasks()

# Lista de botones:
#   --> addTask: Añade una tarea a la lista
#   --> deleteTask: Quita las tareas marcadas
#   --> editTask: Modificar tarea seleccionada
#   --> closeApp: Matar la app
    def addButtons(self):
        self.addTask = tk.Button(self, text="Añadir Tarea",
                                 command=self.addTaskWindow)
        self.addTask.grid(row=0, column=2)

        self.deleteTask = tk.Button(self, text="Eliminar tareas",
                                    command=self.deleteTaskButton)
        self.deleteTask.grid(row=0, column=3)

        self.editTask = tk.Button(self, text="Modificar tarea",
                                  command=self.editTaskButton)
        self.editTask.grid(row=0, column=4)

# Lista de etiquetas:
#   --> columna donde estaran las checkboxes
#   --> columna de id's de las tareas
#   --> columna de nombres de tareas
#   --> columna de fechas de tareas
#   --> columna de fecha "hasta"
    def addLabels(self):
        self.taskId = tk.Label(self, text="Id")
        self.taskId.grid(row=1, column=1)

        self.taskName = tk.Label(self, text="Nombre")
        self.taskName.grid(row=1, column=2)

        self.taskDate = tk.Label(self, text="Fecha")
        self.taskDate.grid(row=1, column=3)

        self.taskDue = tk.Label(self, text="Hasta")
        self.taskDue.grid(row=1, column=4)

# Agregar una tarea a la lista de tareas
# Llama al metodo addTask() del serivicio asociado self.service
# el cual retorna un diccionario de un objeto Task que posteriormente
# se reparte su contenido en sus correspondientes Labels
# Ventana para crear la nueva tarea
    def addTaskWindow(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newAddTaskWindow = AddTaskWindow(self.newWindow, self.service,
                                              self)

    def getTaskById(self, purpose):
        self.newWindow = tk.Toplevel(self.master)
        self.newIdWindow = IdWindow(self.newWindow, self.service,
                                    self, purpose)

# Eliminar una tarea de la lista de tareas
    def deleteTaskButton(self):
        self.getTaskById('deletion')

# Modificar una tarea de la lista de tareas
    def editTaskButton(self):
        self.newWindow = tk.Toplevel(self.master)
        self.newIdWindow = EditTaskWindow(self.newWindow, self.service,
                                          self)

    def updateTaskChart(self):
        self.cleanLabels()
        self.loadTasks()

# Carga las tareas a la ventana
    def loadTasks(self):
        taskList = self.service.loadTasks()
        for i in taskList:
            self.displayTask(i)

# Muestra las tareas
    def displayTask(self, task):
        self.taskId["text"] += "\n%s" % task["id"]
        self.taskName["text"] += "\n%s" % task["name"]
        self.taskDate["text"] += "\n%s" % task["date"]
        self.taskDue["text"] += "\n%s" % task["due"]

# Limpia las etiquetas (usado para actualizaciones)
    def cleanLabels(self):
        self.taskId["text"] = "Id"
        self.taskName["text"] = "Nombre"
        self.taskDate["text"] = "Fecha"
        self.taskDue["text"] = "Hasta"


if __name__ == "__main__":
    root = tk.Tk()
    service = TaskService()
    app = App(root, service)
    app.mainloop()
