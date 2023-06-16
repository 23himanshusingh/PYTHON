s, ans, i = input(), list(), 1
while (i < len(s)):
    if (s[i] == '[' and s[i - 1].isalpha()):
        temp, j = "", i - 1
        while (s[j].isalpha()):
            temp += s[j]; j -= 1
        temp, j = temp[::-1] + " ", i + 1
        while (s[j] != ']'):
            temp += s[j]; j += 1
        ans.append(temp)
        i = j
        continue
    i += 1
print(-1 if not ans else "\n".join(ans))

