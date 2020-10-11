import os
from xml.etree.ElementTree import ElementTree, Element, SubElement
import xml.etree.ElementTree as ET
from xml.dom import minidom


def write_xml_from_parse_result(parsed_sanction_entities):

    natural_persons = Element('natural_persons')


    for entity in parsed_sanction_entities:

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

            name3 = SubElement(name, 'name3')
            name3.text = name_item.name3

            name4 = SubElement(name, 'name4')
            name4.text = name_item.name4

            lor = SubElement(name, 'lor')
            lor.text = name_item.lor


        for address_item in entity.addresses:
            address = ET.SubElement(addresses, 'address')

            street = ET.SubElement(address, 'street')
            street.text = address_item.street

            city = ET.SubElement(address, 'city')
            city.text = address_item.city

            country = ET.SubElement(address, 'country')
            country.text = address_item.country

            lor = ET.SubElement(address, 'lor')
            lor.text = address_item.lor


        for birth_date_item in entity.birthdates:
            birth = ET.SubElement(date_of_births, 'birth')

            dob = ET.SubElement(birth, 'dob')
            dob.text = birth_date_item.dob

            pob = ET.SubElement(birth, 'pob')
            pob.text = birth_date_item.pob

            cob = ET.SubElement(birth, 'cob')
            cob.text = birth_date_item.cob

            lor = ET.SubElement(birth, 'lor')
            lor.text = birth_date_item.lor


        for document_item in entity.documents:
            document = ET.SubElement(documents, 'document')

            dty = ET.SubElement(document, 'dty')
            dty.text = document_item.dty

            did = ET.SubElement(document, 'did')
            did.text = document_item.did

            coi = ET.SubElement(document, 'coi')
            coi.text = document_item.coi

            remarks = ET.SubElement(document, 'remarks')
            remarks.text = document_item.remarks

            lor = ET.SubElement(document, 'lor')
            lor.text = document_item.lor


        for restriction_item in entity.restrictions:
            restriction = ET.SubElement(restrictions, 'restriction')

            dor = ET.SubElement(restriction, 'dor')
            dor.text = restriction_item.dor

            tor = ET.SubElement(restriction, 'tor')
            tor.text = restriction_item.tor

            sor = ET.SubElement(restriction, 'sor')
            sor.text = restriction_item.sor

            aor = ET.SubElement(restriction, 'aor')
            aor.text = restriction_item.aor

            lor = ET.SubElement(restriction, 'lor')
            lor.text = restriction_item.lor
            


    write_location = os.path.join(os.getcwd(), 'data', 'output_files')

    if not os.path.exists(write_location):
        os.makedirs(write_location)

    # ElementTree(natural_persons).write(
    #     os.path.join(write_location, "output2.xml"), encoding="utf-8", xml_declaration=True,
    #     short_empty_elements=False)


    xmlstr = minidom.parseString(ET.tostring(natural_persons, short_empty_elements=False)).toprettyxml(indent="\t", encoding="utf-8")

    with open(os.path.join(write_location, "output_consolidated.xml"), "wb") as f:
        f.write(xmlstr)

        f.close()

    print("Consolidated XML 'output_consolidated.xml' written to data/output_files ")
    

        

    # print("----  OFAC RESULT ---- \n", ofac_result[0:1])
    # print("----  EU RESULT ---- \n", eu_result[0:1])
    # print("----  FINAL RESULT ---- \n", parsed_sanction_entities[0:1])    