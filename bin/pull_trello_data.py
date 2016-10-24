#!/usr/bin/python2.7
"""
    Purpose: Pull Trello To-Do Tasks 

    Steps:
        - Pull Board Ids for User
        - Pull List Ids for User
        - Pull Cards for Lists 

    function call: ./pull_trello_data.py
"""

import sys
import os
import logging
from trello import TrelloApi

CURRENT_PATH = os.path.realpath(sys.path[0])
FILENAME = os.path.splitext(os.path.basename(__file__))[0]
sys.path.insert(0, CURRENT_PATH + '/../')

from config.config import Config

CONFIGS = Config.get('production')
logging.basicConfig(
    level=CONFIGS.LOG_LEVEL, format=CONFIGS.LOG_FORMAT,
    datefmt=CONFIGS.LOG_DATEFORMAT, filemode=CONFIGS.LOG_FILEMODE,
    filename='{0}{1}.log'.format(CONFIGS.LOG_BASE_PATH, FILENAME))

def main():
    """
        Pull Trello To-Do Tasks
    """
    logging.info('Starting Script to Pull Trello To-Do Tasks')

    trello_board_id = get_trello_board_id()
    trello_list_ids = get_trello_list_ids(trello_board_id)

    for trello_list_id in trello_list_ids:
        print trello_list_id
        print trello_list_ids[trello_list_id]

    logging.info('Script to Pull Trello To-Do Tasks Complete')

    return


def get_trello_board_id():
    """
        Get Trello Board Id
    """
    logging.info('Pulling Trello Board Id for "To Do List"')

    trello = TrelloApi(
        CONFIGS.TRELLO_APP_KEY, CONFIGS.TRELLO_APP_TOKEN)
    trello_boards = trello.members.get_board('me')

    trello_board_id = None

    for trello_board in trello_boards:
        if trello_board['name'] == 'To Do List':
            trello_board_id = trello_board['id']

    return trello_board_id


def get_trello_list_ids(trello_board_id):
    """
        Get Trello List Ids For Trello Board
    """
    logging.info('Pulling Lists for Board Id %s', trello_board_id)

    trello = TrelloApi(
        CONFIGS.TRELLO_APP_KEY, CONFIGS.TRELLO_APP_TOKEN)
    trello_lists = trello.boards.get_list(trello_board_id)

    trello_list_ids = {}

    for trello_list in trello_lists:
        trello_list_ids[trello_list['name']] = trello_list['id']

    return trello_list_ids


if __name__ == '__main__':
    main()

