# necessary imports
import time
import random
import numpy as np
import pandas as pd

# shhhhhhh
import warnings
warnings.filterwarnings('ignore', category=pd.errors.SettingWithCopyWarning)

CARDS = pd.read_csv('tarot.csv')

# thank you Claude
TAROT_CARDS = {
    "The Fool": """ _______________
|               |
|   THE FOOL    |
|      0        |
|               |
|    o/        |
|    /|   ☼    |
|    / \\       |
|   ~cliff~    |
|_______________|""",
    
    "The Magician": """ _______________
|               |
| THE MAGICIAN  |
|      I        |
|      ∞        |
|     \\o/       |
|      |        |
| ⚄ ⚆ ⚅ ⚈      |
|_______________|""",
    
    "The High Priestess": """ _______________
|               |
|HIGH PRIESTESS |
|      II       |
|   ☽  ☉  ☾    |
|      ♀        |
|     /|\\       |
|    / | \\      |
|_______________|""",
    
    "The Empress": """ _______________
|               |
| THE EMPRESS   |
|     III       |
|    ♀ ♀ ♀     |
|     \\o/       |
|   ❀ /|\\ ❀    |
|    / | \\      |
|_______________|""",
    
    "The Emperor": """ _______________
|               |
| THE EMPEROR   |
|      IV       |
|     ♂ ♂ ♂    |
|    [===]      |
|     \\o/       |
|      |        |
|_______________|""",

    # accounting for my own typo
    "The Heirophant": """ _______________
|               |
|THE HIEROPHANT |
|      V        |
|      ✚        |
|     \\o/       |
|   ⌂  |  ⌂    |
|     / \\       |
|_______________|""",
    
    "The Lovers": """ _______________
|               |
|  THE LOVERS   |
|      VI       |
|      ☼        |
|    o   o      |
|   /|\\ /|\\     |
|   / \\ / \\     |
|_______________|""",
    
    "The Chariot": """ _______________
|               |
| THE CHARIOT   |
|     VII       |
|     \\o/       |
|    ==|==      |
|   [=====]     |
|   ◐    ◑     |
|_______________|""",
    
    "Strength": """ _______________
|               |
|   STRENGTH    |
|     VIII      |
|      ∞        |
|    o ʕ•ᴥ•ʔ   |
|   /|\\/  |     |
|   / \\   |     |
|_______________|""",
    
    "The Hermit": """ _______________
|               |
|  THE HERMIT   |
|      IX       |
|      ☆        |
|     /o        |
|     /|        |
|     / \\       |
|   ^^^^        |
|_______________|""",
    
    "Wheel of Fortune": """ _______________
|               |
|WHEEL FORTUNE  |
|      X        |
|    ╔═══╗      |
|    ║ ☯ ║      |
|    ╚═══╝      |
|   ↻     ↺     |
|_______________|""",
    
    "Justice": """ _______________
|               |
|   JUSTICE     |
|      XI       |
|     ⚖️         |
|     \\o/       |
|      |        |
|     / \\       |
|_______________|""",
    
    "The Hanged Man": """ _______________
|               |
|HANGED MAN     |
|     XII       |
|   _____       |
|   |   |       |
|   |  o/       |
|   | /|        |
|_______________|""",
    
    "Death": """ _______________
|               |
|    DEATH      |
|     XIII      |
|     ☠️         |
|    /||\\       |
|   / || \\      |
|     ||        |
|_______________|""",
    
    "Temperance": """ _______________
|               |
| TEMPERANCE    |
|     XIV       |
|      ∆        |
|    \\o/        |
|   ⚱ | ⚱      |
|    / \\        |
|_______________|""",
    
    "The Devil": """ _______________
|               |
|  THE DEVIL    |
|      XV       |
|     ⸸ ⸸      |
|     ψo_       |
|    </|\\>      |
|     / \\       |
|_______________|""",
    
    "The Tower": """ _______________
|               |
|  THE TOWER    |
|     XVI       |
|     ☇|☇       |
|      |█       |
|      |█       |
|    __|█__     |
|_______________|""",
    
    "The Star": """ _______________
|               |
|   THE STAR    |
|     XVII      |
|   ✦ ★ ✦      |
|    ✦ ✦ ✦     |
|     \\o/       |
|   ≈≈ | ≈≈    |
|_______________|""",
    
    "The Moon": """ _______________
|               |
|   THE MOON    |
|    XVIII      |
|      ☾        |
|    ʕ•ᴥ•ʔ ∪    |
|   ~~~|~~~     |
|      |        |
|_______________|""",
    
    "The Sun": """ _______________
|               |
|   THE SUN     |
|     XIX       |
|    \\  ☉  /    |
|   ― ― ― ―    |
|    \\o/ ☼      |
|     |         |
|_______________|""",
    
    "Judgement": """ _______________
|               |
|  JUDGEMENT    |
|      XX       |
|     🎺         |
|    \\o/\\o/     |
|     | /|      |
|   _/ \\_/ \\    |
|_______________|""",
    
    "The World": """ _______________
|               |
|  THE WORLD    |
|     XXI       |
|   ╔═════╗     |
|   ║ \\o/ ║     |
|   ║  |  ║     |
|   ╚═════╝     |
|_______________|""",
    
    # WANDS
    "Ace of Wands": """ _______________
|               |
| ACE of WANDS  |
|               |
|      |        |
|     |||       |
|      |        |
|    ♣♣♣♣       |
|_______________|""",
    
    "Two of Wands": """ _______________
|               |
| TWO of WANDS  |
|               |
|     | |       |
|    || ||      |
|     | |       |
|   ♣♣ ♣♣       |
|_______________|""",
    
    "Three of Wands": """ _______________
|               |
|THREE of WANDS |
|               |
|    | | |      |
|   || || ||    |
|    | | |      |
|   ♣♣ ♣♣ ♣♣    |
|_______________|""",
    
    "Four of Wands": """ _______________
|               |
|FOUR of WANDS  |
|  _________    |
|  | | | | |    |
|  | | | | |    |
|  | | | | |    |
| ♣♣ ♣♣ ♣♣ ♣♣   |
|_______________|""",
    
    "Five of Wands": """ _______________
|               |
|FIVE of WANDS  |
|   | | | | |   |
|   X X X X X   |
|   | | | | |   |
|  ♣♣♣♣♣♣♣♣♣♣   |
|_______________|""",
    
    "Six of Wands": """ _______________
|               |
| SIX of WANDS  |
|      ★        |
|      |        |
|   | | | | |   |
|  || |||||||| |
| ♣♣♣♣♣♣♣♣♣♣♣♣  |
|_______________|""",
    
    "Seven of Wands": """ _______________
|               |
|SEVEN of WANDS |
|      |        |
|   | | | | | | |
|   | | | | | | |
|   ♣ ♣ ♣ ♣ ♣ ♣ |
|_______________|""",
    
    "Eight of Wands": """ _______________
|               |
|EIGHT of WANDS |
| ↘ ↘ ↘ ↘      |
|   ↘ ↘ ↘ ↘    |
| | | | | | | ||
| ♣ ♣ ♣ ♣ ♣ ♣ ♣|
|_______________|""",
    
    "Nine of Wands": """ _______________
|               |
|NINE of WANDS  |
|    o | | | |  |
|   /| | | | |  |
|   /| | | | |  |
|  ♣♣♣♣♣♣♣♣♣♣   |
|_______________|""",
    
    "Ten of Wands": """ _______________
|               |
| TEN of WANDS  |
|  |||||||||||  |
|    o          |
|   /|\\         |
|   / \\         |
| ♣♣♣♣♣♣♣♣♣♣♣♣  |
|_______________|""",
    
    "Page of Wands": """ _______________
|               |
| PAGE of WANDS |
|      |        |
|     o/        |
|    /|         |
|    / \\        |
|     ♣♣        |
|_______________|""",
    
    "Knight of Wands": """ _______________
|               |
|KNIGHT of WANDS|
|      |        |
|     \\o        |
|    --|\\--     |
|   ┌─┐/ \\      |
|    ♣♣♣        |
|_______________|""",
    
    "Queen of Wands": """ _______________
|               |
|QUEEN of WANDS |
|     ♛|        |
|     \\o/       |
|    --|-       |
|     / \\       |
|      ♣♣       |
|_______________|""",
    
    "King of Wands": """ _______________
|               |
| KING of WANDS |
|     ♚|        |
|     \\o/       |
|    ==|==      |
|     / \\       |
|      ♣♣       |
|_______________|""",
    
    # CUPS
    "Ace of Cups": """ _______________
|               |
|  ACE of CUPS  |
|               |
|      ✺        |
|     ╱ ╲       |
|    |   |      |
|     \\_/       |
|_______________|""",
    
    "Two of Cups": """ _______________
|               |
|  TWO of CUPS  |
|               |
|   ╱ ╲   ╱ ╲  |
|  |   | |   |  |
|   \\_/   \\_/   |
|      ♥♥       |
|_______________|""",
    
    "Three of Cups": """ _______________
|               |
|THREE of CUPS  |
|  o   o   o    |
| /|\\ /|\\ /|\\   |
|╱╲ | ╱╲ | ╱╲  |
|\\_/ | \\_/ \\_/  |
|_______________|""",
    
    "Four of Cups": """ _______________
|               |
| FOUR of CUPS  |
|  ╱╲  ╱╲  ╱╲  |
| |  ||  ||  |  |
|  \\_/ \\_/ \\_/  |
|      o        |
|     /|\\       |
|_______________|""",
    
    "Five of Cups": """ _______________
|               |
| FIVE of CUPS  |
| ╱╲  ╱╲  ╱╲   |
| XX  XX  XX    |
|  ╱╲    ╱╲    |
| |  |  |  |    |
|  \\_/   \\_/    |
|_______________|""",
    
    "Six of Cups": """ _______________
|               |
|  SIX of CUPS  |
| ╱╲ ╱╲ ╱╲     |
||  |  ||  |    |
| \\_/\\_/\\_/     |
| ╱╲ ╱╲ ╱╲     |
||  |  ||  |    |
|_______________|""",
    
    "Seven of Cups": """ _______________
|               |
|SEVEN of CUPS  |
|     ╱╲        |
| ╱╲ |  | ╱╲   |
||  | \\_/|  |   |
| \\_/ ╱╲ \\_/   |
|    |  | ☁    |
|_______________|""",
    
    "Eight of Cups": """ _______________
|               |
|EIGHT of CUPS  |
| ╱╲ ╱╲ ╱╲ ╱╲ |
||  |  ||  ||  ||
| \\_/\\_/\\_/\\_/  |
|      o/       |
|     /|   ☾    |
|_______________|""",
    
    "Nine of Cups": """ _______________
|               |
| NINE of CUPS  |
| ╱╲╱╲╱╲╱╲╱╲  |
||||||||||||||  |
| \\_/\\_/\\_/\\_/  |
|      \\o/      |
|       |       |
|_______________|""",
    
    "Ten of Cups": """ _______________
|               |
|  TEN of CUPS  |
| ╱╲╱╲╱╲╱╲╱╲  |
||||||||||||||  |
| \\_/\\_/\\_/\\_/  |
|    o o  ♥♥    |
|   /|\\/|\\      |
|_______________|""",
    
    "Page of Cups": """ _______________
|               |
| PAGE of CUPS  |
|     ╱╲        |
|    | 🐟|       |
|     \\_/       |
|      o        |
|     /|\\       |
|_______________|""",
    
    "Knight of Cups": """ _______________
|               |
|KNIGHT of CUPS |
|      ╱╲       |
|     |  |      |
|     \\o/       |
|   ┌─┐|        |
|    / \\        |
|_______________|""",
    
    "Queen of Cups": """ _______________
|               |
| QUEEN of CUPS |
|     ╱╲♛       |
|    |  |       |
|     \\_/       |
|     \\o/       |
|      |        |
|_______________|""",
    
    "King of Cups": """ _______________
|               |
| KING of CUPS  |
|     ╱╲♚       |
|    |  |       |
|     \\_/       |
|     \\o/       |
|    ==|==      |
|_______________|""",
    
    # SWORDS
    "Ace of Swords": """ _______________
|               |
| ACE of SWORDS |
|       †       |
|       ‡       |
|       |       |
|       |       |
|      ♔        |
|_______________|""",
    
    "Two of Swords": """ _______________
|               |
| TWO of SWORDS |
|     \\ X /     |
|      \\o/      |
|     ⚔ ⚔      |
|               |
|      ☾        |
|_______________|""",
    
    "Three of Swords": """ _______________
|               |
|THREE of SWORDS|
|      †        |
|    † ♥ †      |
|      †        |
|               |
|     ☁ ☁      |
|_______________|""",
    
    "Four of Swords": """ _______________
|               |
|FOUR of SWORDS |
|      †        |
|  † _____ †    |
|   |  o  |     |
|   | /|\\ |     |
|      †        |
|_______________|""",
    
    "Five of Swords": """ _______________
|               |
|FIVE of SWORDS |
|   † † †       |
|     \\o        |
|      |\\       |
|     / \\       |
|   ⚔  ⚔       |
|_______________|""",
    
    "Six of Swords": """ _______________
|               |
| SIX of SWORDS |
| † † †         |
|   o  o        |
|  /█████\\      |
| ≈≈≈≈≈≈≈≈≈     |
| † † †         |
|_______________|""",
    
    "Seven of Swords": """ _______________
|               |
|SEVEN of SWORDS|
| † † † † †     |
|      o/       |
|    ⚔/|\\⚔     |
|     / \\       |
|      † †      |
|_______________|""",
    
    "Eight of Swords": """ _______________
|               |
|EIGHT of SWORDS|
|  †  †  †  †   |
|     |o|       |
|     /|\\       |
|     / \\       |
|  †  †  †  †   |
|_______________|""",
    
    "Nine of Swords": """ _______________
|               |
|NINE of SWORDS |
| † † † † † † † |
|               |
|      o        |
|    _(█)_      |
|      |        |
|_______________|""",
    
    "Ten of Swords": """ _______________
|               |
| TEN of SWORDS |
|  † † † † †    |
|   † † † † †   |
|      _o_      |
|   =========   |
|               |
|_______________|""",
    
    "Page of Swords": """ _______________
|               |
|PAGE of SWORDS |
|       †       |
|      /o       |
|      /|       |
|     / \\       |
|    ~~~~       |
|_______________|""",
    
    "Knight of Swords": """ _______________
|               |
|KNIGHT of SWORD|
|       †       |
|      \\o →     |
|    ---|\\---   |
|    ┌─┐/ \\     |
|     ⚔⚔       |
|_______________|""",
    
    "Queen of Swords": """ _______________
|               |
|QUEEN of SWORDS|
|     ♛ †       |
|      \\o/      |
|       |       |
|      / \\      |
|     ⚔⚔⚔      |
|_______________|""",
    
    "King of Swords": """ _______________
|               |
|KING of SWORDS |
|     ♚ †       |
|      \\o/      |
|     ==|==     |
|      / \\      |
|     ⚔⚔⚔      |
|_______________|""",
    
    # PENTACLES
    "Ace of Pentacles": """ _______________
|               |
|ACE of PENTACLE|
|               |
|      ✋        |
|               |
|      ⬟        |
|      ★        |
|_______________|""",
    
    "Two of Pentacles": """ _______________
|               |
|TWO of PENTACLE|
|               |
|     ⬟∞⬟       |
|      \\o/      |
|       |       |
|      / \\      |
|_______________|""",
    
    "Three of Pentacles": """ _______________
|               |
|THREE PENTACLE |
|    ⬟          |
|   ╱ ╲  o      |
|  │   │/|\\     |
|   ╲_╱ / \\     |
|  ⬟    ⬟       |
|_______________|""",
    
    "Four of Pentacles": """ _______________
|               |
|FOUR of PENTACL|
|      ⬟        |
|     \\(o)/     |
|    ⬟ | ⬟      |
|      |        |
|      ⬟        |
|_______________|""",
    
    "Five of Pentacles": """ _______________
|               |
|FIVE of PENTACL|
|    ⬟  ⬟       |
|    o   o      |
|   /|\\ /|\\     |
|   / \\ / \\     |
|      ⬟        |
|_______________|""",
    
    "Six of Pentacles": """ _______________
|               |
|SIX of PENTACLE|
|  ⬟   ⬟   ⬟   |
|      o        |
|     /|\\       |
|    / | \\      |
|  ⬟   ⬟   ⬟   |
|_______________|""",
    
    "Seven of Pentacles": """ _______________
|               |
|SEVEN PENTACLE |
|  ⬟ ⬟ ⬟        |
|   ⬟ ⬟ ⬟       |
|    ⬟  o       |
|      /|\\      |
|     / | \\     |
|_______________|""",
    
    "Eight of Pentacles": """ _______________
|               |
|EIGHT PENTACLE |
| ⬟ ⬟ ⬟ ⬟      |
|   ⬟ ⬟ ⬟      |
|      o        |
|     /|⚒       |
|     / \\       |
|_______________|""",
    
    "Nine of Pentacles": """ _______________
|               |
|NINE of PENTACL|
| ⬟ ⬟ ⬟ ⬟ ⬟    |
|   ⬟ ⬟ ⬟      |
|     \\o/🦅      |
|      |        |
|     / \\       |
|_______________|""",
    
    "Ten of Pentacles": """ _______________
|               |
|TEN of PENTACL |
|  ⬟ ⬟ ⬟ ⬟     |
| ⬟ o ⬟ o ⬟    |
|   /|\\ /|\\     |
|  ⬟ ⬟ ⬟ ⬟     |
|_______________|""",
    
    "Page of Pentacles": """ _______________
|               |
|PAGE PENTACLE  |
|               |
|      ⬟        |
|      o        |
|     /|\\       |
|     / \\       |
|_______________|""",
    
    "Knight of Pentacles": """ _______________
|               |
|KNIGHT PENTACLE|
|      ⬟        |
|     \\o        |
|   ---|\\---    |
|   ┌─┐/ \\      |
|               |
|_______________|""",
    
    "Queen of Pentacles": """ _______________
|               |
|QUEEN PENTACLE |
|     ♛ ⬟       |
|     \\o/       |
|      |        |
|     / \\       |
|    🐰         |
|_______________|""",
    
    "King of Pentacles": """ _______________
|               |
|KING of PENTACL|
|     ♚ ⬟       |
|     \\o/       |
|    ==|==      |
|     / \\       |
|    ⬟⬟⬟⬟      |
|_______________|"""
}

