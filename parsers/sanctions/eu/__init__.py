import xml.etree.ElementTree as ET
from .. import SanctionsParser
from models import SanctionEntity, SanctionEntityAddress, SanctionEntityDOB, SanctionEntityDocument, SanctionEntityName, SanctionEntityRestriction



class EuSanctionsParser(SanctionsParser):

    @staticmethod
    def parse_xml_tree(xml_file_path):
        

        ns = {'export': 'http://eu.europa.ec/fpi/fsd/export'}

        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        # print(root.tag, root.attrib)


        entities = []

        # get outermost child, which is sanctionEntity
        for i, sanction_entity in enumerate(root.findall('export:sanctionEntity', ns)):

            # print("--------\nSanction Entity: \n", sanction_entity.tag, sanction_entity.attrib)
            
            # NEW ENTITY
            new_sanction_entity = SanctionEntity()


            # ----------- BIRTHDATES
            for birthdate in sanction_entity.findall('export:birthdate', ns):
                
                dob = birthdate.get('birthdate')
                year_of_birth = birthdate.get('year') 
                # if exact dob is not present, we use year
                if dob == None:
                    dob = year_of_birth

                # place of birth
                pob = birthdate.get('city')

                # country of birth
                cob = birthdate.get('countryIso2Code')

                # language of regulation
                lor = birthdate.get('regulationLanguage')

                # new instance of birthdate
                new_birthdate = SanctionEntityDOB(
                    dob=dob,
                    pob=pob,
                    cob=cob,
                    lor=lor
                )

                new_sanction_entity.birthdates.append(new_birthdate)
                
                
            # ------ NAME ALIASES
            for name_alias in sanction_entity.findall('export:nameAlias', ns):
                
                name1 = name_alias.get('wholeName')
                name2 = name_alias.get('firstName')
                name3 = name_alias.get('middleName')
                name4 = name_alias.get('lastName')
                lor = name_alias.get('regulationLanguage')
                

                new_name_alias = SanctionEntityName(
                    name1=name1,
                    name2=name2,
                    name3=name3,
                    name4=name4,
                    lor=lor
                )

                new_sanction_entity.names.append(new_name_alias)

            # ------ DOCUMENTS
            for document in sanction_entity.findall('export:identification', ns):
                
                # TODO: map dty to codes?
                dty = document.get('identificationTypeCode')
                did = document.get('firstName')
                coi = document.get('countryIso2Code')
                remarks = document.find('remark')
                if remarks != None:
                    remarks = remarks.text
                lor = document.get('regulationLanguage')

                new_document = SanctionEntityDocument(
                    dty=dty,
                    did=did,
                    coi=coi,
                    remarks=remarks,
                    lor=lor
                )

                new_sanction_entity.documents.append(new_document)

            # ------ RESTRICTIONS
            for restriction in sanction_entity.findall('export:regulation', ns):
                
                dor = restriction.get('entryIntoForceDate')
                tor = "3,30" # todo: ?
                sor = "EU,US OFAC SDN" # todo: ?
                aor = str(restriction.get('regulationtype')) + " " + str(restriction.get('numberTitle'))
                lor = restriction.get('regulationLanguage')

                new_restriction = SanctionEntityRestriction(
                    dor=dor,
                    tor=tor,
                    sor=sor,
                    aor=aor,
                    lor=lor
                )
                
                new_sanction_entity.restrictions.append(new_restriction)

            # ------ ADDRESSES
            for address in sanction_entity.findall('export:address', ns):
                
                street = address.get('street')
                city = address.get('city')
                country = address.get('countryIso2Code')
                lor = address.get('regulationLanguage')

                new_address = SanctionEntityAddress(
                    street=street,
                    city=city,
                    country=country,
                    lor=lor
                )
                
                new_sanction_entity.addresses.append(new_address)


            # append to entities list

            entities.append(new_sanction_entity)

        return entities

            