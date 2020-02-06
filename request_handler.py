import requests as req
from bs4 import BeautifulSoup
import logging
from requests.exceptions import HTTPError
import links
import sys

class Request_handler():
  def __init__(self):

    # A dictionary that contains pairs (chap_title, chap_url)
    self._download_homepage_data()
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
        self.logger.error(f'HTTP error occurred: {http_err}')
        self.logger.info('Bye.')
        sys.exit(-1)

    except Exception as err:
        self.logger.error(f'Other error occurred: {err}')  
        sys.exit(-2)  
    
    else:
        self.logger.info('Success!')

  def _build_chapters_dictionary(self, html):
    """
    This method gets data from the response and build a dictionary

    input
    - html: html of the page to scrap
    """
    chapters = dict()
    try:
      for chapter in html.find_all('tbody')[0].find_all('tr'):
        key = chapter.find_all('td')[1].find_all('a')[0].text.strip()
        value = chapter.find_all('td')[1].find_all('a')[0]['href']
        chapters[key] = value 
      return chapters
    except Exception as e:
      self.logger.error(e)

  def print_chapters(self):
    """
    It prints all the chapters already downloaded
    """
    for i, (k, v) in enumerate(self.chapters.items()):
      print(f"Chapter {i} -- {k}")

  def read_chapter(self, chapter_num):
    """
    Download and print the theory of the specified chapter

    input
    - chapter_num: chapter index
    """
    assert len(self.chapters) < chapter_num, self.logger.error('Plase provide a valid chapter')


  