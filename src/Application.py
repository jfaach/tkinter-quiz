#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Import the required modules
from tkinter import *
from tree import Node


class ProgramGUI:
    def __init__(self, master):
        self.master = master

        # Initialize victory counter
        self.count_victory = 0

        # Initialize animal tree
        self.animalTree = Node(
            "Vive na água",
            Node("Tubarão"),
            Node("Macaco"),
        )

        self.direction = None

        # set current node and parent node to animal tree root
        self.current_node = self.animalTree
        self.parent_node = self.animalTree

        master.title("Jogo dos Animais")
        master.minsize(width=400, height=100)

        self.frame = Frame(self.master)
        self.frame.pack()

        self.menu()

    def initializeMainScreen(self):
        self.current_node = self.animalTree
        self.parent_node = self.animalTree
        self.direction = ""

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.question = Label(self.frame)
        self.question.grid(row=2, columnspan=2, padx=20, pady=10)

        self.button_yes = Button(self.frame, text="Sim", command=self.answerYes)
        self.button_yes.grid(row=3, column=0)

        self.button_no = Button(self.frame, text="Não", command=self.answerNo)
        self.button_no.grid(row=3, column=1)

        self.button_continue = Button(
            self.frame, text="Continuar?", command=self.answerContinue
        )

        self.button_animal_name = Button(
            self.frame, text="Responder", command=self.answerAnimalName
        )

        self.button_animal_feature = Button(
            self.frame, text="Responder", command=self.answerAnimalFeature
        )

        self.question_entry = Entry(self.frame, width=50)

        self.loadQuestion()

    def menu(self):
        self.question = Label(self.frame)
        self.question.grid(row=2, columnspan=2, padx=20, pady=10)
        self.question.config(text="Pense em um animal!")

        self.button_start = Button(
            self.frame, text="Ok", command=self.initializeMainScreen
        )
        self.button_start.grid(row=3, column=0)

    def answerAnimalName(self):
        self.animalName = self.question_entry.get()
        self.question.config(
            text=f"Um(a) {self.animalName} ____________ mas um(a) {self.current_node.value} não"
        )

        self.question_entry.delete(0, "end")
        self.question_entry.grid(row=3)

        self.button_animal_name.destroy()
        self.button_animal_feature.grid(row=4, column=0, pady=10)

    def answerAnimalFeature(self):
        self.animalFeature = self.question_entry.get()
        animalNode = Node(self.animalFeature, Node(self.animalName))
        if self.direction == "right":
            self.parent_node.insertRightNode(animalNode)
        elif self.direction == "left":
            self.parent_node.insertLeftNode(animalNode)

        self.frame.destroy()
        self.frame = Frame(self.master)
        self.frame.pack()
        self.initializeMainScreen()

    def loadQuestion(self):
        if not self.current_node.isLeaf():
            question = f"O animal que você pensou {self.current_node.value} ?"
            self.question.config(text=question)

        if self.current_node.isLeaf():
            question = f"O animal que você pensou é {self.current_node.value} ?"
            self.question.config(text=question)

    def answerYes(self):
        # if current node is leaf increase victory counter
        # if not get child node
        if self.current_node.isLeaf():
            self.count_victory += 1
            if self.count_victory == 1:
                self.question.config(text="Acertei !!")
            else:
                self.question.config(text="Acertei de novo !!")
            self.button_yes.destroy()
            self.button_no.destroy()

            self.current_node = self.animalTree
            self.parent_node = self.animalTree

            self.button_continue.grid(row=3, column=0)
        else:
            self.parent_node = self.current_node
            self.current_node = self.current_node.left
            self.direction = "left"
            self.loadQuestion()

    def answerNo(self):
        if not self.current_node.isLeaf():
            self.parent_node = self.current_node
            self.current_node = self.current_node.right
            self.direction = "right"
            self.loadQuestion()
        elif self.current_node.isLeaf():
            self.button_yes.destroy()
            self.button_no.destroy()
            self.question.config(text="Qual animal voce pensou ?")
            self.question_entry.grid(row=3)
            self.button_animal_name.grid(row=4, column=0, pady=10)

    def answerContinue(self):
        self.frame.destroy()
        self.frame = Frame(self.master)
        self.frame.pack()

        self.menu()


# Create an object of ProgramGUI to begin the program
root = Tk()
gui = ProgramGUI(root)
root.mainloop()
