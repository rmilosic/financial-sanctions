import xml.etree.ElementTree as ET
from parsers.sanctions import SanctionsParser
from models import SanctionEntity, SanctionEntityAddress, SanctionEntityDOB, SanctionEntityDocument, SanctionEntityName, SanctionEntityRestriction



class EuSanctionsParser(SanctionsParser):

    @staticmethod
    def parse_xml_tree(xml_file_path):
        

        ns = {'export': 'http://eu.europa.ec/fpi/fsd/export'}

        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        print(root.tag, root.attrib)


        entities = []

        # get outermost child, which is sanctionEntity
        for i, sanction_entity in enumerate(root.findall('export:sanctionEntity', ns)):

            # print("--------\nSanction Entity: \n", sanction_entity.tag, sanction_entity.attrib)
            
            # empty lists for 
            new_sanction_entity = SanctionEntity()


            # ----------- BIRTHDATE
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
                
                

            for name_alias in sanction_entity.findall('export:nameAlias', ns):
                
                whole_name = name_alias.get('wholeName')
                

                new_name_alias = SanctionEntityName()

            #     print(name_alias.tag, name_alias.attrib)
            
            # print(new_sanction_entity)
            
            if i > 3:
                break
            
            