import os
import xml.etree.ElementTree as ET

from parsers.sanctions import SanctionsParser
from models import SanctionEntity, SanctionEntityAddress, SanctionEntityDOB, SanctionEntityDocument, SanctionEntityName, SanctionEntityRestriction



class OfacSanctionsParser(SanctionsParser):

    @staticmethod
    def parse_xml_tree(file_path=None):
        

        if not file_path:
            # support legacy process
            file_path = os.path.join(os.getcwd(), 'data', 'source_files', 'consolidated-US.xml')

        try:
            tree = ET.parse(file_path)
        except FileNotFoundError as e:
            raise Exception(e)
        
        ns = {'export': 'http://tempuri.org/sdnList.xsd'}

        root = tree.getroot()

        # print(root.tag, root.attrib)


        entities = []

        # get outermost child, which is sanctionEntity
        for i, sanction_entity in enumerate(root.findall('export:sdnEntry', ns)):

            # print("--------\nSanction Entity: \n", sanction_entity.tag, sanction_entity.attrib)
            
            # NEW ENTITY
            new_sanction_entity = SanctionEntity()

            # dob_tag = sanction_entity.find('export:dateOfBirthList', ns)
            # print(dob_tag)


            # ----------- BIRTHDATES
            birthdate_items = sanction_entity.find('export:dateOfBirthList', ns)
            
            if birthdate_items is not None:

                birthdate_item = birthdate_items.find('export:dateOfBirthItem', ns)
                
                places_of_birth = sanction_entity.find('export:placeOfBirthList', ns)
                
                if places_of_birth is not None:

                    place_of_birth_item = places_of_birth.find('export:placeOfBirthItem', ns)
                
                    # print(birthdate.tag, birthdate.attrib)
                    dob = birthdate_item.find('export:dateOfBirth', ns).text
                
                    # place of birth
                    pob = place_of_birth_item.find('export:placeOfBirth', ns).text

                    # country of birth
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
                

            if sanction_entity.find('export:firstName', ns) is not None or sanction_entity.find('export:lastName', ns) is not None:

                try:
                    first_name = sanction_entity.find('export:firstName', ns).text
                except AttributeError as e:
                    first_name = None
                
                try:
                    last_name = sanction_entity.find('export:lastName', ns).text
                except AttributeError as e:
                    last_name = None

                name_combination = ' '.join(filter(None, [first_name, last_name]))

                new_name_alias = SanctionEntityName(
                        name1=name_combination,
                        name2=first_name,
                        name3=last_name,
                        name4=None,
                        lor=lor
                    )

                new_sanction_entity.names.append(new_name_alias)

            

            # ------ NAME ALIASES
            name_aliases = sanction_entity.find('export:akaList', ns)

            if name_aliases is not None:

                for name_alias in name_aliases.findall('export:aka', ns):
                    
                    # first name
                    if name_alias.find('export:firstName', ns) is not None:
                        name2 = name_alias.find('export:firstName', ns).text
                    else:
                        name2 = None
                    
                    # middle name not in xml
                    name3 = None

                    # last name
                    if name_alias.find('export:lastName', ns) is not None:
                        name4 = name_alias.find('export:lastName', ns).text
                    else:
                        name4 = None

                    # combination
                    name1 = " ".join(filter(None, [name2, name4]))
                    
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
            documents = sanction_entity.find('export:idList', ns)

            if documents is not None:

                for document in documents.findall('export:id', ns):
                    
                    # TODO: map dty to codes?
                    if document.find('export:idType', ns) is not None:
                        dty = document.find('export:idType', ns).text
                    else:
                        dty = None
                    
                    if document.find('export:idNumber', ns) is not None:
                        did = document.find('export:idNumber', ns).text
                    else:
                        did = None

                    if document.find('export:idCountry', ns) is not None:
                        coi = document.find('export:idCountry', ns).text
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
            restriction_item = sanction_entity.find('export:programList', ns)
                
            dor = root.find('export:publshInformation', ns).find('export:Publish_Date', ns).text # TODO:?
            tor = "30" # TODO:?
            sor = "US OFAC SDN"
            aor = "US Act - OFAC SDN - " + str(restriction_item.find('export:program', ns).text)
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
            addresses = sanction_entity.find('export:addressList', ns)

            if addresses is not None:

                address_item = addresses.find('export:address', ns)
                
                if address_item.find('export:address1', ns) is not None:
                    address1 = address_item.find('export:address1', ns).text
                else:
                    address1 = None
                
                if address_item.find('export:address2', ns) is not None:
                    address2 = address_item.find('export:address2', ns).text
                else:
                    address2 = None

                if address_item.find('export:address3', ns) is not None:
                    address3 = address_item.find('export:address3', ns).text
                else:
                    address3 = None

                if address1 is not None or address2 is not None or address3 is not None:
                    street = " ".join(filter(None, [address1, address2, address3]))
                else:
                    street = None

                if address_item.find('export:city', ns) is not None:
                    city = address_item.find('export:city', ns).text
                else:
                    city = None
                
                if address_item.find('export:country', ns) is not None:
                    country = address_item.find('export:country', ns).text
                else:
                    country = None
                
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
