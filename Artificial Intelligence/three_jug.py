class Jug:

    def canFill(self) -> bool:
        if self.water < self.__MAX: return True
        else: return False

    def fill(self):
        self.water = self.__MAX

####################################################    

    def canEmpty(self) -> bool:
        if self.water > 0: return True
        else: return False

    def empty(self):
        self.water = 0

####################################################
    
    def canTransferFrom(self) -> bool:
        if self.water > 0: return True
        else: return False

    def add(self, amt:int) -> int:
        self.water += amt
        self.__clip()

        remaining = self.__MAX - amt
        if (remaining > 0): return remaining
        else: return 0

######################################################

    def __init__(self, max) -> None:
        self.__MAX = max
        self.water = 0

    def __clip(self):
        if (self.water > self.__MAX):
            self.water = self.__MAX

    def __str__(self) -> str:
        return 'Jug[' + str(self.__MAX) + ']'


def transfer(toJug:Jug, fromJug:Jug):
    remaining = toJug.add(fromJug.water)
    fromJug.water = remaining


def BFS(goal:tuple) -> list:
    jug1 = Jug(5)
    jug2 = Jug(4)

    traversePath = []
    finalPath = []

    q_front = 0
    while (not (jug1.water == goal[0]) and (jug2.water == goal[1])):
        traversePath.append((jug1, jug2))
        print(traversePath)

        j1 = jug1
        if jug1.canFill():
            j1.fill()
            if (j1, jug2) not in traversePath:
                traversePath.append((j1, jug2))
        j2 = jug2
        if jug2.canFill():
            j2.fill()
            if (j1, jug2) not in traversePath:
                traversePath.append((jug1, j2))
        
        j1 = jug1
        if jug1.canEmpty():
            j1.empty()
            if (j1, jug2) not in traversePath:
                traversePath.append((j1, jug2))
        j2 = jug2
        if jug2.canEmpty():
            j2.empty()
            if (j1, jug2) not in traversePath:
                traversePath.append((jug1, j2))

        j1 = jug1
        j2 = jug2
        if jug1.canTransferFrom():
            transfer(j2, j1)
            if (j1, jug2) not in traversePath:
                traversePath.append((j1, j2))
            
        j1 = jug1
        j2 = jug2
        if jug2.canTransferFrom():
            transfer(j1, j2)
            if (j1, jug2) not in traversePath:
                traversePath.append((j1, j2))

        jug1 = traversePath[q_front][0]
        jug2 = traversePath[q_front][1]
        q_front += 1

    # print(traversePath)

def main():
    BFS(goal=(2,0))

if __name__ == '__main__':
    main()