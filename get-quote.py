import random
def primary():
  # print("Keep it logically awesome.")
  last = 13
  rnd = random.randint(0, last)
  
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  # print(quotes)
  # print(quotes[0])
  last = len(quotes) - 1
  print(quotes[rnd])

if __name__== "__main__":
  primary()
