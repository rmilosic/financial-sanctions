import sys
import io
import os

from parsers.sanctions.eu import EuSanctionsParser
from parsers.sanctions.ofac import OfacSanctionsParser

from functions import write_xml_from_parse_result


def main():
    # LOAD ALL FILES IN PRESET LOCATION

    eu_file_path = os.path.join('data', 'source_files', 'consolidated-EU.xml')
    ofac_file_path = os.path.join('data', 'source_files', 'consolidated-US.xml')
    
    # parsers

    ofac_parser = OfacSanctionsParser()
    ofac_result = ofac_parser.parse_xml_tree(ofac_file_path)

    eu_parser = EuSanctionsParser()
    eu_result = eu_parser.parse_xml_tree(eu_file_path)

    # join
    final_result = eu_result + ofac_result


    write_xml_from_parse_result(final_result)



if __name__ == '__main__':
    main()