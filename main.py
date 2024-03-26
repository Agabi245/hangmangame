from random import choice


class Hangman:
    def __init__(self):
        self.pics = ['', ''''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

   +---+
   |   |
   O   |
       |
       |
       |
=========''', '''

   +---+
   |   |
   O   |
   |   |
       |
       |
=========''', '''

   +---+
   |   |
   O   |
  /|   |
       |
       |
=========''', '''

   +---+
   |   |
   O   |
  /|\\  |
       |
       |
=========''', '''

   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
=========''', '''

   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
=========''']


class WordLoader:
    def __init__(self, file_name):
        self.file_name = file_name

    def load(self):
        with open(self.file_name, 'r') as f:
            return choice(f.readlines()).strip()


class HangmanGame:
    def __init__(self, hangman, word_loader):
        self.hangman = hangman
        self.word_loader = word_loader
        self.secret_word = word_loader.load()

    @staticmethod
    def is_russian_letter(letter):
        return len(letter) == 1 and letter.isalpha() and 'а' <= letter.lower() <= 'я'

    def play(self):
        choose_word = ['_' for _ in self.secret_word]
        counter = 0
        letters_not_in_word = []
        while '_' in choose_word:
            letter = input('Enter a letter: ')
            if self.is_russian_letter(letter):
                if letter in self.secret_word:
                    for i in range(len(self.secret_word)):
                        if self.secret_word[i] == letter:
                            choose_word[i] = letter
                else:
                    if letter not in letters_not_in_word:
                        letters_not_in_word.append(letter)
                        counter += 1
                try:
                    print(self.hangman.pics[counter])
                    print(''.join(choose_word))
                    print(f'Использованные буквы: {', '.join(sorted(letters_not_in_word))}')
                except IndexError:
                    return f"Вы проиграли\nСекретным словом было {self.secret_word}"
            else:
                print("Введите только букву на кириллице в нижнем регистре")
        return f"Вы выиграли\nСекретным словом было {self.secret_word}"


hangmangame = Hangman()
word_downloader = WordLoader('words.txt')
game = HangmanGame(hangmangame, word_downloader)
print(game.play())
