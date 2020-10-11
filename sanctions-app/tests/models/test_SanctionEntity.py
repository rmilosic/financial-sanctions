import pytest

from models import SanctionEntityName, SanctionEntityAddress

def test_SanctionEntityName():

    entity = {
        'name1': 'Saddam',
        'name2': 'Ali',
        'name3': None,
        'name4': None,
        'lor': 'en'
    }

    sanction_entity_name = SanctionEntityName(
        name1=entity['name1'], 
        name2=entity['name2'],
        name3=entity['name3'],
        name4=entity['name4'],
        lor=entity['lor']
    )

    assert sanction_entity_name.name1 == 'Saddam'
    assert sanction_entity_name.name3 == None

def test_SanctionEntityAddress():

    entityAddress = {
        'street': 'test street 1',
        'city': None,
        'country': 'IQ',
        'lor': 'en'
    }

    sanction_entity_name = SanctionEntityAddress(
        street=entityAddress['street'], 
        city=entityAddress['city'],
        country=entityAddress['country'],
        lor=entityAddress['lor']
    )

    assert sanction_entity_name.street == 'test street 1'
