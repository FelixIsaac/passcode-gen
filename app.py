import string
import random


def generate(length=28, letters=True, digits=True, symbols=True):
  if (length > 8):
    if (letters or digits or symbols):
      result = ""
      chars = (string.ascii_letters if letters else '') + \
        (string.digits if digits else '') + (string.punctuation if symbols else '')

      for i in range(length):
        result += random.choice(chars)

      return result
    else:
      return 'Missing requirement'
  else:
    return 'Password is too weak!'