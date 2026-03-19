# libraries:--

# import random 
# coin = random.choice(["heads", "tails"])
# print(coin)

# from random import choice
# coin = choice(["heads", "tails"])
# print(coin)

# import random
# number = random.randint(1, 100)
# print(number)

# import random
# cards = ["jack", "queen", "king"]
# random.shuffle(cards)
# for card in cards:
#     print(card)

# statistics in lib:--
# import statistics

# print(statistics.mean([100, 70]))

# command-line arguments
# sys.argv -- list of words that were typed before running
# import sys
# print("hello, my name is", sys.argv[0])

# import sys
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
# print("hello, my name is", sys.argv[1])

# slices -- 
# import sys
# if len(sys.argv) < 2:
#     sys.exit("Two few arguments")
# for arg in sys.argv[1:]:
#     print("hello, my name is", arg)

# packages -- a 3rd party lib
# pip -- let's u install packages
# import cowsay
# import sys
# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])

# APIs --- 

# import requests
# import sys
# if len(sys.argv) != 2:
#     sys.exit()
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(response.json())

# import json
# import requests
# import sys
# if len(sys.argv) != 2:
#     sys.exit()
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2 ))
#import json
#import requests
#import sys
#if len(sys.argv) != 2:
#     sys.exit()
#response = #requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
#o = response.json()
#for result in o["results"]:
#    print(result["trackName"])