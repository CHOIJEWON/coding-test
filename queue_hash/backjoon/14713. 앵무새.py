import sys

N = int(sys.stdin.readline().strip())
sentence_lis = [str(sys.stdin.readline().strip()).split() for _ in range(N)]
complete_sentence = str(sys.stdin.readline().strip()).split()

is_complete = True
for word in complete_sentence:
    found = False
    for i, sentence in enumerate(sentence_lis):
        if sentence and sentence[0] == word:
            sentence.pop(0)
            found = True
            break
    if not found:
        is_complete = False
        break

if is_complete and all(len(sentence) == 0 for sentence in sentence_lis):
    print('Possible')
else:
    print('Impossible')
