import sys
import io
import os
import logging

from parsers.sanctions.eu import EuSanctionsParser
from parsers.sanctions.ofac import OfacSanctionsParser
from parsers.sanctions.un import UnSanctionsParser

from functions import write_xml_from_parse_result
from email.send_email import send_consolidated_file_over_smtp


def main():

    logger = logging.getLogger('APP LOGGER')
    logger.setLevel(logging.INFO)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)
    # add ch to logger
    logger.addHandler(ch)


    
    logger.info('Sanctions app initiated')
    
    # TODO: get fresh data via scrapers


    # parsers

    ofac_parser = OfacSanctionsParser()
    ofac_result = ofac_parser.parse_xml_tree()
    
    # TODO: second ofac_parser

    eu_parser = EuSanctionsParser()
    eu_result = eu_parser.parse_xml_tree()


    un_parser = UnSanctionsParser()
    un_result = un_parser.parse_xml_tree()


    # join
    final_result = eu_result + ofac_result + un_result



    write_xml_from_parse_result(final_result)

    # send email
    
    # send_consolidated_file_over_smtp()


if __name__ == '__main__':
    main()