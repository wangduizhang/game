#_*_coding:utf-8_*_
import random
import string

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
global la_st
la_st = ''
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
  'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
WORDLIST_FILENAME = "words.txt"


def loadWords(WORDLIST_FILENAME):
    """
    返回一个有效的单词列表，单词是小写的字符串。
    依赖单词表的长度，这个函数需要保持到结束。
    """
    # inFile: file
    wordList = []
    with open(WORDLIST_FILENAME,'r') as txt:
      lines = txt.readlines()
      for i in lines:
        wordList.append(i)
    return wordList

def getFrequencyDict(sequence):
    """
    返回一个字典，这个字典包含了sequence的全部字母和它出现的次数。
    sequence: string or list
    return: dictionary
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# Problem #1: Scoring a word
def getWordScore(word, n):
    """
    返回单词的分数
    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    print word
    s = 0
    for i in word:
      s += SCRABBLE_LETTER_VALUES[i.lower()]
    s *= len(word)
    if len(word) == n:
      s += 50
    return s
    

    
# Problem #2: Make sure you understand how this function works and what it does!
def displayHand(hand):
    """
    将字典中的字母（几次）展开，打印
    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,                  
    print '\n'                   



def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3 #元音字母个数
    #得到元音字母
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
    #得到辅音字母    
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newhand = hand
    for i in word:
      newhand[i] -= 1
      if newhand[i] == 0:
        del newhand[i]
    return newhand

#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    检测单词的有效性，有效返回true，无效返回false
    
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    s = True
    newhand = hand
    for i in word:
      if i == '':
          s = False
          break
      elif i in hand:
          newhand[i] -= 1
          if newhand[i] < 0:
            s = False
            break
      elif not i in hand:
        s = False
        break
    if ( word.upper() in wordList ) and s:
      return True
 

# Problem #4: Playing a hand
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    s = 0
    for i in hand:
      s += hand[i]
    return s

def playHand(hand, wordList, n):
    """

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    print '你获取的字母为:',
    displayHand(hand)
    while True:
      print '请输入你的单词(输入 . 游戏结束)'
      order = raw_input('1>>>')
      if order == '.':
        word = ''
        print '游戏结束, 最终分数%d' % getWordScore(word, n)
        playGame(wordList)
      else:
        word = order
      while True:
        if isValidWord(order, hand, wordList):
          word = order
          break
        else:
          print '你输入的单词有误，请核查后重新输入！！'
          print '输入 . 游戏结束'
          order = raw_input('2>>>')
          if order == '.':
            word = ''
            print '游戏结束，你最终的分数是：%d ' % getWordScore(word,n)
            playGame(wordList)

        if calculateHandlen(hand) == 0:
          print '游戏结束，你最终的分数是：%d ' % getWordScore(word,n)
          break
        print '剩余字母： %s，当前分数：%d ' % (updateHand(hand, word) ,getWordScore(word,n))
     
# Problem #5: Playing a game
# 

def playGame(wordList):

    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
         2) When done playing the hand, repeat from step 1    
    """
    global la_st
    n = 0
    print 'n:新的游戏 r:重开上局 e:退出'
    order = raw_input('>>>').lower()    
    while True:
      if order == 'n':
        while True:
          n = raw_input('你想获取的字母数(大于4个):')
          try:
            n =  int(n)
            if n > 4:
              break
          except ValueError,e:
            print '输入有误！'
        hand = dealHand(n)
        la_st = hand
        playHand(hand, wordList, n)
      if order == 'r':
        if la_st:
          hand = la_st
          playHand(hand, wordList, n)
        else:
          print '您没有上局存档，请重新输入指令：'
          order = raw_input('>>>')
      if order == 'e':
        print '游戏结束'
        break
      break
      if not order in ['r','n','e'] or order == '':
        print '请重新输入指令：'
        order = raw_input('>>>')
      
      
    
########################################################################




if __name__ == '__main__':
    wordList =  loadWords(WORDLIST_FILENAME)
    last = ''
    playGame(wordList)
