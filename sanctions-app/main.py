import sys
import io
import os

from parsers.sanctions.eu import EuSanctionsParser
from parsers.sanctions.ofac import OfacSanctionsParser
from parsers.sanctions.un import UnSanctionsParser

from functions import write_xml_from_parse_result


def main():

    # parsers

    ofac_parser = OfacSanctionsParser()
    ofac_result = ofac_parser.parse_xml_tree()

    eu_parser = EuSanctionsParser()
    eu_result = eu_parser.parse_xml_tree()


    un_parser = UnSanctionsParser()
    un_result = un_parser.parse_xml_tree()

    # join
    final_result = eu_result + ofac_result + un_result


    write_xml_from_parse_result(final_result)



if __name__ == '__main__':
    main()