def calculate_valence(row):
    '''
    Helper function for block_shuffle().
    
    Assigns a numerical classification to the cards
    based on the assumed positivity of the reading.

    Used to assign a valence score after shuffling.
    '''
    # 0s are only when the cards are neutral
    if row['Valence'] == 'Neutral':
        return 0
        
    # 1 for when a card is more positive read upright
    elif row['Valence'] == 'Upright':
        return 1 if row['Orientation'] == 'Upright' else -1

    # -1 for when card is more positive read reversed
    else: # row['Valence'] == 'Reversed'
        return 1 if row['Orientation'] == 'Reversed' else -1

def block_shuffle():
    '''
    Attempting to mimic how people shuffle tarot:
    Takes 'piles' out of the deck and reverses them with a
    22.2% chance. Then randomly chooses to put the pile back
    on top or bottom of the deck and uses the Upright or 
    Reversed position to assign an orientation and calculate
    valence score.

    Reads in the unshuffled deck and returns the shuffled deck.
    '''
    # initialize the cards
    deck = CARDS.sample(frac=1).reset_index(drop=True)
    deck['Reading'] = deck['Upright']
    deck['Orientation'] = 'Upright'
    
    # do 17-42 'block shuffles'
    num_piles = random.randint(17, 42)
    
    for i in range(num_piles):
        # take out a random pile of cards
        pile_size = random.randint(5, 15)
        pile = deck[:pile_size].copy()
        rest = deck[pile_size:]
    
        # they might reverse themselves
        if random.random() < 0.222:
            pile['Reading'] = pile['Reversed']
            pile['Orientation'] = 'Reversed'
        else:
            pile['Reading'] = pile['Upright']
            pile['Orientation'] = 'Upright'
    
        # can put the cards back on top or bottom of deck
        top_or_bottom = random.choice(['top', 'bottom'])
        
        if top_or_bottom == 'top':
            deck = pd.concat([pile, rest], ignore_index=True)
        else: # == 'bottom'
            deck = pd.concat([rest, pile], ignore_index=True)

    deck['Valence'] = deck.apply(calculate_valence, axis=1)
    deck = deck.drop(['Upright', 'Reversed'], axis=1)

    # splitting the deck into thirds
    thirds = 26

    # introduce some randomness
    first_cutoff = thirds + random.randint(-7, 7)
    second_cutoff = 2 * thirds + random.randint(-7, 7)

    # split the cards
    left = deck[:first_cutoff]
    middle = deck[first_cutoff:second_cutoff]
    right = deck[second_cutoff:]

    # replacement order is random
    order = [left, middle, right]
    random.shuffle(order)

    # reorder the cards
    final_shuffle = pd.concat(order, ignore_index=True)
    
    return final_shuffle

