from parsers.sanctions.ofac import OfacSanctionsParser

import os



def test_OfacParserSanctions():

    ofac_sanctions_parser = OfacSanctionsParser()


    # ...
    ofac_sanctions_parser.parse_xml_tree()
    
