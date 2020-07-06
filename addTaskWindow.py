import tkinter as tk


class AddTaskWindow(tk.Frame):
    def __init__(self, master, service, boss):
        super().__init__(master)
        self.master = master
        self.masterService = service
        self.boss = boss
        self.addButtons()
        self.addTextboxes()
        self.addLabels()
        self.grid(sticky='nswe')

    def addTextboxes(self):
        self.nameBox = tk.Entry(self.master, width=32)
        self.nameBox.grid(column=1, row=0, columnspan=4)

        self.dateBox = tk.Entry(self.master, width=10)
        self.dateBox.grid(column=1, row=1)

        self.dueBox = tk.Entry(self.master, width=10)
        self.dueBox.grid(column=3, row=1)

    def addLabels(self):
        self.nameLabel = tk.Label(self.master, width=10, height=1,
                                  text='Nombre:')
        self.nameLabel.grid(column=0, row=0)

        self.dateLabel = tk.Label(self.master, width=10, height=1,
                                  text='Inicio:')
        self.dateLabel.grid(column=0, row=1)

        self.dueLabel = tk.Label(self.master, width=10, height=1,
                                 text='Hasta:')
        self.dueLabel.grid(column=2, row=1)

    def addButtons(self):
        self.saveButton = tk.Button(self.master, text="Guardar",
                                    width=18, command=self.addTask)
        self.saveButton.grid(column=0, columnspan=2, row=2)

        self.cancelButton = tk.Button(self.master, text="Cancelar",
                                      command=self.master.destroy,
                                      width=18)
        self.cancelButton.grid(column=2, columnspan=2, row=2)

    def addTask(self, id=None):
        nombre = self.nameBox.get()
        date = self.dateBox.get()
        due = self.dueBox.get()
        self.data = [nombre, date, due]
        task = self.masterService.addTask(data=self.data)
        self.boss.displayTask(task.__dict__)
        self.master.destroy()
        del self


if __name__ == "__main__":
    branch = tk.Tk()
    addTaskWindow = AddTaskWindow(branch)
    branch.mainloop()
