import random
import string


def generate_password(length=12):
  letters = string.ascii_letters
  digits = string.digits
  special_chars = string.punctuation

  all_chars = letters + digits + special_chars

  password = [
      random.choice(letters),
      random.choice(letters.upper()),
      random.choice(digits),
      random.choice(special_chars),
  ]

  password += random.choices(all_chars, k=length - 4)

  random.shuffle(password)

  return ''.join(password)


password = generate_password(length=12)
print("Random Password:", password)
