
import requests
from bs4 import BeautifulSoup


class WikiMining:

    name = ''

    def __init__(self, query=None):
        self.__extract_name(str(query))

    def __extract_name(self, query):

        if query is None:
            raise Exception('Please provide a query !!')

        elif "when is" in query and "'s" in query and ("birthday" in query or "birth day" in query or "b'day" in query):
            print("Name Extracted :", query[int(query.index("is ")) + 3: int(query.index("'s"))])
            self.name = query[int(query.index("is ")) + 3: int(query.index("'s"))]

        elif "of " in query and ("birthday" in query or "birth day" in query or "b'day" in query):
            print("Name Extracted :", query[query.index('of ') + 3: ])
            self.name = query[query.index('of ') + 3: ]

        self.__format_name()

    def __format_name(self):

        self.name.replace(' ', '_')

        self.__display_wiki_details()

    def __display_wiki_details(self):

        self.__get_wiki_bday()
        self.__get_wiki_def()

    def __get_wiki_bday(self):

        source_code = requests.get('https://en.wikipedia.org/wiki/' + self.name)
        soup = BeautifulSoup(source_code.text, "lxml")
        tds = soup.find('span', {'class' : 'bday'})
        print(tds.string)

    def __get_wiki_def(self):

        source_code = requests.get('https://en.wikipedia.org/wiki/' + self.name)
        soup = BeautifulSoup(source_code.text, "lxml")
        tds = soup.find('p')
        list = tds.find_all(text=True)
        str = ''
        for i in list:
            str += i
        print(str)
