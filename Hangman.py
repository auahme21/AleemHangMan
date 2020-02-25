global UpdateSpaces
global lives
global word
letter =["h"]
word = ['hamza']
def check(UpdateSpaces):
    lives = 6
    UpdateSpaces= ['-','-','-','-','-']
    if letter in word:
        word.find(letter,0,len(word)-1)
        UpdateSpaces[0]='h'
        word.find(letter,1,len(word)-1)
        UpdateSpaces[1]='a'
        word.find(letter,2,len(word)-1)
        UpdateSpaces[2]='m'
        word.find(letter,3,len(word)-1)
        UpdateSpaces[3]='z'
        word.find(letter,4,len(word)-1)
        UpdateSpaces[4]='a'
    else:
        lives = lives - 1

