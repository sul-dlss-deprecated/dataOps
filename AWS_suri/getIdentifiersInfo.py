import requests
from xml.etree import ElementTree
import os

druid_username = os.environ['druid_username']
druid_pword = os.environ['druid_pword']


def handler(event, context):
    """Retrieve namespace / source information from ID systems proxied."""
    sources = []

    # Handle DRUIDs
    ns_request = "https://{0}:{1}@sul-lyberservices-prod.stanford.edu/suri2/namespaces/druid"
    resp = requests.get(ns_request.format(druid_username, druid_pword)).content
    tree = ElementTree.fromstring(resp)
    for ns in tree.iter('namespace'):
        source = {}
        source['name'] = ns.find('name').text
        source['template'] = ns.find('template').text
        sources.append(source)

    return(sources)
