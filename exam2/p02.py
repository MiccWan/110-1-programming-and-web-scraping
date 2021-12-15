def find_prefix(*word_lst):
    common = ""
    break_flag = False
    for i in range(len(word_lst[0])):
        s = word_lst[0][i]
        for w in word_lst[1:]:
            if i == len(w):
                break_flag = True
                break
            if w[i] != s:
                break_flag = True
                break
        if break_flag:
            break
        else:
          common += s
    return common or None

print(find_prefix("dog", "cat", "does"))
print(find_prefix("statue", "stand", "student"))