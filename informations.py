import json


with open('db.json', 'r') as f:
    data = json.load(f)
    i = data['usernames']
    l = [[user.get(str(c), 2) for c in range(5)] + [struser, user['etgar']] for struser, user in i.items()]
    for user in l:
        c = user.count(0)
        if c > 0:
            print(user)
