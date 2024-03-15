import random

class Crossword:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[' ']*width for _ in range(height)]
        self.words = []

    def add_word(self, word):
        word = word.upper()
        if len(word) > max(self.height, self.width):
            print(f"Word '{word}' is too long to fit in the grid.")
            return

        self.words.append(word)
        placed = False

        while not placed:
            direction = random.choice(['across', 'down'])
            x = random.randint(0, self.width - len(word)) if direction == 'across' else random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1) if direction == 'across' else random.randint(0, self.height - len(word))
            dx, dy = (1, 0) if direction == 'across' else (0, 1)
            if self.check_fit(word, x, y, dx, dy):
                self.place_word(word, x, y, dx, dy)
                placed = True

    def check_fit(self, word, x, y, dx, dy):
        for i, char in enumerate(word):
            if self.grid[y + i*dy][x + i*dx] not in [' ', char]:
                return False
        return True

    def place_word(self, word, x, y, dx, dy):
        for i, char in enumerate(word):
            self.grid[y + i*dy][x + i*dx] = char

    def display(self):
        for row in self.grid:
            print(' '.join(row))


def main():
    crossword = Crossword(12, 12)
    words = ["PYTHON", "ALGORITHM", "PROGRAMMING", "COMPUTER", "LANGUAGE"]
    for word in words:
        crossword.add_word(word)

    crossword.display()


if __name__ == "__main__":
    main()
