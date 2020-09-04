import random

verbs = ["Increase", "Boost", "Scale", "Grow"]
adjectives = ["portrait", "family", "brand"]
nouns = ["business", "profits", "sales"]

verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

phrase = verb + " your " + adjective + " photography " + noun + " with Video Portraits!"

print(phrase)

