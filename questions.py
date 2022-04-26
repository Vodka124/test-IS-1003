# This takes in the random class for jumbling up the questions randomly
import random

# This sets up the class thing
class question:
    
    # This subclass initializes the quiz dictionary and some early checkers
    def __init__(self):
        self.answer = 'pie'
        self.score = 0
        self.tracker = []
        self.letter_ans = 0
        
        self.TOTAL_QUEST = {1 : {'What is the informal language, used by programmers use to\ncreate models of programs, that has no syntax rules and\nis not meant to be compiled or executed?'
                    : 'n/a', 'psuedocode' : ['flowchart','algorithm','source code','pseudocode']},
         2 : {'A(n) __________ is a diagram that graphically depicts the\nsteps that take place in a program?'
              : 'n/a', 'flowchart' : ['flowchart','algorithm','source code','pseudocode']}, 
         3 : {'The __________ function reads a piece of data that has been\nentered at the keyboard and returns that piece of data, as a\nstring, back to the program.'
              : 'n/a', 'input()' : ['input()','output()','eval_input()','str_input()']}, 
         4 : {'The line continuation character is a'
              : 'n/a', 'slash' : ['#','%','&','\\']}, 
         5 : {'Which mathematical operator is used to raise 5 to the secondpower in Python?'
              : 'n/a', '**' : ['/','**','^','~']}, 
         6 : {'In a print statement, you can set the __________ argument to\na space or empty string to stop the output from advancing to\na new line.'
              : 'n/a', 'end' : ['stop','end','separator','newLine']},
         7 : {'After the execution of the following statement, the variable\nsold will reference the numeric literal value as (n) _______\ndata type.\n\nsold = 256.752'
              : 'n/a', 'float' : ['int','float','str','currency']}, 
         8 : {'After the execution of the following statement, the variable\nprice will reference the value __________.\n\nprice = int(68.549)'
              : 'n/a', '68' : ['68','69','68.55','68.6']}, 
         9 : {'What is the output of the following statement?\n\nprint(\'I\\\'m ready to begin\')'
              : 'n/a', 'third' : ['Im ready to begin','I\\\'m ready to begin','I\'m ready to begin','\'I\\\'m ready to begin\'']}, 
         10 : {'What is the output of the following statement, given that\nvalue1 = 2.0 and value2 = 12?\n\nprint(value1 * value2)'
               : 'n/a', '24.0' : ['24','value1 * value2','24.0','2.0 * 12']}}
    
    # This sub-class resets the answer once called
    def setten(self, new_pie):
        self.answer = new_pie
    
    # This one resets a random number to be used later
    def set_rando(self):
        return random.randint(1,10)
    
    # This monster shoes the question and the answers to the user!
    # If the same question gets recognized, the number resets
    def next_contestant(self, parashut):
        if parashut in self.tracker:
            parashut = self.set_rando()
            self.pose_question(parashut)
            print(f'\n1. {self.show_choices(parashut, 0)}\n2. {self.show_choices(parashut, 1)}'
                  + f'\n3. {self.show_choices(parashut, 2)}\n4. {self.show_choices(parashut, 3)}\n')
        else:
            self.tracker.append(parashut)
            if parashut == 9:
                print()
            self.pose_question(parashut)
            print(f'\n1. {self.show_choices(parashut, 0)}\n2. {self.show_choices(parashut, 1)}'
                  + f'\n3. {self.show_choices(parashut, 2)}\n4. {self.show_choices(parashut, 3)}\n')
    
    # This is where the whole user shebang gets checked if it was right or not
    def you_are_who_you_choos2B(self, rando_calrisian):
        reveal = self.prerequisite(rando_calrisian)
        if rando_calrisian != 10 and rando_calrisian != 8:
            if self.answer == self.letter_ans:
                print('\n\nThat is the correct answer.\n\n\n')
                self.score += 1
            elif self.answer != self.letter_ans:
                print(f'\n\nThat is incorrect. The correct answer is {self.letter_ans + 1}\n\n\n')
        elif rando_calrisian == 10:
            if self.answer == self.letter_ans:
                print('\n\nThat is the correct answer.\n')
                self.score += 1
            elif self.answer != self.letter_ans:
                print(f'\n\nThat is incorrect. The correct answer is {self.letter_ans + 1}\n')
        elif rando_calrisian == 7:
            if self.answer == self.letter_ans:
                print('\n\nThat is the correct answer.\n\n\n')
                self.score += 1
            elif self.answer != self.letter_ans:
                print(f'That is incorrect. The correct answer is {self.letter_ans + 1}', end='')
        elif rando_calrisian == 9:
            if self.answer == self.letter_ans:
                print('\n\nThat is the correct answer.\n\n\n')
                self.score += 1
            elif self.answer != self.letter_ans:
                print(f'\n\nThat is incorrect. The correct answer is {self.letter_ans + 1}', end=' ')
        elif rando_calrisian == 8:
            if self.answer == self.letter_ans:
                print('\n\nThat is the correct answer.\n\n')
                self.score += 1
            elif self.answer != self.letter_ans:
                print(f'\n\nThat is incorrect. The correct answer is {self.letter_ans + 1}', end=' ')
                print('\n')
        
    # this dude runs a loop that prints a specific key to the user [a.k.a. the question]        
    def pose_question(self, key_get):
        for key, value in self.TOTAL_QUEST.items():
            for dum in value:
                if key == key_get:
                    print(dum)
                    break
    
    # This sends back a value from the inner nesting dictionary at large
    def show_choices(self, banner, noom):
        f_zero = self.prerequisite(banner)
        return f'{self.TOTAL_QUEST[banner][f_zero][noom]}'
    
    # This sets the precedent for the answer checker                 
    def prerequisite(self, code):
        if code == 1:
            self.letter_ans = 3
            return 'psuedocode'
        elif code == 2:
            self.letter_ans = 0
            return 'flowchart'
        elif code == 3:
            self.letter_ans = 0
            return 'input()'
        elif code == 4:
            self.letter_ans = 3
            return 'slash'
        elif code == 5:
            self.letter_ans = 1
            return '**'
        elif code == 6:
            self.letter_ans = 1
            return 'end'
        elif code == 7:
            self.letter_ans = 1
            return 'float'
        elif code == 8:
            self.letter_ans = 0
            return '68'
        elif code == 9:
            self.letter_ans = 2
            return 'third'
        elif code == 10:
            self.letter_ans = 2
            return '24.0'
    
    # This presents the user with the final score       
    def le_score(self):
        self.score = float(self.score / 10)
        self.score = self.score * 100
        print(f'Your score is: {self.score:.0f}%')
