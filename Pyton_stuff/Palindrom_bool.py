
def reversed(text):
    rev = ''
    for i in range(len(text), 0, -1):
        rev += text[i-1]
    return rev

class Palindrome:
  @staticmethod
  def is_palindrome(word):
      word = word.lower()
      for elem in range(len(word)):
          if word[elem] == reversed(word)[elem]:
              #print(word[elem], word[-1:elem])
              pass
          else:
              return False
      return True
#word = input()
word = "test"
print(Palindrome.is_palindrome(word))
print(Palindrome.is_palindrome("Deleveled"))
print(Palindrome.is_palindrome("adam"))
