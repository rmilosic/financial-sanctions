import sys
import io
import os
from xml.etree.ElementTree import ElementTree, Element, SubElement
import xml.etree.ElementTree as ET

import dicttoxml

from parsers.sanctions.eu import EuSanctionsParser
from parsers.sanctions.ofac import OfacSanctionsParser

from xml.dom import minidom



def main():
    # LOAD ALL FILES IN PRESET LOCATION

    eu_file_path = os.path.join('data', 'source_files', 'consolidated-EU.xml')
    ofac_file_path = os.path.join('data', 'source_files', 'consolidated-US.xml')
    
    # parsers

    

    ofac_parser = OfacSanctionsParser()
    ofac_result = ofac_parser.parse_xml_tree(ofac_file_path)
    # final_result.append(ofac_result)

    eu_parser = EuSanctionsParser()
    eu_result = eu_parser.parse_xml_tree(eu_file_path)
    # final_result.append(eu_result)

    final_result = eu_result + ofac_result

    
    # root = ET.Element('xml')
    # root.set('version', "1.0")
    # root.set('encoding', "UTF-8")

    natural_persons = Element('natural_persons')


    # xml = dicttoxml.dicttoxml(final_result)

    # print(xml)

    for entity in final_result[0:100]:

        # print("ENTITY \n", entity)
        person = SubElement(natural_persons, 'person')

        names = SubElement(person, 'names')
        addresses = SubElement(person, 'addresses')
        date_of_births = SubElement(person, 'date_of_births')
        restrictions = SubElement(person, 'restrictions')
        documents = SubElement(person, 'documents')

        

        for name_item in entity.names:
            name = SubElement(names, 'name')

            name1 = SubElement(name, 'name1')
            name1.text = name_item.name1

            name2 = SubElement(name, 'name2')
            name2.text = name_item.name2

    
    ElementTree(natural_persons).write(
        "output2.xml", encoding="utf-8", xml_declaration=True,
        short_empty_elements=False)


    xmlstr = minidom.parseString(ET.tostring(natural_persons, encoding="utf-8", short_empty_elements=False)).toprettyxml(indent="\t")
    with open("output2_pretty.xml", "w") as f:
        f.write(xmlstr)

        # for addresses_item in person["addresses"]:
        #     address = ET.SubElement(addresses, 'address')
        #     address.text = addresses_item

        # for birth_date_item in person["date_of_births"]:
        #     birth = ET.SubElement(addresses, 'address')
        #     address.text = birth_date_item

    # print("----  OFAC RESULT ---- \n", ofac_result[0:1])
    # print("----  EU RESULT ---- \n", eu_result[0:1])
    print("----  FINAL RESULT ---- \n", final_result[0:1])



if __name__ == '__main__':
    main()