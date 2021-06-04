def knights():
    title = 'Sir'
    actions = (lambda x : title + ' ' + x)
    return action

act = knights()
print act('David')
print act('Mukund')
