#!/usr/bin/env python3
import random

moves = ['rock', 'paper', 'scissors']


class Player():
    def __init__(self):
        self.score = 0

    def move(self):
        pass

    def learn(self, learnMove):
        pass


class RandomPlayer(Player):
    def move(self):
        Random = random.choice(moves)
        return (Random)


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.learnMove = None

    def move(self):
        if self.learnMove is None:
            Reflect = random.choice(moves)
            return (Reflect)
        else:
            Reflect = self.learnMove
            return (Reflect)

    def learn(self, learnMove):
        self.learnMove = learnMove


class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.cycle = 0

    def move(self):
        Cycle = None
        if self.cycle == 0:
            Cycle = moves[0]
            self.cycle += 1
        elif self.cycle == 1:
            Cycle = moves[1]
            self.cycle += 1
        else:
            Cycle = moves[2]
            self.cycle += 1
        return (Cycle)


class HumanPlayer(Player):
    def move(self):
        while True:
            Human = input("Please pick one of this options:[ rock | paper |\
 scissors ]--> ")
            Human = Human.lower()
            if Human not in moves:
                print("Oops! The value you entered is not valid. Try again..")
                continue
            else:
                return (Human)


class RepeatPlayer(Player):
    def move(self):
        return 'rock'


class Game():

    def __init__(self, p2):
        self.p1 = HumanPlayer()
        self.p2 = p2

    def play_game(self):

        print("------- GAME START! -------")
        rounds = 3
        for round in range(rounds):
            roundd = round
            roundd += 1
            print(" ROUND\n", roundd,)
            self.play_round()
        if self.p1.score > self.p2.score:
            print('------- YOU WON IN THIS GAME ------- ')
        elif self.p1.score < self.p2.score:
            print('------- COMPUTER WON IN THIS GAME ------- ')
        else:
            print("------- IT'S A TIE -------")
        print('Final score  ' + str(self.p1.score)+' to ' + str(self.p2.score))

    def play_singleRou(self):

        print("------- GAME START! -------")
        print("--- The game only one round ---")
        self.play_round()
        if self.p1.score > self.p2.score:
            print('------- YOU WON IN THIS GAME ------- ')
        elif self.p1.score < self.p2.score:
            print('------- COMPUTER WON IN THIS GAME ------- ')
        else:
            print("------- IT'S A TIE -------")
        print('Final score  ' + str(self.p1.score)+' to ' + str(self.p2.score))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        Game.play(move1, move2)
        self.p1.learn(move2)
        self.p2.learn(move1)

    def play(self, move1, move2):
            print(f"You chose --> | {move1} |")
            print(f"Computer chose --> | {move2} |")
            if beats(move1, move2):
                print("------- YOU WINS IN THIS ROUND -------")
                self.p1.score += 1
                print("The Score| You  " + str(self.p1.score)+" \
                Computer  " + str(self.p2.score))
                return 1
            elif beats(move2, move1):
                print("------- COMPUTER WINS IN THIS ROUND -------")
                self.p2.score += 1
                print("The Score| You  " + str(self.p1.score)+" \
                    Computer  " + str(self.p2.score))
                return 2
            else:
                print("------- IT'S A TIE -------")
                print("The Score| You  " + str(self.p1.score)+" \
                    Computer  " + str(self.p2.score))
                return 0


def beats(one, two):
    return ((one == 'rock' and two == 'scissors')
            or(one == 'scissors' and two == 'paper')
            or(one == 'paper' and two == 'rock'))


if __name__ == '__main__':
    print("\nRepeat: A player that always plays 'rock'.\nRandom: A player that\
    chooses its moves randomly.\nCycle: A player that cycles through the three\
    moves\nReflect: A player that remembers and imitates what the human player\
    did in the previous round.\n\n")
    while True:
        p2 = input('Now you can choose by writing one of these opponent mode:\
        \n[ Repeat | Random | Cycle | Reflect ] --> ')
        p2 = p2.lower()
        opponentMode = ['repeat', 'random', 'cycle', 'reflect']
        if p2 in opponentMode:
                if p2 == 'repeat':
                    p2 = RepeatPlayer()
                elif p2 == 'random':
                    p2 = RandomPlayer()
                elif p2 == 'cycle':
                    p2 = CyclePlayer()
                elif p2 == 'reflect':
                    p2 = ReflectPlayer()
                break
        else:
            print("Oops! The value you entered is not valid. Try again..")

    Game = Game(p2)
    while True:
        typeGame = input("\nNow you can choose type game by writing:\
         \n[ Single | Full] (Hint: Single: One round, Full:\
three rounds ) --> ")
        typeGame = typeGame.lower()
        typeGameList = ['full', 'single']
        if typeGame in typeGameList:
            if typeGame == 'full':
                Game.play_game()
            elif typeGame == 'single':
                Game.play_singleRou()
            break
        else:
            print("Oops! The value you entered is not valid. Try again..")
