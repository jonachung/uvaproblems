class Bumper(object):
    xPos = 0
    yPos = 0
    cost = 0
    value = 0

    def __init__(self, xPos, yPos, value, cost):
        self.xPos = xPos
        self.yPos = yPos
        self.value = value
        self.cost = cost

    def get_xPos(self):
        return self.xPos

    def get_yPos(self):
        return self.yPos

    def get_value(self):
        return self.value

    def get_cost(self):
        return self.cost


def make_bumper(xPos, yPos, value, cost):
    bumper = Bumper(xPos, yPos, value, cost)
    return bumper


class Ball(object):
    xPos = 0
    yPos = 0
    direction = 0
    lifetime = 0
    points = 0

    def __init__(self, xPos, yPos, direction, lifetime, points):
        self.xPos = xPos
        self.yPos = yPos
        self.direction = direction
        self.lifetime = lifetime
        self.points = points

    def get_xPos(self):
        return self.xPos

    def get_yPos(self):
        return self.yPos

    def get_direction(self):
        return self.direction

    def get_lifetime(self):
        return self.lifetime

    def get_points(self):
        return self.points

    def set_xPos(self, xPos):
        self.xPos = xPos

    def set_yPos(self, yPos):
        self.yPos = yPos

    def set_direction(self, direction):
        self.direction = direction

    def set_lifetime(self, lifetime):
        self.lifetime = lifetime

    def set_points(self, points):
        self.points = points


def make_ball(xPos, yPos, direction, lifetime, points):
    ball = Ball(xPos, yPos, direction, lifetime, points)
    return ball


def doesHitBumper(bumperList, newYPosition, newXPosition):
    for i in range(0, len(bumperList)):  # if ball hits bumper
        if newYPosition == bumperList[i].get_yPos() and newXPosition == bumperList[i].get_xPos():
            return True
    return False


def doesHitWall(direction, newXPosition, newYPosition, row, col):
    if direction == 0 and newXPosition == row:
        return True
    elif direction == 1 and newYPosition == col:
        return True
    elif direction == 2 and newXPosition < 0:
        return True
    elif direction == 3 and newYPosition < 0:
        return True


def changeDirection(direction, ball, hitWall, wallCost, hitBumper, bumperList, newXPosition, newYPosition):
    if direction == 0:
        ball.set_direction(3)
    elif direction == 1:
        ball.set_direction(0)
    elif direction == 2:
        ball.set_direction(1)
    elif direction == 3:
        ball.set_direction(2)
    if hitWall:
        life = ball.get_lifetime()
        ball.set_lifetime(life - wallCost)
        life = ball.get_lifetime()
        ball.set_lifetime(life - 1)
    elif hitBumper:
        for i in range(0, len(bumperList)):
            if newXPosition == bumperList[i].get_xPos() and newYPosition == bumperList[i].get_yPos():
                life = ball.get_lifetime()
                ball.set_lifetime(life - bumperList[i].get_cost())
                life = ball.get_lifetime()
                ball.set_lifetime(life - 1)
    else:
        life = ball.get_lifetime()
        ball.set_lifetime(life - 1)


def addValue(ball, newXPosition, newYPosition, bumperList):
    for i in range(0, len(bumperList)):
        if newXPosition == bumperList[i].get_xPos() and newYPosition == bumperList[i].get_yPos():
            if ball.get_lifetime() != 0:
                points = ball.get_points()
                ball.set_points(points + bumperList[i].get_value())
            #     print("I added points")
            # else:
            #     print("I did not add points")


def makeMove(ball, newXPosition, newYPosition):
    life = ball.get_lifetime()
    ball.set_yPos(newYPosition)
    ball.set_xPos(newXPosition)
    ball.set_lifetime(life - 1)


def moveDirection(direction, ball, bumperList, row, col, wallCost):
    if direction == 0:
        newXPosition = ball.get_xPos() + 1
        newYPosition = ball.get_yPos()
    elif direction == 1:
        newXPosition = ball.get_xPos()
        newYPosition = ball.get_yPos() + 1
    elif direction == 2:
        newXPosition = ball.get_xPos() - 1
        newYPosition = ball.get_yPos()
    else:
        newXPosition = ball.get_xPos()
        newYPosition = ball.get_yPos() - 1
    if doesHitBumper(bumperList, newYPosition, newXPosition):
        changeDirection(direction, ball, False, wallCost, True, bumperList, newXPosition, newYPosition)
        addValue(ball, newXPosition, newYPosition, bumperList)
    elif doesHitWall(direction, newXPosition, newYPosition, row, col):
        changeDirection(direction, ball, True, wallCost, False, bumperList, newXPosition, newYPosition)
    else:
        makeMove(ball, newXPosition, newYPosition)


def moveBall(ball, row, col, wallCost, bumperList):
    if ball.get_direction() == 0:
        moveDirection(0, ball, bumperList, row, col, wallCost)
    elif ball.get_direction() == 1:
        moveDirection(1, ball, bumperList, row, col, wallCost)
    elif ball.get_direction() == 2:
        moveDirection(2, ball, bumperList, row, col, wallCost)
    elif ball.get_direction() == 3:
        moveDirection(3, ball, bumperList, row, col, wallCost)


def main():
    boardRowCol = input().split()
    row = int(boardRowCol[0])
    col = int(boardRowCol[1])
    wallCost = int(input())
    numBumpers = int(input())
    bumpersList = []
    totalValue = 0
    for i in range(0, numBumpers):
        info = input().split()
        xPos = int(info[0])
        yPos = int(info[1])
        value = int(info[2])
        cost = int(info[3])
        bump = make_bumper(xPos, yPos, value, cost)
        bumpersList.append(bump)
    info = input()
    ballInfo = info.split()
    count = 1
    while info != "":
        xPos = int(ballInfo[0])
        yPos = int(ballInfo[1])
        direction = int(ballInfo[2])
        lifetime = int(ballInfo[3])
        points = 0
        ball = make_ball(xPos, yPos, direction, lifetime, points)
        while ball.lifetime > 0:

            moveBall(ball, row, col, wallCost, bumpersList)

        print(str(ball.get_points()))
        totalValue += ball.get_points()
        count += 1
        info = input()
        ballInfo = info.split()
    print(str(totalValue))


main()
