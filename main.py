import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = [
    "apple", "baker", "chair", "dream", "earth", "fruit", "grape", "house",
    "igloo", "jolly", "kite", "lemon", "mouse", "night", "ocean", "plant",
    "queen", "river", "smile", "table", "union", "value", "water", "xenon",
    "yacht", "zebra", "angel", "beach", "cloud", "dance", "eagle", "flame",
    "ghost", "happy", "inked", "juice", "knife", "light", "music", "north",
    "olive", "peach", "quiet", "robot", "snake", "train", "unity", "vocal",
    "wagon", "x-ray", "young", "zesty", "awake", "brave", "crane", "doubt",
    "early", "fancy", "giant", "hotel", "ivory", "jolly", "koala", "loyal",
    "melon", "novel", "opera", "proud", "quest", "ready", "sunny", "tiger",
    "under", "vivid", "worry", "xerox", "yummy", "crazy", "beard", "cabin",
    "daisy", "empty", "feast", "grass", "hello", "ideas", "jumps", "kicks",
    "lucky", "magic", "never", "owing", "party", "quick", "rusty", "sweet",
    "today", "urban", "vowel", "write", "yells", "zones", "alarm", "brick",
    "calm", "dwarf", "empty", "faint", "glove", "hairy", "irony", "jumps",
    "kneel", "latch", "minus", "nerve", "oat", "paint", "quill", "roast",
    "shade", "twist", "usher", "vest", "whisk", "yarn", "adorn", "bless",
    "climb", "ditch", "enjoy", "flock", "greet", "hatch", "inner", "joust",
    "knead", "leash", "mirth", "notch", "outer", "pouch", "quart", "round",
    "sniff", "towel", "usual", "vague", "witty", "yawn", "alert", "bloom",
    "crisp", "drill", "eager", "float", "grace", "haste", "itchy", "joint",
    "knock", "lunar", "medal", "niece", "onion", "prism", "quilt", "rebel",
    "stump", "tasty", "ultra", "vixen", "widen", "youth", "azure", "bingo",
    "cider", "dizzy", "elbow", "fable", "gavel", "hilly", "index", "jumbo",
    "kiosk", "liven", "motto", "niece", "organ", "pilot", "quack", "reach",
    "silly", "trunk", "usher", "vivid", "wedge", "yacht", "zest"
]

# You can then use this list, for example:
# for word in random_words:
#     print(word)

# Or access specific words:
# print(random_words[0]) # Output: serendipity


lives = 6

chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"


    print(display)


    if guess not in chosen_word:
        lives -= 1
    if lives == 0:
        print("You lose.")
        print(chosen_word)
        game_over = True
    if "_" not in display:
        game_over = True
        print("You win.")

 
    print(stages[lives])
