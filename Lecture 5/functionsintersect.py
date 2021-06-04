def intersect(seq1, seq2):
    res = [] #blank list
    for item in seq1:
        if item in seq2:
            res.append(item)
    return res

s1 = "SPAM"
s2 = "SCAM"
print intersect(s1, s2)

x1 = [1, 2, 3, 4]
x2 = [3, 4, 5, 7]
print intersect(x1, x2)

tweet1 = ['Rain', 'NYC', 'umbrella']
tweet2 = ['Wet', 'Clothes', 'Rain']
print intersect(tweet1, tweet2)
