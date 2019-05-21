'''
Created on 17 Sep 2015

@author: seamusmurphy
'''
from framework.services.common.rabbit_client import RabbitmqClient
from pkg_resources import ResourceManager
import logging
import json

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class TestSetupEvironment(object):
    '''
        Class is used to setup Environment details for ATs.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.rm = ResourceManager()
        self.rmq_client = RabbitmqClient()

    def clean_environment_test(self):
        '''
            Clean environment.
        '''
        logger.info('Tear down environment')
        self.rmq_client.publish_message(message=json.dumps({}), routing_key='mb.model.clean.request',
                                        header={'event-class': 'mb.eventbus.events.model.CleanModelRequestEvent'},
                                        callback_binding='mb.model.cleaned', )
