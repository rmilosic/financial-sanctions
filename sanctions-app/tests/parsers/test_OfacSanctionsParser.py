from parsers.ofac import OfacSanctionsParser

import os



def test_OfacParserSanctions():

    ofac_sanctions_parser = OfacSanctionsParser()


    # ...
    ofac_sanctions_parser.parse_xml_tree(os.path.join(os.getcwd(), 'sanctions-app', 'tests', 'parsers', 'files', 'ofac_non_sdn.xml'))
    