def tarot_reading():
    '''
    Read your future!
    
    Flips over the first five cards,
    assigning them with a reading
    temporality (Past, Present, Subconscious,
    Subconscious, Future).
    Verifies if this matches Claude's assignment
    and calculates an adjustment according to 
    Claude's stated confidence level.

    Reads in the deck of cards and returns the reading.
    '''

    # shuffle / split the cards
    shuffled_cards = block_shuffle()

    # pull out the top 5
    reading = shuffled_cards.iloc[:5]

    # assign each a temporality
    five_card_spread = ['Past', 'Present', 'Subconscious', 'Subconscious', 'Future']
    reading['Temporality'] = five_card_spread

    # check if it's correct (encodes 1 if so, 0 if not)
    reading['Alignment'] = (reading['Temporality (assigned by Claude)'] == reading['Temporality']).astype(int)

    # adjust for Claude's confidence level
    error_adjustment = np.where(
        reading['Alignment'] == 1,
        1 + reading['Confidence'] / 15,  # small bonus for confident correct answers
        0 - reading['Confidence'] / 15 # penalty for wrong answers
    )
    reading['Noisy Alignment'] = reading['Alignment'] + error_adjustment
    
    # drop these columns, no longer needed
    reading = reading.drop(['Temporality (assigned by Claude)', 'Confidence'], axis=1)
    
    return reading

