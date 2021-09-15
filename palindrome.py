# def sentenceTrimmed
#
# def palindrome(word):
#     return word == word[::-1]
#
# # split sentence into words and filter out the non palindromes
# sentence = [w for w in input("Enter a sentence: ").split() if palindrome(w)]
#
# print(" There are {} palindromes in your sentence\n.".format(len(sentence)))
# # print each palindrome from our list
# for pal in sentence:
#     print("{} is a palindrome".format(pal))
#
# sentence = input("Enter a sentence: ").split()
#
# count = 0
# for w in sentence:
#     if palindrome(w):
#         count += 1
#         print("{} is a palindrome.")
#     else:
#         print("{}  is not a palindrome.")
# print(" There are {} palindromes in your sentence\n.".format(count))
#
# def palindrome(word):
#     if len(word) > 1:
#         return word == word[::-1]
#     return word.isalpha()



def is_palindrome(sentence):
    return sentence.replace(" ","").lower() == sentence[::-1].replace(" ","").lower()

print(is_palindrome('A saa s a'))

"""
def is_pal(txt):
    txt = txt.replace(" ","").lower()
    return txt == txt[::1]
"""