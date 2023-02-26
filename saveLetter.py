import json
letters = {}
starts = []


def update_letters(word):
    starts.append(word[0])
    for a, b in zip(word, word[1:]):
        if a not in letters:
            letters[a] = []
        letters[a].append(b)


if __name__ == "__main__":
    wordsFile = open('./10000-common.txt')
    word = next(wordsFile)[:-1]
    while word is not None:
        if len(word) < 5:
            word = next(wordsFile, None)
            continue

        update_letters(word)
        word = next(wordsFile, None)

    with open('./saved.json', 'w') as save:
        json.dump({'letters': letters, 'starts': starts}, save)
