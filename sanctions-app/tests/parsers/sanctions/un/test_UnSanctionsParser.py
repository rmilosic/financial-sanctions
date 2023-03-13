from parsers.sanctions.un import UnSanctionsParser

import os



def test_OnParserSanctions():

    un_sanctions_parser = UnSanctionsParser()


    # ...
    result = un_sanctions_parser.parse_xml_tree(os.path.join(os.getcwd(), 'sanctions-app', 'tests', 'parsers', 'sanctions', 'files', 'un_consolidated.xml'))

    # assert result == None


    
