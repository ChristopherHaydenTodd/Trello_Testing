#!/usr/bin/python

class Config(object):

    @classmethod
    def get(cls, env):
        """
            Get specific config instance
        """

        if env in ('prod', 'production'):
            return cls.Production()
        elif env in ('test', 'testing', 'qa'):
            return cls.Test()
        elif env in ('dev', 'development'):
            return cls.Development()
        else:
            return None

    class Production():
        """
            Production configuration
        """

        DEBUG = False

        ###
        # Trello Configs
        ###

        TRELLO_APP_KEY =\
            'trello_key'
        TRELLO_APP_TOKEN =\
            'trello_token'

    class Test(Production):
        """
            Test/QA configuration
        """

        ###
        # Trello Configs
        ###

        TRELLO_APP_KEY =\
            'trello_key'
        TRELLO_APP_TOKEN =\
            'trello_token'

    class Development(Test):
        """
            Development configuration
        """

        DEBUG = True

