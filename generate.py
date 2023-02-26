import json
import random


def generate():
    output = [random.choice(starts)]
    while output[-1] != '\n':
        output.append(random.choice(letters[output[-1]]))

    return ''.join(output[:-1])


if __name__ == "__main__":
    with open('./saved.json') as json_file:
        data = json.load(json_file)
    letters = data['letters']
    starts = data['starts']

    for i in range(15):
        print(generate())
