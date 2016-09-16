#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

chosung_list = ["ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ","ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ" ]
jungsung_list = ["ㅏ","ㅐ","ㅑ","ㅒ","ㅓ","ㅔ","ㅕ","ㅖ","ㅗ","ㅘ","ㅛ","ㅙ","ㅚ","ㅜ","ㅝ","ㅞ","ㅟ","ㅠ","ㅡ","ㅢ","ㅣ"]
jongsung_list = [" ","ㄱ","ㄲ","ㄳ","ㄴ","ㄵ","ㄶ","ㄷ","ㄹ","ㄺ","ㄻ","ㄼ","ㄽ","ㄾ","ㄿ","ㅀ","ㅁ","ㅂ","ㅄ","ㅅ","ㅆ","ㅇ","ㅈ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"]

#0 1 2 3 4 5 6 7 8 9
digit_list = [True, True, False, True, False, False, True, True, True, False]


def has_jongsung(word):
	last_char = unicode(word)[-1:].upper()
	uni = ord(last_char)
	
	offset = ord(u'0')
	if uni >= offset and uni < offset + 10:
		# print (uni-offset)
		return digit_list[ (uni-offset) ]

	offset = ord(u"가")
	jongsung = jongsung_list[ (uni-offset) % len(jongsung_list) ]
	if jongsung == " ":
		return False
	else:
		return True

if(__name__ == '__main__'):
	test_list = ["강호동", "유재석", "이소라", "411", "2,899", "제 3", "5,000,000"]
	for test in test_list:
		result = has_jongsung(test)
		if result == True:
			print "%s은 그렇다." % test
		else:
			print "%s는 그러하다." % test

