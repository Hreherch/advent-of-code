import sys

# careful...
players = int(sys.argv[1])
lastMarble = int(sys.argv[2])

# Doubly Linked List Node Definition
class Marble:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value

class Game:
    def __init__(self, players, lastMarble):
        marble0 = Marble(0)
        marble0.next = marble0
        marble0.prev = marble0
        self.currentMarble = marble0
        self.player = 1
        self.marbleValue = 1
        self.next23 = 23
        self.players = players
        self.lastMarble = lastMarble
        self.score = {}

    def setNextPlayer(self):
        self.player += 1
        if self.player > self.players:
            self.player = 1
        self.marbleValue += 1

    def addScore(self, player, score):
        self.score[player] = self.score.get(player, 0) + score

    def play(self):
        marble = self.currentMarble
        if self.marbleValue == self.next23:
            for i in range(7):
                marble = marble.prev
            marble.prev.next = marble.next
            marble.next.prev = marble.prev
            self.currentMarble = marble.next
            self.addScore(self.player, marble.value + self.next23)
            self.next23 += 23
        else:
            for i in range(2):
                marble = marble.next
            newMarble = Marble(self.marbleValue)
            newMarble.next = marble
            newMarble.prev = marble.prev
            marble.prev.next = newMarble # must do before the next step :p
            marble.prev = newMarble
            self.currentMarble = newMarble
        self.setNextPlayer()

    # yay debugging -- could fail if 0 ever removed
    def __str__(self):
        s = ""
        marble = self.currentMarble
        while marble.value != 0:
            marble = marble.next
        s += "[{}]".format(self.player) + "  "
        while True:
            s += str(marble.value) + "{} ".format("*" if marble.value == self.currentMarble.value else "")
            marble = marble.next
            if marble.value == 0:
                break
        return s

game = Game(players, lastMarble)
while game.marbleValue <= lastMarble:
    game.play()
    #print(game)
print(max(game.score.values()))