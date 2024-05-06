from data import word_prompts;
from data import stories;
import random

story = random.choice(stories)
def main(story):
    words = []
    for item in word_prompts:
        word = input(f"Enter a word ({item}): ")
        words.append(word)

    if len(words) == len(word_prompts):  
        s23 = story.format(adjective= words[0],name=words[1],animal=words[2],cloth=words[3],number=words[4],animals=words[5],verb=words[6],weather=words[7])  # Format story with all words
        print(words)
        print(s23)
        return s23
    else:
        print("Not enough words provided to fill in the story placeholders.")

if __name__ == "__main__":
    main(story)