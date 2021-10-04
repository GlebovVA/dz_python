with open('users.csv', 'r', encoding='utf-8') as f_u:
    with open('hobby.csv', 'r', encoding='utf-8') as f_h:

        users = f_u.read().splitlines()
        hobby = f_h.read().splitlines()
        if len(users) >= len(hobby):
            with open('result.txt', 'w', encoding='utf-8') as f:
                inf_list = {}
                for i in range(len(users)):
                    if len(hobby) > i:
                        inf_list[users[i]] = hobby[i]
                    else:
                        inf_list[users[i]] = None
                print(inf_list, file=f)
        else:
            exit(1)
