import requests as req
from bs4 import BeautifulSoup
import logging
from requests.exceptions import HTTPError
import links

class Request_Handler():
  def __init__(self):
    self.chapters = {} # a dictionary that contains pairs (chap_title, chap_url)
    self._init_logger()
    

  def _init_logger(self):
    self.logger = logging.getLogger()
    self.logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    self.logger.addHandler(stream_handler)

    # Just as a trial
    self.logger.info('Logger initialized!')

  def _download_homepage_data(self):
    """
    It downloades chapters' title and related link to the theory
    """
    try:
      resp = req.get(links.ROSALIND_BIOINFO_HOME)
      resp.raise_for_status()
      html = BeautifulSoup(resp.content, 'html.parser')
      self.chapters = self._build_chapters_dictionary(html)

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

  def _build_chapters_dictionary(self, html):
    """
    This method gets data from the response and build a dictionary
    """
    chapters = dict()
    try:
      for chapter in html.find_all('tbody')[0].find_all('tr'):
        key = chapter.find_all('td')[1].find_all('a')[0].text.strip()
        value = chapter.find_all('td')[1].find_all('a')[0]['href']
        
        chapters[key] = value        
    except Exception as e:
      self.logger.info('An error has occured in retrieving the chapters')
  