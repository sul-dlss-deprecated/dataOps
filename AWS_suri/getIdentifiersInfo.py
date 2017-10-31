import requests
from requests.packages.urllib3.util.retry import Retry
from xml.etree import ElementTree
import os
import logging
import json
import time

logger = logging.getLogger()
logger.setLevel(logging.INFO)
api_env = os.environ['api_env']
retry = Retry(
    # Maximum number of connection retries
    total = 5,
    # backoff factor is in milliseconds
    backoff_factor = .01
    )
retries = requests.adapters.HTTPAdapter(max_retries=retry)

# DRUID Namespace variables
druid_username = os.environ['druid_username']
druid_pword = os.environ['druid_pword']
suri_ns_url = "https://{0}:{1}@sul-lyberservices-{2}.stanford.edup/suri2/namespaces/druid"
druid_ns_url = suri_ns_url.format(druid_username, druid_pword, api_env)
druid_ns_url_safe = suri_ns_url.format(druid_username, "password", api_env)

def handler(event, context):
    """Retrieve namespace / source information from ID systems proxied."""
    sources = []

    # Handle DRUIDs
    logger.info('Starting a DRUID Namespace call: {0}'.format(druid_ns_url_safe))
    logger.info('Calling lyberservices test.')

    try:
        session = requests.Session()
        session.mount("https://", retries)
        resp = session.get(druid_ns_url)
        tree = ElementTree.fromstring(resp.content)
        logger.info('Parsing SURI response for DRUID Namespace.')
        for ns in tree.iter('namespace'):
            source = {}
            source['name'] = ns.find('name').text
            source['template'] = ns.find('template').text
            sources.append(source)
        return(sources)
    except requests.exceptions.RequestException as e:
        exception_class = e.__class__.__name__
        exception_msg = e
        handle_network_errors(exception_class, exception_msg)


def handle_network_errors(exception_class, exception_msg):
    api_exception_obj = {
        "isError": True,
        "type": exception_class,
        "message": exception_msg
    }

    api_exception_json = json.dumps(api_exception_obj)
    raise LambdaException(api_exception_json)

class LambdaException(Exception):
    pass
