import json
import os

admin = False

def jsonToDict(filename):
    try:
        login = open(filename, 'r') # get login data
        string_json = ""

        for line in login:
            string_json += line

        login.close()

        return json.loads(string_json)
    except:
        return None

while True:
    if os.path.isfile('/Users/adityapawar/Downloads/sign_up.txt'):
    
        f = open('/Users/adityapawar/Downloads/sign_up.txt', 'r')
        inp = ""
        for line in f:
            inp += line
            print(line)

        f.close()
        print("inp: {}".format(inp))

        filename = '/Users/adityapawar/Desktop/questhacks/login/login.json'
        admin = False
        try:
            user = inp.split('-')[2]
            password = inp.split('-')[3]
            city = inp.split('-')[-1]

            login_data = jsonToDict(filename)

            dump = {'pass': password, 'city': city}

            if not admin:
                login_data['users'].__setitem__(user, dump)
            else:
                login_data['admin'].__setitem__(user, dump)

            output = json.dumps(login_data)

            with open(filename, 'w+') as out:
                out.write(output)


            if not admin:
                login_data['users'].__setitem__(user, dump)
            else:
                login_data['admin'].__setitem__(user, dump)

            output = json.dumps(login_data)

            with open(filename, 'w+') as out:
                out.write(output)

            os.remove('/Users/adityapawar/Downloads/sign_up.txt')
        except:
            print('There was an error')

            output = json.dumps(login_data)

            with open(filename, 'w+') as out:
                out.write(output)

            os.remove('/Users/adityapawar/Downloads/sign_up.txt')









