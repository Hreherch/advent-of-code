import sys

# careful...
players = int(sys.argv[1])
lastMarble = int(sys.argv[2])

# Uses List...
# Which means you get O(N^2) running inserts and pops everywhere
# And that's pretty crazy with 1 Million inters for part 2, but not bad for part 1
class Game:
    def __init__(self, players, lastMarble):
        # start at round 2 (might break some general cases..)
        self.board = [0, 1]
        self.player = 2
        self.curMarbleVal = 2
        self.next23 = 23
        self.curMarblePos = 1
        self.players = players
        self.lastMarble = lastMarble
        self.score = {}

    def getCWPos(self, n):
        return (self.curMarblePos + n) % len(self.board)

    def getCCWPos(self, n):
        return (self.curMarblePos - n) % len(self.board)

    def setNextPlayer(self):
        self.player += 1
        if self.player > self.players:
            self.player = 1
        self.curMarbleVal += 1

    def play(self):
        if self.curMarbleVal == self.next23:
            removeMarbleAt = self.getCCWPos(7)
            if removeMarbleAt == 0:
                removeMarbleAt = len(self.board)
            value = self.board.pop(removeMarbleAt)
            self.curMarblePos = (removeMarbleAt % len(self.board))
            self.score[self.player] = self.score.get(self.player, 0) + self.next23 + value
            self.setNextPlayer()
            self.next23 += 23
        else:
            placeMarbleAt = self.getCWPos(2)
            if placeMarbleAt == 0:
                placeMarbleAt = len(self.board)
            self.curMarblePos = placeMarbleAt
            self.board.insert(placeMarbleAt, self.curMarbleVal)
            self.setNextPlayer()

game = Game(players, lastMarble)
while game.curMarbleVal <= lastMarble:
    game.play()
    #print(game.board)
print(max(game.score.values()))