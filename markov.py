#!/usr/bin/env python
from random import choice
from sys import argv
script, first = argv
import twitter

api = twitter.Api(//Secret//)

api.VerifyCredentials()

def make_chains(words):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    chains_of_words = {}

    for i in range(len(words) - 2):
        chains_of_words[(words[i], words[i+1])] = chains_of_words.get((words[i], words[i+1]), [])
        chains_of_words[(words[i], words[i+1])].append(words[i+2])
    return chains_of_words

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    list_of_keys = chains.keys()
    key = choice(list_of_keys)
    next_word = choice(chains[key])

    sentence = "%s %s %s" % (key[0], key[1], next_word)

    while True:
        key = (key[1], next_word)
        
        if key in chains:
            next_word = choice(chains[key])
            if len((sentence + next_word)) < 137:
                sentence += (" " + next_word)    
            else:
                break
        else:
            break

    sentence = sentence.rstrip(',"\'!-')
    if not "." in sentence[-1]:
        if "?" in sentence[-1]:
            pass
        else:
            sentence += "..."    
    sentence = sentence[0].upper() + sentence[1:]
    return sentence


def main():
    words = open(first).read().split()
    chain_dict = make_chains(words)
    random_text = make_text(chain_dict)
    status = api.PostUpdate('%s' % random_text)
    print status.text


if __name__ == "__main__":
    main()
