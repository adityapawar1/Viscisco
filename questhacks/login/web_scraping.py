import json
import requests
from bs4 import BeautifulSoup



def jsonToDict(filename):
    try:
        login = open(filename, 'r') # get login data
        string_json = ""

        for line in login:
            string_json += line

        return json.loads(string_json)
    except:
        return None

def scrape():
    f = open('out.txt', 'r')
    out = open('scrape.txt', 'w+')

    try:
        city = ""
        for line in f:
            if line == False:
                break
            uname = line

        login_data = jsonToDict('login.json')

        for k, v in login_data.items():
            if k == uname:
                city = v['city']


        url = 'https://www.eventbrite.com/d/ca--{}/volunteer-events/?page=1'  #out database

        r = requests.get(url.format(city.strip().replace(' ', '-'))) # searches for places near you, 'gives you the URL so you can look into it 

        print(city)
        soup = BeautifulSoup(r.content, 'html.parser') #find specific keywords
        vol_names = soup.find_all('div', attrs={'data-spec':'event-card__formatted-name--content'})
        # vol_links = soup.find_all('a', attrs={'class':'eds-media-card-content__action-link'})
        for div in vol_names: #counts how many places we have
            try:
                print("{} - {}".format(div.text, soup.find(attrs={'aria-label':"See more of {}".format(div.text)})['href']))
                out.write("{} - {}".format(div.text, soup.find(attrs={'aria-label':"See more of {}".format(div.text)})['href']))
                out.write('\n')
            except:
                pass
        
        out.close()

    except:
        pass

if __name__ == "__main__":
    scrape()