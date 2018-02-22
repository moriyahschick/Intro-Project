import Draw
import random
import sys

#opens the page that you see when you start the game
def startProgram():
    Draw.setCanvasSize(1400, 750)
    lightBlue = Draw.color(204, 229, 255)
    Draw.setColor(lightBlue)
    Draw.filledRect(0, 0, 1400, 750)
    Draw.setColor(Draw.LIGHT_GRAY)
    Draw.filledRect(600, 375, 200, 75)
    Draw.setColor(Draw.BLACK)
    Draw.rect(600, 375, 200, 75)
    Draw.setFontFamily('Courier')
    Draw.setFontSize(24)
    Draw.string("Play", 672, 400)
    Draw.setFontSize(45)
    Draw.string("Word Cookies", 560, 200)
    while True:
        if Draw.mousePressed():
            newX = Draw.mouseX()
            newY = Draw.mouseY()
            if newX >= 600 and newX <= 800 and newY >= 375 and newY <= 450:
                Draw.clear()
                mediumBlue = Draw.color(66, 158, 218)
                Draw.setColor(mediumBlue)
                Draw.filledRect(0, 0, 1400, 750)
                Draw.setColor(Draw.WHITE)
                Draw.setFontSize(14)
                for i in range(100, 600, 100):
                    Draw.filledRect(500, i, 400, 50)
                Draw.setColor(Draw.BLACK)
                Draw.string("Instructions:", 655, 570)
                Draw.string("Press on letters, then click \"Enter\"", 510, 600)
                Draw.string("Get points for the length of the word you input", 510, 620)
                Draw.string("When you get enough points- you win!", 510, 640)
                for i in range(100, 600, 100):
                    Draw.rect(500, i, 400, 50)
                for i in range(120, 575, 100):
                    Draw.string("Level "+str(i//100), 680, i)
                Draw.show()
                return False

################################################################################
#Open scrabble dictionary and turn it into a list
#(which will then be used to make smaller lists with words of ___ length)

fourLetterWords = [ ]
fiveLetterWords = [ ]
sixLetterWords = [ ]
sevenLetterWords = [ ]
eightLetterWords = [ ]
dictionaryWords= [ ]

def createDictionary():
    fin = open("scrabbleDictionary.txt")
    line = fin.readline()
    while line:
        line = line.rstrip('\n')
        dictionaryWords.append(line)
        line = fin.readline()
    fin.close()
        
    for word in dictionaryWords:
        if len(word) == 4:
            fourLetterWords.append(word)
        elif len(word) == 5:
            fiveLetterWords.append(word)
        elif len(word) == 6:
            sixLetterWords.append(word)
        elif len(word) == 7:
            sevenLetterWords.append(word)
        elif len(word) == 8:
            eightLetterWords.append(word)

lettersOnScreen = []
def chooseWord(num):
    global lettersOnScreen
    wordUsed = ""
    box = 0   #how many boxes you have on the screen for letters
    numOptions = []  #option of what index to call to draw on screen (to be used randomly later)
    
    if num == 1:
        box = 4
        wordUsed = fourLetterWords[random.randint(0,len(fourLetterWords))]
        for i in range(box):
            numOptions.append(i)
            
    elif num == 2:
        box = 5
        wordUsed = fiveLetterWords[random.randint(0, len(fiveLetterWords))]
        for i in range(box):
            numOptions.append(i) 
        
    elif num == 3:
        box = 6
        wordUsed = sixLetterWords[random.randint(0, len(sixLetterWords))]
        for i in range(box):
            numOptions.append(i) 
        
    elif num == 4:
        box = 7
        wordUsed = sevenLetterWords[random.randint(0, len(sevenLetterWords))]
        for i in range(box):
            numOptions.append(i)  
        
    elif num == 5:
        box = 8
        wordUsed = eightLetterWords[random.randint(0, len(eightLetterWords))]
        for i in range(box):
            numOptions.append(i)   
                
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(28)
    for i in range(590-((num)*50), 850+((num)*50), 100):
        # pick a random num to index at
        c = random.choice(numOptions)
        # draw that random letter on the screen
        Draw.string(wordUsed[c], i, 560)
        # add letter on the screen to global list keeping track
        lettersOnScreen.append(wordUsed[c])
        # remove num option 
        numOptions.remove(c)
           
    Draw.show()
    
################################################################################
#set up points counter
#for each word accepted add to points len(wordAccepted)
#if number of points reached x (x is based off of difficulty of level) then
#can go onto the next level
#at new level, set the points to zero

points = 0

#Level 1 -- 5 points
#Level 2 -- 12 points
#Level 3 -- 15 points
#Level 4 -- 20 points
#Level 5 -- 25 points

#prints on screen how many points needed to win level
def pointsToWin(num):
    Draw.setColor(Draw.BLACK)
    if num == 1:
        Draw.string("You Need 5 Points to Win", 610, 110)
    if num == 2:
        Draw.string("You Need 12 Points to Win", 610, 110)   
    if num == 3:
        Draw.string("You Need 15 Points to Win", 610, 110) 
    if num == 4:
        Draw.string("You Need 20 Points to Win", 610, 110)
    if num == 5:
        Draw.string("You Need 25 Points to Win", 610, 110)    
        
#if you won the level (aka got enough points):
#(will be invoked as consequence of an if statement)
def youWon(num):
    global lettersOnScreen
    global points
    global theString
    global a
    global b 
    global maxWords
    #have a box pop up that tell you you won and gives you the option to
    #       A) continue playing
    #       B) go on to next level
    lightBlue = Draw.color(204, 229, 255)
    Draw.setColor(lightBlue)    
    Draw.filledRect(1110, 225, 200, 200)
    Draw.setColor(Draw.WHITE)
    Draw.rect(1110, 225, 200, 200) 
    Draw.rect(1135, 317, 150, 35)  #A
    Draw.rect(1135, 368, 150, 35)  #B
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(24)
    Draw.string("YOU WON!", 1147, 255)
    Draw.setFontSize(12)
    Draw.string("Continue this Level", 1145, 325)
    Draw.string("Next Level", 1170, 375)
    Draw.show()
    
    while True:
        if Draw.mousePressed():
            newX = Draw.mouseX()
            newY = Draw.mouseY()
            #if you press on "continue playing"
            if newX >= 1135 and newX <= 1285 and newY >= 317 and newY <= 352:
                #cover this box with a box same size thats medium blue and a bottom to move on
                #draw a new button to go to next level in the corner
                mediumBlue = Draw.color(66, 158, 218)
                Draw.setColor(mediumBlue)
                Draw.filledRect(1110, 225, 200, 200)
                
                #continue playing the level
                return True
                
            #if press enter: (Without pressing continue playing)         
            if newX > 990 and newX < 1090 and newY > 650 and newY < 700:
                if theString in dictionaryWords:
                    Draw.setFontSize(16)
                    Draw.string(theString, a, b)
                    points += len(theString)
                    mediumBlue = Draw.color(66, 158, 218)
                    Draw.setColor(mediumBlue)
                    Draw.filledRect(0, 0, 150, 100)
                    pointsStatus()
                    dictionaryWords.remove(theString)
                    theString = ""
                    redrawInputBox()
                    
                    if b <= 390 and a <= 890: # end of box
                        b += 20
                        
                    if b > 390 and a <= 890:
                        b = 200
                        a += 110
                        
                    if a > 890:
                        maxWordsReached()
                      
                else:
                    theString = ""
                    redrawInputBox()
                    
            Draw.setFontSize(24)
            sys.stdout.flush()
            character = None
            
            redrawInputBox()
            Draw.setFontSize(24)
            Draw.string(theString, 700-(len(theString)*10), 660)
            Draw.show() 
                                        
            
            #original next level button
            if newX >= 1135 and newX <= 1285 and newY >= 368 and newY <= 403 and num <= 4:
                #go on to next level
                nextLevel(num)
            
            #decided to play on, now want to go to next level
            if newX >= 1140 and newX <= 1290 and newY >= 650 and newY <= 700 and num <= 4:
                #go on to next level
                nextLevel(num)
                
def wonLevel5():
    Draw.clear()
    lightestBlue = Draw.color(135, 206, 250)
    Draw.setColor(lightestBlue)       
    Draw.filledRect(0, 0, 1400, 750)
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(36)
    Draw.string("Congrats!", 600, 225)
    Draw.string("YOU WON!!", 600, 300)
    Draw.show()

def maxWordsReached():
    lightBlue = Draw.color(204, 229, 255)
    Draw.setColor(lightBlue)    
    Draw.filledRect(1110, 225, 200, 200)
    Draw.setColor(Draw.WHITE)
    Draw.rect(1110, 225, 200, 200) 
    Draw.rect(1135, 317, 150, 35)  #A
    Draw.rect(1135, 368, 150, 35)  #B
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(24)
    Draw.string("YOU WON!", 1147, 255)
    Draw.setFontSize(12)
    Draw.string("Max Words Reached", 1145, 325)
    Draw.string("Next Level", 1170, 375)
    Draw.show()  
    newX = Draw.mouseX()
    newY = Draw.mouseY()    
    if newX >= 1135 and newX <= 1285 and newY >= 368 and newY <= 403 and num <= 4:
        #go on to next level
        print("Button pressed after maxWordsReached to go to next level")
        nextLevel(num)


################################################################################
#set up how the level page will look

#how the input box will look in all levels
def inputBox():
    Draw.setColor(Draw.WHITE)
    Draw.filledRect(500, 650, 400, 50)
    Draw.filledRect(990, 650, 100, 50)
    Draw.setColor(Draw.BLACK)
    Draw.rect(500, 650, 400, 50)
    Draw.rect(990, 650, 100, 50)
    Draw.setFontSize(16)
    Draw.string("Enter", 1015, 665)
    Draw.setFontSize(14)
    
def redrawInputBox():
    mediumBlue = Draw.color(66, 158, 218)
    Draw.setColor(mediumBlue)
    Draw.filledRect(0, 650, 950, 50)
    Draw.setColor(Draw.WHITE)
    Draw.filledRect(500, 650, 400, 50)
    Draw.setColor(Draw.BLACK)
    Draw.rect(500, 650, 400, 50)  

def whichLetterPressingOn(num):
    global theString
    global lettersOnScreen
    newX = Draw.mouseX()
    newY = Draw.mouseY()    
    if newX > 575-(num*50) and newX < 835+(num*50) and newY > 550 and newY < 600:
        cellNum = (newX-(575-(num*50)))//50
        if cellNum % 2 == 0:
            cellNum //= 2
            if len(theString) <= 15:
                character = lettersOnScreen[cellNum]
                theString += character     

a = 450
b = 200
maxWords = False            
def ifPressEnter(num):
    global theString
    global a
    global b
    global points
    newX = Draw.mouseX()
    newY = Draw.mouseY()
    global maxWords
    #if press enter:
    if newX > 990 and newX < 1090 and newY > 650 and newY < 700:
        if theString in dictionaryWords:
            Draw.setFontSize(16)
            Draw.string(theString, a, b)
            points += len(theString)
            mediumBlue = Draw.color(66, 158, 218)
            Draw.setColor(mediumBlue)
            Draw.filledRect(0, 0, 150, 100)
            pointsStatus()
            dictionaryWords.remove(theString)
            theString = ""
            redrawInputBox()
            
            if b <= 390 and a <= 890: # end of box
                b += 20
           
            if b > 390 and a <= 890:
                b = 200
                a += 110
            
            if a > 890:
                maxWords = True
                
        else:
            theString = ""
            redrawInputBox()
        if maxWords == False:
            if num == 1 and points >= 5:
                youWon(num)
            if num == 2 and points >= 12:
                youWon(num)
            if num == 3 and points >= 15:
                youWon(num)
            if num == 4 and points >= 20:
                youWon(num) 
            if num == 5 and points >= 25:
                wonLevel5()
        if maxWords == True:
            #maxWordsReached()
            lightBlue = Draw.color(204, 229, 255)
            Draw.setColor(lightBlue)    
            Draw.filledRect(1110, 225, 200, 200)
            Draw.setColor(Draw.WHITE)
            Draw.rect(1110, 225, 200, 200) 
            Draw.rect(1135, 317, 150, 35)  #A
            Draw.rect(1135, 368, 150, 35)  #B
            Draw.setColor(Draw.BLACK)
            Draw.setFontSize(24)
            Draw.string("YOU WON!", 1147, 255)
            Draw.setFontSize(12)
            Draw.string("Max Words Reached", 1145, 325)
            Draw.string("Next Level", 1170, 375)
            Draw.show()  

theString = ""

#have the input appear in the input box and have it processed as theString when enter is pressed
#(to then after use to loop through dictionary and check for it)
def inputToString(num):
    global lettersOnScreen
    global points
    global theString
    global a
    global b
    global maxWords
    Draw.setColor(Draw.BLACK)
    while True:
        if Draw.mousePressed():
            newX = Draw.mouseX()
            newY = Draw.mouseY()
            
            #if press enter:
            ifPressEnter(num)
            if maxWords == True:
                if newX >= 1135 and newX <= 1285 and newY >= 368 and newY <= 403 and num <= 4:
                    #go on to next level
                    print("Button pressed after maxWordsReached to go to next level")
                    nextLevel(num)            
                print("Ran maxWordsReached in if statement of ifPressEnter")
                print("Meaning maxWords = True")            
            
            #otherwise, which letter are you pressing
            whichLetterPressingOn(num)  
        
            Draw.setFontSize(24)
            redrawInputBox()
            Draw.string(theString, 700-(len(theString)*10), 660)
            if num == 5 and points >= 25:
                wonLevel5()
            Draw.show() 

################################################################################    
#Make a box in middle in which inputted words show up
def boxApprovedWords():
    Draw.setColor(Draw.LIGHT_GRAY)
    Draw.filledRect(400, 150, 605, 300)
    Draw.setColor(Draw.BLACK)
    Draw.rect(400, 150, 605, 300)

def pointsStatus():
    global points
    Draw.setColor(Draw.BLACK)
    Draw.string("Points: "+ str(points), 10, 10)
    
#set up level and show level and input box 
def level(num):
        Draw.clear()
        global points
        points = 0
        mediumBlue = Draw.color(66, 158, 218)
        Draw.setColor(mediumBlue)
        Draw.filledRect(0, 0, 1400, 750)
        Draw.setColor(Draw.BLACK)
        Draw.setFontSize(30)
        Draw.string("Level "+str(num), 650, 50)
        inputBox()
        boxApprovedWords()
        pointsStatus()
        pointsToWin(num)

#if player wins the level and wants to go on to next level, invoke this function        
def nextLevel(num):  
    global points
    global lettersOnScreen
    global a
    global b
    #TESTING
    global maxWords
    a = 450
    b = 200
    maxWords = False
    Draw.clear()
    dictionaryWords.clear()
    createDictionary()
    lettersOnScreen.clear()
    level(num+1)
    lettersLevel(num+1)
    chooseWord(num+1)
    if num <= 4:
        inputToString(num+1)
        pointsStatus()
    if num == 5:
        wonLevel5()
    Draw.show()    

#show number of letters available for use in the level        
def lettersLevel(num):
    Draw.setColor(Draw.WHITE)
    for i in range(575-(num*50), 850+(num*50), 100):
        Draw.filledRect(i, 550, 50, 50)
    Draw.setColor(Draw.BLACK)
    for i in range(575-(num*50), 850+(num*50), 100):
        Draw.rect(i, 550, 50, 50) 
    Draw.show() 

def chooseLevel():
    while True:
        if Draw.mousePressed():
            newX = Draw.mouseX()
            newY = Draw.mouseY()
            #Level 1
            if newX >= 500 and newX <= 900 and newY >= 100 and newY <= 150:
                level(1)
                lettersLevel(1)
                chooseWord(1)
                inputToString(1)
                return False
            #Level 2
            if newX >= 500 and newX <= 900 and newY >= 200 and newY <= 250:
                level(2)
                lettersLevel(2)
                chooseWord(2)
                inputToString(2)
                return False
            #Level 3
            if newX >= 500 and newX <= 900 and newY >= 300 and newY <= 350:
                level(3)
                lettersLevel(3)
                chooseWord(3)
                inputToString(3)
                return False
            #Level 4
            if newX >= 500 and newX <= 900 and newY >= 400 and newY <= 450:
                level(4)
                lettersLevel(4)
                chooseWord(4)
                inputToString(4)
                return False
            #Level 5
            if newX >= 500 and newX <= 900 and newY >= 500 and newY <= 550:
                level(5)
                lettersLevel(5)
                chooseWord(5)
                inputToString(5)
                return False       
        
def main():
    createDictionary()
    startProgram()
    chooseLevel()
main()