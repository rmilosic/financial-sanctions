
class SanctionEntityName:
    
    def __init__(self, name1, name2, name3, name4, lor):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.name4 = name4
        self.lor = lor

    def __repr__(self):
        return str({
            "name1": self.name1,
            "name2": self.name2,
            "name3": self.name3,
            "name4": self.name4,
            "lor": self.lor
        })


class SanctionEntityDOB:

    def __init__(self, dob, pob, cob, lor):
        self.dob = dob
        self.pob = pob
        self.cob = cob
        self.lor = lor

    def __repr__(self):
        return str({
            "dob": self.dob,
            "pob": self.pob,
            "cob": self.cob,
            "lor": self.lor
        })


class SanctionEntityAddress:

    def __init__(self, street, city, country, lor):
        self.street = street
        self.city = city
        self.country = country
        self.lor = lor

    def __repr__(self):
        return str({
            "street": self.street,
            "city": self.city,
            "country": self.country,
            "lor": self.lor
        })

class SanctionEntityDocument:

    def __init__(self, dty, did, coi, remarks, lor):
        self.dty = dty
        self.did = did
        self.coi = coi
        self.remarks = remarks
        self.lor = lor
    
    def __repr__(self):
        return str({
            "dty": self.dty,
            "did": self.did,
            "coi": self.coi,
            "lor": self.lor
        })

class SanctionEntityRestriction:

    def __init__(self, dor, tor, sor, aor, lor):
        self.dor = dor
        self.tor = tor
        self.sor = sor
        self.aor = aor
        self.lor = lor

    def __repr__(self):
        return str({
            "dor": self.dor,
            "tor": self.tor,
            "sor": self.sor,
            "aor": self.aor,
            "lor": self.lor
        })

class SanctionEntity:

    def __init__(self):
        self.names = []
        self.birthdates = []
        self.addresses = []
        self.documents = []
        self.restrictions = []
        
    def __repr__(self):
        return str({
            "names": self.names,
            "birthdates": self.birthdates,
            "addresses": self.addresses,
            "documents": self.documents,
            "restrictions": self.restrictions
        })

