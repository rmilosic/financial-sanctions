import sys
import io
import os
import logging

from parsers.sanctions.eu import EuSanctionsParser
from parsers.sanctions.ofac import OfacSanctionsParser
from parsers.sanctions.un import UnSanctionsParser

from functions import write_xml_from_parse_result
from mail.send_email import send_consolidated_file_over_smtp
from scrapers.ofac import download_ofac_non_sdn, download_ofac_sdn
from scrapers.eu_fsd import download_eu_fsd
from scrapers.un_sc_consolidated_list import download_un_consolidated

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
    
    try:
        ofac_non_sdn_path = download_ofac_non_sdn()
        ofac_sdn_path = download_ofac_sdn()
        eu_fsd_path = download_eu_fsd()
        un_consolidated_path = download_un_consolidated()

    except Exception as e:
        SystemExit(e)
    


    # parsers

    ofac_parser = OfacSanctionsParser()
    ofac_non_sdn_result = ofac_parser.parse_xml_tree(ofac_non_sdn_path)
    ofac_sdn_result = ofac_parser.parse_xml_tree(ofac_sdn_path)
    

    eu_parser = EuSanctionsParser()
    eu_result = eu_parser.parse_xml_tree(eu_fsd_path)


    un_parser = UnSanctionsParser()
    un_result = un_parser.parse_xml_tree(un_consolidated_path)


    # join
    final_result = eu_result + ofac_sdn_result + ofac_non_sdn_result + un_result



    write_xml_from_parse_result(final_result)

    # send email
    
    # send_consolidated_file_over_smtp()


if __name__ == '__main__':
    main()