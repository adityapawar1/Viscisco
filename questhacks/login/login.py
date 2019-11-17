import json
import os
from time import sleep
from web_scraping import scrape

def jsonToDict(filename):
    try:
        login = open(filename, 'r')
        string_json = ""

        for line in login:
            string_json += line

        return json.loads(string_json)
    except:
        return None
while True:
    if os.path.isfile('/Users/adityapawar/Downloads/login.txt'):
        if True:
            f = open("/Users/adityapawar/Downloads/login.txt")
            inp = ""
            c = 0
            while len(inp) < 2 or c < 20:
                c += 2
                for line in f:
                    inp = line

            f.close()
            
            username = inp.split('-')[0]
            password = inp.split('-')[-1]

            print('user: {}, pass: {}'.format(username, password))

            login_data = jsonToDict("login.json")

            error = ""

            if username in login_data['users'].keys():
                database_out = login_data['users'].__getitem__(username)

                if database_out != None:
                    if database_out['pass'] == password:
                        login_success = True
                    else:
                        login_success = False
                        error = "Wrong Password"
                else:
                    login_success = False
                    error = "Invalid Username"

                with open('out.txt', 'w+') as out:
                    out.write(str(login_success) + "\n")
                    out.write(username)
                    scrape()


                os.remove('/Users/adityapawar/Downloads/login.txt')

            else:
                os.remove('/Users/adityapawar/Downloads/login.txt')
                # print(0/0)

        else:
            with open('out.txt', 'w+') as out:
                out.write(str(False) + '\n')

            os.remove('/Users/adityapawar/Downloads/login.txt')