def read_the_cards(show_description=False):
    '''
    Uses the shuffling functions to randomly shuffle and order the deck.
    Then, uses the tarot reading function to 'read' the top five.

    Prints the display with the following logic:
        - Color of the special characters represents
        the valence of the reading (blue for a more
        negative interpretation, yellow for a more
        positive one).
        - Lights up the positions that are significant
        for the reading.
        - Reveals the cards and their interpretations
        (along with optional descriptions).

    Reads the deck and prints a reading.
    '''
    
    # read the cards!
    reading = tarot_reading()

    # setting up the display
    names = reading['Name'].tolist()
    readings = reading['Reading'].tolist()
    
    # change the display color depending on the interpretation
    interpretation = reading['Valence'].mean()
    if interpretation > 0:
        color = '\033[93m' 
    elif interpretation == 0:
        color = '\033[37m' # light grey
    else:
        color = '\033[94m'
    
    reset = '\033[0m'

    # printing display
    print(f'{color}*$*^$**(^%$*&(_^$^*&(_^$**^*@^*@*-*{reset} YOUR READING {color}*$^%$*&($$*&(_^$**^*@^%$*&(_^&(_^$**^*@*-* {reset}\n')

    print(', '.join(names).center(88))

    # match to Claude's visualizations
    visuals = []
    alignments = reading['Alignment'].tolist()
    orientations = reading['Orientation'].tolist()
    
    for name, aligned, orientation in zip(names, alignments, orientations):
        visual = TAROT_CARDS.get(name, "uh oh")
        
        # Reverse the card if it's in reversed position
        if orientation == 'Reversed':
            visual_lines = visual.split('\n')
            visual = '\n'.join(reversed(visual_lines))
        
        if aligned == 1:
            # light the card yellow
            magic_card = [f"{'\033[33m'}{line}{reset}" for line in visual.split('\n')]
            visual = '\n'.join(magic_card)
        visuals.append(visual)
    
    # Split each visual into lines for side-by-side display
    visual_lines = [visual.split('\n') for visual in visuals]
    max_lines = max(len(lines) for lines in visual_lines)
    
    # Print cards side by side
    for line_idx in range(max_lines):
        line_parts = []
        for visual in visual_lines:
            if line_idx < len(visual):
                line_parts.append(visual[line_idx])
            else:
                line_parts.append(' ' * 15)  # Empty space if card has fewer lines
        print('  '.join(line_parts))
    
    print()
    
    if show_description:
        # pass in argument to show description
        print(f'\n{color}*$*^$*^$**(^%$*&(_^$**^*@^$**(^(_^$**^*@^%$*&(_^$**^*@*-^$**^*@*^$$*^$**(^%$*&(_^$$(_^$^*@*-*{reset}\n')
        
        descriptions = reading['Description'].tolist()
        
        for card_description in descriptions:
            print(card_description.center(88))
    
    print(f'\n{color}*$*^$**(^%$*&(_^$*^*@*-**$*^$**(^$**^*%*@*^$**^%$*&(_^$**^*@^$**(^%$*(*$**(^%$**&(_^$*-**$*^{reset}\n')
    
    # light up the positions that match the card's temporality
    positions = []
    for idx, row in reading.iterrows():
        if row['Alignment'] == 1:
            # using yellow to indicate matches
            positions.append(f"{'\033[33m'}{row['Temporality']}{reset}")
        else:
            positions.append(row['Temporality'])
    
    print(', '.join(positions).center(99))
    
    print(f'\n{color}*$*^$**(^%^*@*-**$*^$**-**$*^**(^%$*&(_^$**^*@^$**(^%$*&(_^$**^*@^^$**^*@$**(^%$*&(_^$$**$*^$-*{reset}\n')
    
    for interpretation in readings:
        print(interpretation.center(88))
    
    print(f'\n{color}*$*^$**(^%$*&(_^$**^$**(^%$*&(_^$**^*@^*@*-**$^%$*&(_^$$*&(_^$**^*@^%$*&(_^$*^*^$*^*@*-**$*^$*-*{reset}')

    return reading