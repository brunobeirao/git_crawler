from bs4 import BeautifulSoup
import requests
import configparser
import os

class CrawlerService:

    def __init__(self):
        thisfolder = os.path.dirname(os.path.abspath(__file__))
        configFilePath = (os.path.join('C:\\TI\\workspace\\python\\git_crawler\\git_crawler\\config', 'config.ini'))
        config = configparser.ConfigParser()
        config.read(str(configFilePath))
        config.sections()
        self.login_data = {
            'user[login]': config['DEV']['LOGIN'],
            'user[password]': config['DEV']['PASSWORD'],
            'user[remember_me]': '1'
        }
        self.url_login = config['DEV']['LOGIN_URL']
        self.url_commits = config['DEV']['COMMITS_URL']
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/73.0.3683.86 Safari/537.36'
        }

    def login(self, session):
        response = session.get(self.url_login, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        self.login_data['authenticity_token'] = soup.find(
            'input', attrs={'name': 'authenticity_token'})['value']
        session.post(self.url_login, data=self.login_data, headers=self.headers)
        return session

    def get_commits(self):
        with requests.session() as session:
            session_logged = self.login(session)
            resp = session_logged.get(self.url_commits)
            result = BeautifulSoup(resp.text, 'html.parser')
            print(result.prettify())
