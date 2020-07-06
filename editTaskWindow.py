import tkinter as tk
import json


class EditTaskWindow(tk.Frame):
    def __init__(self, master, service=None, boss=None):
        super().__init__(master)
        self.master = master
        self.masterService = service
        self.boss = boss
        self.addButtons()
        self.addTextboxes()
        self.addLabels()
        self.grid(sticky='nswe')

    def addTextboxes(self):
        self.idBox = tk.Entry(self.master, width=20)
        self.idBox.grid(column=1, row=0, columnspan=2)

        self.nameBox = tk.Entry(self.master, width=32)
        self.nameBox.grid(column=1, row=1, columnspan=4)

        self.dateBox = tk.Entry(self.master, width=10)
        self.dateBox.grid(column=1, row=2)

        self.dueBox = tk.Entry(self.master, width=10)
        self.dueBox.grid(column=3, row=2)

    def addLabels(self):
        self.idLabel = tk.Label(self.master, width=10, height=1,
                                text='Id:')
        self.idLabel.grid(column=0, row=0)

        self.nameLabel = tk.Label(self.master, width=10, height=1,
                                  text='Nombre:')
        self.nameLabel.grid(column=0, row=1)

        self.dateLabel = tk.Label(self.master, width=10, height=1,
                                  text='Inicio:')
        self.dateLabel.grid(column=0, row=2, ipadx=0)

        self.dueLabel = tk.Label(self.master, width=10, height=1,
                                 text='Hasta:')
        self.dueLabel.grid(column=2, row=2)

    def addButtons(self):
        self.searchButton = tk.Button(self.master, text="Buscar",
                                      command=self.searchId, width=8)
        self.searchButton.grid(column=3, row=0)

        self.saveButton = tk.Button(self.master, text="Guardar",
                                    width=18, command=self.editTask)
        self.saveButton.grid(column=0, columnspan=2, row=3)

        self.cancelButton = tk.Button(self.master, text="Cancelar",
                                      command=self.master.destroy,
                                      width=18)
        self.cancelButton.grid(column=2, columnspan=2, row=3)

    def searchId(self):
        self.id = int(self.idBox.get())
        filePath = self.masterService.searchId(self.id)
        editTask = json.load(open(filePath))
        self.nameBox.insert(0, editTask['name'])
        self.dateBox.insert(0, editTask['date'])
        self.dueBox.insert(0, editTask['due'])

    def editTask(self):
        nombre = self.nameBox.get()
        date = self.dateBox.get()
        due = self.dueBox.get()
        self.data = [nombre, date, due]
        self.masterService.editTask(self.id, self.data)
        self.boss.updateTaskChart()
        self.master.destroy()


if __name__ == "__main__":
    branch = tk.Tk()
    addTaskWindow = EditTaskWindow(branch)
    branch.mainloop()
