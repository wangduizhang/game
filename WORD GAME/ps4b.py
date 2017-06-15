# _*_coding:utf-8_*_
from ps4a import *
import time
import copy
import random
global la_st2
la_st2 = ''

def maxcompChooseWord(hand, wordList, n):
    # 电脑给出最优解
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    point = 0
    maxword = ''
    for word in wordList:
        newword1 = copy.deepcopy(word)
        newword2 = copy.deepcopy(word)
        if isValidWord(newword1, hand, wordList):
            p = getWordScore(newword2, n)
            if p > point:
                point = p
                maxword = word
    if point == 0:
        return None
    else:
        return maxword, point

def compChooseWord(hand, wordList, n):
    #电脑给出随机答案
    wordlist = []
    for word in wordList:
        newword1 = copy.deepcopy(word)
        if isValidWord(newword1, hand, wordList):
            wordlist.append(word)
    if wordlist == None:
        return None
    else:
        x = random.randrange(len(wordlist))
        word = wordlist[x]
        newword2 = copy.deepcopy(word)
        p = getWordScore(newword2, n)
        return word, p
    
def outcome(usersumpoint,comsumpoint):
    if usersumpoint > comsumpoint:
        print '真厉害！你赢了！'
    elif usersumpoint < comsumpoint:
        print '虽然输了，但祝你下次好运！'
    elif usersumpoint == comsumpoint:
        print '差一点就赢了！下次加油！'


# Problem #7: Computer plays a hand
#

def playHandplus(hand, wordList, n):
    global la_st2
    """
      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    num = 1
    usernewhand = copy.deepcopy(hand)
    comnewhand =  copy.deepcopy(hand)
    usersumpoint = 0
    comsumpoint = 0
    comanswer = True
    print ' = ' * 20
    print '你们获取的字母为:',
    displayHand(hand),
    while True:
        print ' = ' * 20
        print '***第 %d 轮***' % num
        print '请思考你的答案'
        print '电脑正在思考'
        try:
            if comanswer:
                (comword, compoint) = compChooseWord(comnewhand, wordList, n)
        except ValueError as e:
            print '电脑实在想不出答案了'
            comword = ''
            compoint = 0
            comanswer = False
        if compoint != 0:
            print '电脑思考结束'
        print ' = ' * 20
        print "输入你的答案（'.'结束游戏)"
        order = raw_input('>>>')
        if order == '.':
            print '游戏结束，你最终的分数是：%d ' % usersumpoint
            print '游戏结束，电脑最终的分数是：%d ' % comsumpoint
            print ' = ' * 20
            outcome(usersumpoint, comsumpoint)
            print ' = ' * 20
            playGameplus(wordList)
            return
        while True:
            if isValidWord(order, usernewhand, wordList):
                if comword:
                    print '电脑的答案：%s' % comword
                userword = order
                userpoint = getWordScore(userword, n)
                print '正确的单词！这局你的分数 %d' % userpoint
                print '这局电脑的分数 %d' % compoint
                print ' = ' * 20
                num += 1
                comsumpoint += compoint
                usersumpoint += userpoint
                break
            else:
                print '你输入的单词有误，请核查后重新输入！！'
                print '输入 . 游戏结束'
                order = raw_input('>>>')
            if order == '.':
                print '游戏结束，你最终的分数是：%d ' % usersumpoint
                print '游戏结束，电脑最终的分数是：%d ' % comsumpoint
                print ' = ' * 20
                outcome(usersumpoint, comsumpoint)
                print ' = ' * 20
                playGameplus(wordList)
                break
        usernewhand = updateHand(usernewhand, userword)
        comnewhand = updateHand(comnewhand, comword)

        if calculateHandlen(usernewhand) == 0 or calculateHandlen(comnewhand) == 0:
            print '游戏结束，你最终的分数是：%d ' % sumpoint
            print '游戏结束，电脑最终的分数是：%d ' % comsumpoint
            print ' = ' * 20
            outcome(usersumpoint, comsumpoint)
            print ' = ' * 20
            break
        print '电脑剩余字母：', 
        displayHand(comnewhand),
        print '电脑当前分数 %d ' % ( comsumpoint)
        print ' = ' * 20
        print '你剩余字母:', 
        displayHand(usernewhand),
        print '你当前分数：%d' % (usersumpoint)


def playGameplus(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    #选择游戏模式
    global la_st2
    n = 0
    print '请选择你想进行的模式：a：单人 c：人机 e: 退出游戏'
    while True:
        order9 = raw_input('>>>').lower()
        if (order9 == 'a') or (order9 =='c'):
            moudl = True
            break
        elif order9 == 'e':
            moudl = False
            print '游戏已退出'
            print ' = ' * 20
            break
        else:
            print '命令有误，请重新输入'
    if moudl:
        print 'n:新的游戏 r:重开上局 e:退出'
        order8 = raw_input('>>>').lower()  
        while True:
            if order8 == 'n':
                while True:
                    n = raw_input('你想获取的字母数(大于4个):')
                    while True:
                        try:
                            n =  int(n)
                            if n > 4:
                                break
                        except ValueError,e:
                            print '输入有误！'
                    if order9 == 'a':
                        hand = dealHand(n)
                        la_st = copy.deepcopy(hand)
                        playHand(hand, wordList, n)
                    elif order9 == 'c':
                        hand = dealHand(n)
                        la_st = copy.deepcopy(hand)
                        playHandplus(hand, wordList, n)
            if order8 == 'r':
                if la_st2 and (order9 == 'a'):
                    playHand(la_st, wordList, n)
                elif la_st2 and (order9 == 'c'):
                    playHandplus(hand, wordList, n)
                elif not la_st2:
                    print '您没有上局存档，请重新输入指令：'
                order8 = raw_input('>>>').lower()
            if order8 == 'e':
                print '游戏结束'
                break
            if not order8 in ['r','n','e'] or order8 == '':
                print '请重新输入指令：'
                order8 = raw_input('>>>').lower()



if __name__ == '__main__':
    wordList = loadWords('words.txt')
    playGameplus(wordList)


