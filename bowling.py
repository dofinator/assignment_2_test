class Game(object):

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def total_points(self):
        points = 0
        spin_index = 0
        for _ in range(10):
            if self._is_strike(spin_index):
                points += 10 + self.rolls[spin_index+1] + self.rolls[spin_index+2]
                spin_index += 1
            elif self._is_spare(spin_index):
                points += 10 + self.rolls[spin_index+2]
                spin_index += 2
            else:
                points += self.rolls[spin_index] + self.rolls[spin_index+1]
                spin_index += 2
        return points

    def _is_spare(self, spin_index):
        return self.rolls[spin_index] + self.rolls[spin_index+1] == 10

    def _is_strike(self, spin_index):
        return self.rolls[spin_index] == 10