#_*_coding:utf-8_*_

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "读取文件内容......"
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "个单词填装成功"
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)
def pand_(word):
    a_z = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    if word.lower() == "help":
        return ""
    if isinstance(word,str) and word.lower() in a_z:
        pass        
    else:
        print '请输入正确的字母！'
        word = raw_input('>>>')
        pand_(word)
    return word.lower()
    

def in_case(word,case):
    if word not in case:
        return word
    else:
        print "您已猜过 %s ,请重新输入。" % word
        word = raw_input('>>>')
        in_case(word, case)
    return word    
    

def now_result(w, lw, tw, rw):
    if w in tw:
        print "wow,你猜对了。"
        for i in range(len(tw)):
            if w == lw[i:i+1]:
                rw[i:i+1] = w


    else:
        print "sorry,你猜错了。"
    return rw

def cross_(rw):
    if '_' in rw:
        return True
    else:
        return False
wordlist = loadWords()
secretWord = chooseWord(wordlist)
wordcase = []
rw = ['_'] * len(secretWord)
sw = ''
i = 1


while cross_(rw) and i < 20:
    word = raw_input('请输入你的第 %d 次猜想：'% i)
    word = pand_(word)
    word = in_case(word, wordcase)
    wordcase += word

    i += 1
    rw = now_result(word, secretWord,tuple(secretWord),rw)
    sw = ''
    for b in rw:
        sw += b+' '    
    print '当前进度：%s' % sw
    print '您猜过的字母：%s '% wordcase
if not cross_(rw):
    print '！恭喜你通关'
else:
    print '正确答案是%s' % secretWord
    print '!没有猜出来呀，祝你下次好运!'
    
        
        
