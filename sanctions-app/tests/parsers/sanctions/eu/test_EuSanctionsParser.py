from parsers.sanctions.eu import EuSanctionsParser

import os



def test_EuParserSanctions():

    eu_sanctions_parser = EuSanctionsParser()


    # ...
    eu_sanctions_parser.parse_xml_tree(os.path.join(os.getcwd(), 'sanctions-app', 'tests', 'parsers', 'sanctions', 'files', 'eu_fsd.xml'))
    
