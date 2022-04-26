# This imports the class thingy
import questions

# This sets the loop up to answer the questions
# The one command commented out is replaced for the grade, but it's what sets up the random number
def linux():
    it_begins = questions.question()
    limit = 1
    
    while limit != 11:
        dire = it_begins.set_rando()
        it_begins.next_contestant(dire)
    
        hai = int(input('Enter your solution (a number between 1 and 4): '))
        hai -= 1
        it_begins.setten(hai)
        it_begins.you_are_who_you_choos2B(dire)
        
        limit += 1
    it_begins.le_score()

# This begins it in the witty spit    
linux()
