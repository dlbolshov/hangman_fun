""" Hangman game, one launch - one cycle for one user, but with any ammount of iterations."""
import random
import time

word_list = ['action', 'activity', 'age', 'air', 'animal', 'area', 'authority',
             'bank', 'body', 'book', 'building', 'business', 'car', 'case', 'centre', 'century',
             'change', 'child', 'city', 'community', 'company', 'condition', 'control', 'country',
             'course', 'court', 'day', 'decision', 'development', 'door', 'education', 'effect',
             'end', 'example', 'experience', 'eye', 'face', 'fact', 'family', 'father', 'field',
             'figure', 'flat', 'food', 'form', 'friend', 'game', 'girl', 'government', 'group',
             'guy', 'hand', 'head', 'health', 'history', 'home', 'hour', 'house', 'idea',
             'industry', 'information', 'interest', 'job', 'kid', 'kind', 'language', 'law',
             'level', 'life', 'line', 'love', 'man', 'manager', 'manner', 'market', 'million',
             'mind', 'minute', 'moment', 'money', 'month', 'morning', 'mother', 'name',
             'night', 'number', 'office', 'opportunity', 'order', 'paper', 'parent', 'part',
             'party', 'people', 'period', 'person', 'place', 'plan', 'point', 'police', 'policy',
             'position', 'power', 'president', 'price', 'problem', 'process', 'programme',
             'project', 'quality', 'question', 'reason', 'relationship', 'report', 'research',
             'rest', 'result', 'road', 'room', 'school', 'sense', 'service', 'side', 'society',
             'staff', 'story', 'street', 'student', 'system', 'table',
             'teacher', 'team', 'term', 'thing', 'time', 'type', 'view', 'war', 'water',
             'way', 'week', 'woman', 'word', 'work', 'world', 'year']

guessed = False 

