import re
import pandas as pd
import matplotlib.pyplot as plt

# TASK 1
print("Type path to the input file (ftp links)")
path1 = input()
print("Type path to the output directory (dont forget / at the end)")
path2 = input()
path2 = path2 + "ftps"

input1 = pd.read_csv(path1, sep="\t", header=None, engine='python')
pattern = '^ftp'
output1 = open(path2, "w")
for (columnName, columnData) in input1.iteritems():
    for value1 in columnData.values:
        try:
            result = re.match(pattern, value1)
        except TypeError:
            continue
        if result:
            output1.write(value1 + '\n')
output1.close()

# TASK 2,3

print("Type path to the input file (story)")
path2_1 = input()
print(path2_1)

with open(path2_1) as input2_1:
    result_t_2 = []
    result_t_2_2 = []
    for line in input2_1.readlines():
        pattern = r'\d+'
        pattern2 = 'a+'
        for word in line.split(' '):
            result2 = re.match(pattern, word)
            result2_2 = re.match(pattern2, word, re.IGNORECASE)
            if result2:
                if word.find(".") > -1:
                    result_t_2.append(word)
                else:
                    result_t_2.append(result2.group(0))
            if result2_2:
                word = re.sub("[^a-zA-Z]+", "", word)
                result_t_2_2.append(word)
                result_t_2_2.append(word)
    print("Task2 results:")
    print(*result_t_2)
    print("Task 3 results:")
    print(*result_t_2_2)

# TASK 4

with open(path2_1) as input2_1:
    print("Task 4 results:")
    sentencess = []
    for line4 in input2_1.readlines():
        pattern4 = re.compile(r'([A-Z][^\.!?]*[!])', re.M)
        for sentence in pattern4.findall(line4):
            if len(sentence) > 0:
                sentencess.append(sentence)
    print(*sentencess)

# TASK 5

with open(path2_1) as input2_1:
    print("Task 5 results:")
    big_string = ""
    for line5 in input2_1.readlines():
        big_string = big_string+line5
    pattern5 = r'\w+'
    uniq_words = set(line_sth.lower() for line_sth in (re.findall(pattern5, big_string, re.IGNORECASE)))
    uniq_words_list = list(uniq_words)
    uniq_words_sorted = list(sorted(uniq_words_list, key=len))
    word_dict = {}
    i = 1
    word_dict[1] = 0
    for j in uniq_words_sorted:
        if len(j) == i:
            word_dict[i] = word_dict[i] + 1
        else:
            i = i + 1
            word_dict[i] = 0
    length_list = list(word_dict.values())

    plt.bar(word_dict.keys(), word_dict.values(), width=0.5, color='y')
    plt.xlabel('Word length')
    plt.ylabel('Count')
    plt.title('Histogram of word length')
    plt.grid(True)
    plt.xticks([i for i in range(1, 16)])
    plt.show()
