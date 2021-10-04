with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    with open('log_file.txt', 'w', encoding='utf-8') as p:
        inf_list = ((log.split()[0], log.split()[5][1:], log.split()[6]) for log in f)
        for i in inf_list:
            print(i)
            print(i, file=p)
