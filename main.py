import turtle
import random

class Circuito():
    runners = {}
    __posStartY = (-30, -10, 10, 30)
    __turtleColor = ('red', 'blue', 'purple', 'orange')
    __turtleName= ('Raphael', 'Leonardo', 'Donatello', 'MichelAngelo')
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20
        
        self.__createRunners()
        
    def __createRunners(self):
        turtles = []
        for i in range(4):
            newTurtle = turtle.Turtle()
            newTurtle.shape('turtle')
            newTurtle.color(self.__turtleColor[i])
            newTurtle.penup()
            newTurtle.setpos(self.__startLine, self.__posStartY[i])
            
            turtles.append(newTurtle)

        self.runners = (dict(zip(self.__turtleName, turtles)))


    def competir(self):
        hayGanador = False

        while not hayGanador:
            for runnerName, runner in self.runners.items():
                runner.pendown()
                avance = random.randint(1, 6)
                runner.forward(avance)
            
                if runner.position()[0] >= self.__finishLine:
                    hayGanador = True

                    print("¡¡Ha ganado {}!!".format(runnerName))                    
    

if __name__ == '__main__':
    circuito = Circuito(640, 480)
    circuito.competir()

    