
class SanctionEntityName:
    
    def __init__(name1, name2, name3, name4, lor):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.name4 = name4
        self.lor = lor


class SanctionEntityAddress:

    def __init__(street, city, country, lor):
        self.street = street
        self.city = city
        self.country = country
        self.lor = lor


class SanctionEntityDocument:

    def __init__(dty, did, coi, remarks, lor):
        self.dty = dty
        self.did = did
        self.coi = coi
        self.remarks = remarks
        self.lor = lor
    

class SanctionEntityRestriction:

    def __init__(dor, tor, sor, aor, lor):
        self.dor = dor
        self.tor = did
        self.sor = sor
        self.aor = aor
        self.lor = lor


class SanctionEntity:

    def __init__(names, date_of_births, addresses, documents, restrictions):

