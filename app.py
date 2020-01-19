import string
import random
import re
  
def strength(password, stringBased = True):
  # Points
  points = 0;
  
  points += (len(re.findall(r'\w', password)))
  points += (len(re.findall(r'\d', password))) * 2
  points += (len(re.findall(r'\b', password))) * 3
  
  if stringBased:
    if points > 80:
      return 'Super strong!'
    elif points > 60 and points < 80:
      return 'Very strong'
    elif points > 50 and points < 60:
      return 'strong'
    elif points > 40 and points < 50:
      return 'Fairly strong'
    elif points > 30 and points < 40:
      return 'Weak'
    elif points < 30:
      return 'Very weak'
  else:
    return points

def generate(length = 28, letters = True, digits = True, symbols = True):
  if (length > 8):
    if (letters or digits or symbols):
      result = ""
      chars = (string.ascii_letters if letters else '') + \
        (string.digits if digits else '') + (string.punctuation if symbols else '')

      for i in range(length):
        result += random.choice(chars)

      if (strength(password= result, stringBased = False) > 60):
        return result
      else:
        return generate(length = length, letters = letters, digits = digits, symbols = symbols)
    else:
      return 'Missing requirement'
  else:
    return 'Password is too weak!'