def display_hangman(tries):
    """Return stages of hang depend on tries"""
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ ⎞
                   |    
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ 
                   |
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |
                   |
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼
                   |
                   |
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      ▼
                   |
                   |
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def print_fireworks():
    """Print victorious animation"""
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                          \\   /
                        \\\\˚˚|˚˚//
                      \\\\\\˚˚˚|˚˚˚///
                       //˚˚˚|˚˚˚\\\\
                         / ˚ ˚ \\
                              
                             
                             
                             
                             
                             
                ____________|______________
                ''',
                # голова, торс, обе руки, одна нога
                '''
                               
                          \\˚ ˚/
                        \\\\˚˚|˚˚//
                        //˚˚|˚˚\\\\
                         / ˚ ˚ \\
                              
                             
                             
                             
                             
                             
                ____________|______________
                ''',
                # голова, торс, обе руки
                '''
                               
                          \\   /
                         \\˚˚|˚˚/
                         /˚˚|˚˚\\
                           ˚ ˚  
                              
                             
                             
                             
                             
                             
                ____________|______________
                ''',
                # голова, торс и одна рука
                '''
                               
                             
                          \\˚ ˚/
                          /˚|˚\\
                            |  
                              
                             
                             
                             
                             
                             
                ____________|______________
                ''',
                # голова и торс
                '''
                               
                             
                          
                           ˚O˚
                           ˚|˚
                            | 
                            |
                             
                             
                             
                             
                ____________|______________
                ''',
                # голова
                '''
                               
                             
                          
                            
                            
                            O 
                           /|\\
                            |
                            |
                            |
                            |
                ____________|______________
                ''',
                # начальное состояние
                '''
                               
                             
                          
                            
                            
                              
                            
                             
                            O 
                           /|\\
                            |
                ____________|______________
                ''',
                '''
                               
                             
                          
                            
                            
                              
                            
                             
                              
                            
                            O                           
                ____________|______________
                '''
    ]
    for i in stages[::-1]:
        print(i, flush=True)
        time.sleep(1)


def get_word():
    """Choose random word from word_list"""
    return random.choice(word_list)


def play(_word):
    """Realise main logic of game for one word (one iteration)"""
    global guessed
    guessed = False                    # сигнальная метка    
    word = _word.upper()
    # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion = '_' * len(word)
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток

    print('Let\'s play hangman!\n')
    print(display_hangman(tries))
    print(word_completion)

    while True:
        if tries == 0:
            print(f'The word was {word}')
            print('This is the end, ', end='')
            time.sleep(0.3)
            for i in 'poor hangman':
                print(i, flush=True, end='')
                time.sleep(0.3)
            for i in range(random.randint(4, 8)):
                print('.', flush=True, end='')
                time.sleep(0.5)
            print('.', flush=True)
            guessed = False
            break

        char = input('Enter a letter or a word:\n').upper()

        if not char.isalpha():  # or len(char) != 1 or len(char) != len(word):
            print('You made a mistake (wrong input), try again\n')
            print(display_hangman(tries))
            print(word_completion)
            continue
        if char in guessed_letters or char in guessed_words:
            print('Already was ;)')
            if tries > 1:
                print(f'You have {tries} tries more)')
            if tries == 1:
                print('It\'s your last try, use it wisely)')
            print(display_hangman(tries))
            print(word_completion)
            continue
        if len(char) == len(word):
            if char == word:
                guessed = True
                print('You are goddamn right! It\'s a  word!\n')
                print(display_hangman(tries))
                print(word)
                print()
                time.sleep(3)
                print_fireworks()
                time.sleep(3)
                break
            else:
                guessed_words.append(char)
                tries -= 1
                print('Oops, sorry, but no.')
                if tries > 1:
                    print(f'You have {tries} tries more)')
                if tries == 1:
                    print('It\'s your last try, use it wisely)')
                print(display_hangman(tries))
                print(word_completion)
                continue

        guessed_letters.append(char)
        if char in word:
            new_competion = ''
            for i, x in enumerate(word_completion):
                if word[i] == char:
                    new_competion += char
                else:
                    new_competion += x
            word_completion = new_competion
            if word_completion == word:
                guessed = True
                print('You are goddamn right! That\'s it!\n')
                print(display_hangman(tries))
                print(word)
                print()
                time.sleep(3)
                print_fireworks()
                time.sleep(3)
                break
            print('Yes, this letter is in word!')
            if tries > 1:
                print(f'You have {tries} tries more)')
            if tries == 1:
                print('It\'s your last try, use it wisely)')
            print(display_hangman(tries))
            print(word_completion)
        else:
            tries -= 1
            print('Oops, sorry, but no.')
            if tries > 1:
                print(f'You have {tries} tries more)')
            if tries == 1:
                print('It\'s your last try, use it wisely)')
            print(display_hangman(tries))
            print(word_completion)

play(get_word())
# score = guessed  # False if user loose, True if user wins
user_point = 0
comp_point = 0
flag = True

while True:
    if guessed and flag:
        user_point += 1
    if not guessed and flag:
        comp_point += 1
    flag = False
    print('Our score:\n')
    print(f'Me - {comp_point}\n')
    print(f'You - {user_point}\n')
    if user_point == comp_point:
        print('It\'s a tie now')
    if user_point > comp_point:
        print('You are winnig now, aren\'t you?)')
    if user_point < comp_point:
        print('I\'m still winnig!')
    print('\nDo you want to play again?')
    print('\n'*3)
    quest = input('Enter "Y"/"N": ')
    if quest.lower() == 'y':
        flag = True
        play(get_word())
    if quest.lower() == 'n':
        break

print('\n'*6)
if user_point == comp_point:
    print('Thank you for playing! You are good competitor.')
if user_point > comp_point:
    print('Thank you for playing! You are just awesome!')
if user_point < comp_point:
    print('Thank you for playing! See you next time!')
print('\n'*6)
