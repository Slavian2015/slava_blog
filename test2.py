class Element:

    def __init__(self, new_input):
        self.data = new_input

    @staticmethod
    def validate_lower(item):
        rep = any(map(str.islower, item))
        return rep

    @staticmethod
    def validate_upper(item):
        rep = any(map(str.isupper, item))
        return rep

    @staticmethod
    def validate_lenth(item):
        rep = 4 <= len(item) <= 6
        return rep

    @staticmethod
    def validate_number(item):
        rep = any(map(str.isdigit, item))
        return rep

    @staticmethod
    def validate_symbol(item):
        special_characters = "*#+@"
        rep = any(c in special_characters for c in item)
        return rep

    @staticmethod
    def validate_space(item):
        if any(c.isspace() for c in item):
            rep = False
        else:
            rep = True
        return rep

    def reponse(self, new_input):
        rep = []
        for i in new_input.split(","):
            if self.validate_lower(i) and \
                    self.validate_upper(i) and \
                    self.validate_lenth(i) and \
                    self.validate_number(i) and \
                    self.validate_symbol(i) and \
                    self.validate_space(i):
                rep.append(i)
        if rep:
            return rep
        else:
            return "There is no valid password"

    def __repr__(self):
        return f"{self.reponse(self.data)}"


item = Element(input("Please enter password :  "))
print(item)
