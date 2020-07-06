import tkinter as tk


class IdWindow(tk.Frame):
    def __init__(self, master, service, boss, purpose):
        super().__init__(master)
        self.master = master
        self.masterService = service
        self.boss = boss
        self.purpose = purpose
        self.addTextboxes()
        self.addLabels()
        self.addButtons()
        self.grid()

    def addTextboxes(self):
        self.idBox = tk.Entry(self.master, width=20)
        self.idBox.grid(column=1, row=0)

    def addLabels(self):
        self.nameLabel = tk.Label(self.master,
                                  text='Id:')
        self.nameLabel.grid(column=0, row=0)

    def addButtons(self):
        self.saveButton = tk.Button(self.master, text="Buscar",
                                    command=self.searchId)
        self.saveButton.grid(column=3, row=0)

    def searchId(self):
        self.id = int(self.idBox.get())
        self.masterService.deleteTask(self.id)
        self.boss.updateTaskChart()
        self.master.destroy()


if __name__ == "__main__":
    branch = tk.Tk()
    idWindow = IdWindow(branch)
    branch.mainloop()
