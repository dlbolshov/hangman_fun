import tkinter as tk
import random


class Hangman:

    root = tk.Tk()
    root.config(bg='#b3e59f')
    root.title('Hangman')
    root.geometry('400x400+500+100')
    root.resizable(False, False)
    root.grid_columnconfigure(0, minsize=200)
    root.grid_columnconfigure(1, minsize=200)
    root.grid_rowconfigure(0, minsize=70)
    root.grid_rowconfigure(1, minsize=150)
    root.grid_rowconfigure(2, minsize=25)
    root.grid_rowconfigure(3, minsize=50)
    root.grid_rowconfigure(4, minsize=30)

    firework = [
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
    word_list = ['action', 'activity', 'age', 'air', 'animal', 'area',
                 'authority', 'bank', 'body', 'book', 'building', 'business',
                 'car', 'case', 'centre', 'century', 'change', 'child',
                 'city', 'community', 'company', 'condition', 'control',
                 'country', 'course', 'court', 'day', 'decision', 'door',
                 'education', 'effect', 'end', 'example', 'eye', 'face', 'fact',
                 'family', 'father', 'field', 'figure', 'flat', 'food', 'form',
                 'friend', 'game', 'girl', 'group', 'guy', 'hand', 'head',
                 'health', 'history', 'home', 'hour', 'house', 'idea', 'industry',
                 'interest', 'job', 'kid', 'kind', 'language', 'law', 'level',
                 'life', 'line', 'love', 'man', 'manager', 'manner', 'market',
                 'million', 'mind', 'minute', 'moment', 'money', 'month',
                 'morning', 'mother', 'name', 'night', 'number', 'office',
                 'order', 'paper', 'parent', 'part', 'party', 'people', 'period',
                 'person', 'place', 'plan', 'point', 'police', 'policy',
                 'position', 'power', 'president', 'price', 'problem', 'process',
                 'programme', 'project', 'quality', 'question', 'reason', 'report',
                 'research', 'rest', 'result', 'road', 'room', 'school', 'sense',
                 'service', 'side', 'society', 'staff', 'story', 'street', 'student',
                 'system', 'table', 'teacher', 'team', 'term', 'thing', 'time', 'type',
                 'view', 'war', 'water', 'way', 'week', 'woman', 'word', 'work', 'world', 'year']
    comp_point = 0
    user_point = 0

    def __init__(self) -> None:
        self.word = self.__get_word()
        # строка для подстановки букв
        self.word_completion = '_' * len(self.word)
        self.guessed_letters = []                    # список уже названных букв
        self.guessed_words = []                      # список уже названных слов
        self.tries = 6                               # кол-во доступных попыток
        self.label_tit = tk.Label(Hangman.root, text='Let\'s play hangman!\nEnter a letter or a word',
                                  bg='#b3e59f',
                                  fg='black',
                                  font=('Monaco', 20, 'bold'),
                                  )

        self.label_hang = tk.Label(Hangman.root, text=self.__display_hangman(self.tries),
                                   font=('Monaco', 25, 'bold'),
                                   bg='#b3e59f',
                                   justify=tk.LEFT,
                                   width=8,
                                   height=6,
                                   anchor='w',
                                   padx=40
                                   )

        self.label_word = tk.Label(Hangman.root, text=self.word_completion,
                                   bg='#b3e59f',
                                   fg='black',
                                   font=('Monaco', 30, 'bold'),
                                   )

        self.inp = tk.Entry(Hangman.root,
                            font=('Monaco', 30, 'bold'),
                            width=len(self.word),
                            bg='#b3e59f',
                            )
        self.inp.bind("<Key>", self.__enter_event)

        self.label_desc = tk.Label(Hangman.root, text='↑enter a letter\n or a word',
                                   bg='#b3e59f',
                                   fg='black',
                                   font=('Monaco', 15),
                                   justify=tk.LEFT
                                   )

        self.label_score = tk.Label(Hangman.root, text=f'My score: {Hangman.comp_point}\t\tYour score: {Hangman.user_point}',
                                    bg='#b3e59f',
                                    fg='black',
                                    font=('Monaco', 15),
                                    )

    def __get_word(self):
        return random.choice(Hangman.word_list).upper()

    def __display_hangman(self, tries):
        return Hangman.stages[tries]

    def __create_widgets(self):
        self.label_tit.grid(row=0, column=0, columnspan=2, stick='we')
        self.label_hang.grid(row=1, column=0, rowspan=3, stick='nsew')
        self.label_word.grid(row=1, column=1, stick='w')
        self.inp.grid(row=2, column=1, stick='wn')
        self.label_desc.grid(row=3, column=1, stick='w')
        self.label_score.grid(row=4, column=0, sticky='s',
                              columnspan=2, pady=40)

    def start(self):
        self.__create_widgets()
        Hangman.root.mainloop()

    def __play(self):
        char = self.inp.get().upper()
        self.inp.delete(0, tk.END)
        if self.tries == 0:
            self.label_tit['text'] = f'The word was {self.word}\nThis is the end'
        elif not char.isalpha() or (len(char) != 1 and len(char) != len(self.word)):
            self.label_tit['text'] = 'You made a mistake (wrong input)\n try again'
        elif char in self.guessed_letters or char in self.guessed_words:
            if self.tries > 1:
                self.label_tit['text'] = f'Already was ;)\nYou have {self.tries} tries more)'
            if self.tries == 1:
                self.label_tit['text'] = 'Already was ;)\nLast try, use it wisely)'
        elif len(char) == len(self.word):
            if char == self.word:
                self.label_tit['text'] = 'You are goddamn right!\nIt\'s a  word!'
                self.label_word['text'] = self.word
                Hangman.user_point += 1
                tk.Tk.after(self.root, 2000, self.__celebrate)
            else:
                self.guessed_words.append(char)
                self.tries -= 1
                if self.tries > 1:
                    self.label_tit['text'] = f'Oops, sorry, but no.\nYou have {self.tries} tries more)'
                if self.tries == 1:
                    self.label_tit['text'] = 'Oops, sorry, but no.\nLast try, use it wisely)'
                if self.tries == 0:
                    self.label_tit['text'] = f'The word was {self.word}\nThis is the end'
                    Hangman.comp_point += 1
                    tk.Tk.after(self.root, 2000, self.__score_show)
                self.label_hang['text'] = self.__display_hangman(self.tries)
        else:
            self.guessed_letters.append(char)
            if char in self.word:
                new_completion = ''
                for i, x in enumerate(self.word_completion):
                    if self.word[i] == char:
                        new_completion += char
                    else:
                        new_completion += x
                self.word_completion = new_completion
                if self.word_completion == self.word:
                    self.label_tit['text'] = 'You are goddamn right!\nIt\'s a  word!'
                    self.label_word['text'] = self.word
                    Hangman.user_point += 1
                    tk.Tk.after(self.root, 2000, self.__celebrate)
                else:
                    if self.tries > 1:
                        self.label_tit[
                            'text'] = f'Yes, this letter is in word!\nYou have {self.tries} tries more)'
                    if self.tries == 1:
                        self.label_tit['text'] = 'Yes, this letter is in word!\nLast try, use it wisely)'
                    self.label_word['text'] = self.word_completion
            else:
                self.tries -= 1
                if self.tries > 1:
                    self.label_tit['text'] = f'Oops, sorry, but no.\nYou have {self.tries} tries more)'
                if self.tries == 1:
                    self.label_tit['text'] = 'Oops, sorry, but no.\nLast try, use it wisely)'
                if self.tries == 0:
                    self.label_tit['text'] = f'The word was {self.word}\nThis is the end'
                    Hangman.comp_point += 1
                    tk.Tk.after(self.root, 2000, self.__score_show)
                self.label_hang['text'] = self.__display_hangman(self.tries)

    def __enter_event(self, event):
        if event.keysym == 'Return':
            self.__play()

    def __celebrate(self):
        for child in self.root.winfo_children():
            child.destroy()
        label_fire = tk.Label(self.root, text=self.firework[7],
                              font=('Monaco', 20, 'bold'),
                              bg='#b3e59f',
                              justify=tk.LEFT,
                              anchor='w',
                              padx=40,
                              pady=100
                              )
        label_fire.pack()
        tk.Tk.after(self.root, 500, lambda: label_fire.configure(
            text=self.firework[6]))
        tk.Tk.after(self.root, 1000, lambda: label_fire.configure(
            text=self.firework[5]))
        tk.Tk.after(self.root, 1500, lambda: label_fire.configure(
            text=self.firework[4]))
        tk.Tk.after(self.root, 2000, lambda: label_fire.configure(
            text=self.firework[3]))
        tk.Tk.after(self.root, 2500, lambda: label_fire.configure(
            text=self.firework[2]))
        tk.Tk.after(self.root, 3000, lambda: label_fire.configure(
            text=self.firework[1]))
        tk.Tk.after(self.root, 3500, lambda: label_fire.configure(
            text=self.firework[0]))
        tk.Tk.after(self.root, 5000, self.__score_show)

    def __score_show(self):
        for child in self.root.winfo_children():
            child.destroy()
        if Hangman.user_point == Hangman.comp_point:
            text = 'It\'s a tie now'
        if Hangman.user_point > Hangman.comp_point:
            text = 'You are winnig now,\naren\'t you?)'
        if Hangman.user_point < Hangman.comp_point:
            text = 'I\'m still winnig!'
        label_1 = tk.Label(self.root, text=text,
                           font=('Monaco', 25, 'bold'),
                           bg='#b3e59f',
                           justify=tk.CENTER,
                           anchor='w',
                           pady=20
                           )

        label_2 = tk.Label(self.root, text='Our score:',
                           font=('Monaco', 25, 'bold'),
                           bg='#b3e59f',
                           justify=tk.CENTER,
                           anchor='w',
                           pady=20
                           )

        label_3 = tk.Label(self.root, text=f'Me: {Hangman.comp_point}\tYou: {Hangman.user_point}',
                           font=('Monaco', 25, 'bold'),
                           bg='#b3e59f',
                           justify=tk.CENTER,
                           anchor='w'
                           )

        label_4 = tk.Label(self.root, text='Do you want to play again?',
                           font=('Monaco', 23, 'bold'),
                           bg='#b3e59f',
                           justify=tk.LEFT,
                           anchor='s',
                           pady=20
                           )

        but1 = tk.Button(self.root, text='Yes',
                         fg='black',
                         font=('Monaco', 30),
                         padx=20,
                         command=self.__reload
                         )

        but2 = tk.Button(self.root, text='No',
                         fg='black',
                         font=('Monaco', 30),
                         padx=20,
                         command=self.__exit
                         )

        label_1.pack(side=tk.TOP)
        label_2.pack(side=tk.TOP)
        label_3.pack(side=tk.TOP)
        label_4.pack(side=tk.TOP)
        but1.pack(side=tk.LEFT, padx=40)
        but2.pack(side=tk.RIGHT, padx=40)

    def __reload(self):
        for child in self.root.winfo_children():
            child.destroy()
        self.__init__()
        self.__create_widgets()

    def __exit(self):
        for child in self.root.winfo_children():
            child.destroy()
        if Hangman.user_point == Hangman.comp_point:
            text = 'Thank you for playing!\nYou are good competitor.'
        if Hangman.user_point > Hangman.comp_point:
            text = 'Thank you for playing!\nYou are just awesome!'
        if Hangman.user_point < Hangman.comp_point:
            text = 'Thank you for playing!\nSee you next time!'
        label_1 = tk.Label(self.root, text=text,
                           font=('Monaco', 25, 'bold'),
                           bg='#b3e59f',
                           justify=tk.CENTER,
                           anchor='w',
                           pady=40
                           )

        label_2 = tk.Label(self.root, text='☺',
                           font=('Courier new', 200),
                           bg='#b3e59f',
                           justify=tk.CENTER,
                           anchor='w',
                           pady=40
                           )

        label_1.pack()
        label_2.pack()
        tk.Tk.after(self.root, 3000, self.root.destroy)


if __name__ == '__main__':
    game = Hangman()
    game.start()
