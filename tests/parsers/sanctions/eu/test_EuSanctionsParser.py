from parsers.sanctions.eu import EuSanctionsParser

import os



def test_EuParserSanctions():

    eu_sanctions_parser = EuSanctionsParser()


    # ...
    eu_sanctions_parser.parse_xml_tree(os.path.join(os.path.dirname(__file__), 'consolidated-EU.xml'))
    
