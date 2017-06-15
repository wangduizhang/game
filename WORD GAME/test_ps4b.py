# _*_ coding: utf-8


# Date    : 2017-06-15 12:45:26
# Author  : wangpeng

#ps4b测试文件


import random
from ps4b import compChooseWord
from ps4a import dealHand, loadWords


# text compChooseWord


wordline = loadWords('words.txt')
def test_compchooseword():
	for i in range(1):
		n = random.randrange(5,7)
		print '我们生成了 %d 位字母' % n
		hand = dealHand(n)
		print '我们的‘hand’是：%s' % hand
		print '最优解：%s；最高分：%d ；所有解：%s' % compChooseWord(hand, wordline, n)


print ' * ' * 20
print '开始测试 compChooseWord'
test_compchooseword()
print '测试成功'
print ' = ' * 20