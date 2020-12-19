import os

prompts = [
    "Holiday: ",
    "Noun: ",
    "Adjective -ing: ",
    "Noun: ",
    "Adverb: ",
    "Adjective: ",
    "Emotion: ",
    "Number: ",
    "Body Part Plural: ",
    "Emotion: ",
    "Verb: ",
    "Verb: ",
]
promptAnswers = []
for prompt in prompts:
    print(prompt, end='')
    userinput = input()
    os.system("clear")
    promptAnswers.append(userinput)

print("It was {} eve, a special time.\nThe {} was {}, because the deadline was near.\nYou powered up your {} and began to code.\nBut, your code was {} {} and you couldn't feel more {}.\nThere were {} bugs, and you were up to your {} in errors.\nBut with a git add and a git push, you committed it without {}!\nYou submit a pull request and {} at your work.\n\"It's QA\'s problem now!\", you hope they all {} at your code!".format(*promptAnswers))