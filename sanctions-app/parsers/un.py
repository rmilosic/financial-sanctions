import os
import xml.etree.ElementTree as ET

from parsers import SanctionsParser
from models import SanctionEntity, SanctionEntityAddress, SanctionEntityDOB, SanctionEntityDocument, SanctionEntityName, SanctionEntityRestriction



class UnSanctionsParser(SanctionsParser):

    @staticmethod
    def parse_xml_tree(file_path=None):
        
        if not file_path:
            # support legacy process
            file_path = os.path.join(os.getcwd(), 'data', 'source_files', 'consolidated-UN.xml')

        try:
            tree = ET.parse(file_path)
        except FileNotFoundError:
            raise Exception("UN sanctions source file 'consolidated-UN.xml' not found in data/source_files")
        
        ns = {'export': 'http://www.w3.org/2001/XMLSchema-instance'}

        root = tree.getroot()

        # print(root.tag, root.attrib)


        entities = []

        individuals = root.find('INDIVIDUALS')

        # print("Individuals tag", individuals_tag.tag, individuals_tag.attrib)

        # get outermost child, which is sanctionEntity
        for i, sanction_entity in enumerate(individuals.findall('INDIVIDUAL')):

            # print("--------\nSanction Entity: \n", sanction_entity.tag, sanction_entity.attrib)
            
            # NEW ENTITY
            new_sanction_entity = SanctionEntity()

            # dob_tag = sanction_entity.find('export:dateOfBirthList', ns)
            # print(dob_tag)


            # ----------- BIRTHDATES
            birthdate_item = sanction_entity.find('INDIVIDUAL_DATE_OF_BIRTH')
            place_of_birth_item = sanction_entity.find('INDIVIDUAL_PLACE_OF_BIRTH')

            dob_type = birthdate_item.find('TYPE_OF_DATE')

            if dob_type == 'EXACT':
                dob = birthdate_item.find('DATE').text
            else:
                dob = None

            
            # place of birth
            if place_of_birth_item.find('CITY') is not None:
                pob = place_of_birth_item.find('CITY').text
            else:
                pob = None

            # country of birth
            if place_of_birth_item.find('COUNTRY') is not None:
                cob = place_of_birth_item.find('COUNTRY').text
            else:
                cob = None

            # language of regulation
            lor = "en"

            # new instance of birthdate
            new_birthdate = SanctionEntityDOB(
                dob=dob,
                pob=pob,
                cob=cob,
                lor=lor
            )

            new_sanction_entity.birthdates.append(new_birthdate)
                
                
            # ------ NAME ALIASES


                
            # name1
            if sanction_entity.find('FIRST_NAME') is not None:
                name1 = sanction_entity.find('FIRST_NAME', ns).text
            else:
                name1 = None
            
            # name2
            if sanction_entity.find('SECOND_NAME') is not None:
                name2 = sanction_entity.find('SECOND_NAME', ns).text
            else:
                name2 = None

            # name3
            if sanction_entity.find('THIRD_NAME') is not None:
                name3 = sanction_entity.find('THIRD_NAME', ns).text
            else:
                name3 = None

            if sanction_entity.find('FOURTH_NAME') is not None:
                name4 = sanction_entity.find('FOURTH_NAME', ns).text
            else:
                name4 = None
            
            lor = "en"
            

            new_name_alias = SanctionEntityName(
                name1=name1,
                name2=name2,
                name3=name3,
                name4=name4,
                lor=lor
            )

            new_sanction_entity.names.append(new_name_alias)

            # ------ DOCUMENTS

            document = sanction_entity.find('INDIVIDUAL_DOCUMENT')


            # TODO: map dty to codes?
            if document.find('TYPE_OF_DOCUMENT') is not None:
                dty = document.find('TYPE_OF_DOCUMENT').text
            else:
                dty = None
            
            if document.find('NUMBER') is not None:
                did = document.find('NUMBER').text
            else:
                did = None

            if document.find('ISSUING_COUNTRY', ns) is not None:
                coi = document.find('ISSUING_COUNTRY', ns).text
            else:
                coi = None

            remarks = None
            lor = "en"

            new_document = SanctionEntityDocument(
                dty=dty,
                did=did,
                coi=coi,
                remarks=remarks,
                lor=lor
            )

            new_sanction_entity.documents.append(new_document)


            # ------ RESTRICTIONS
            if sanction_entity.find('LISTED_ON') is not None:
                dor = sanction_entity.find('LISTED_ON').text
            else:
                dor = None

            tor = None
            sor = "UN"
            aor = " - ".join(filter(None, ["UN", sanction_entity.find('UN_LIST_TYPE').text, sanction_entity.find('REFERENCE_NUMBER').text]))
            lor = "en"

            new_restriction = SanctionEntityRestriction(
                dor=dor,
                tor=tor,
                sor=sor,
                aor=aor,
                lor=lor
            )
                
            new_sanction_entity.restrictions.append(new_restriction)

            # ------ ADDRESSES

    
            address_item = sanction_entity.find('INDIVIDUAL_ADDRESS')

            
            if address_item.find('COUNTRY') is not None:
                country = address_item.find('COUNTRY').text
            else:
                country = None

            if address_item.find('CITY') is not None:
                city = address_item.find('CITY').text
            else:
                city = None

            if address_item.find('STREET') is not None:
                street = address_item.find('STREET').text
            else:
                street = None
            
            lor = "en"

            new_address = SanctionEntityAddress(
                street=street,
                city=city,
                country=country,
                lor=lor
            )
            
            new_sanction_entity.addresses.append(new_address)


            # append to entities list

            entities.append(new_sanction_entity)

        # print(entities[1:15])

        return entities

            