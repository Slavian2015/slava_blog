
class Element:

    def __init__(self, new_input):
        self.data = new_input

    @staticmethod
    def validate(num):
        # Checking if it is only 2 numbers
        try:
            d = num.split(",")
            if len(d) == 2:
                return isinstance(int(d[0]), int) and isinstance(int(d[1]), int)
            else:
                return False
        except:
            return False

    @staticmethod
    def reformat(x, y):
        # Main logic
        arr = []
        n = 1
        for i in range(x):
            col = []
            for j in range(y):
                col.append(n)
                n += 1
            arr.append(col)
        return arr

    def __repr__(self):
        if self.validate(self.data):
            x, y = self.data.split(",")
            return f"{self.reformat(int(x), int(y))}"
        else:
            return "Input data is incorrect. Please try again"


my_inputs = []
for i in range(4):
    item = Element(input("Please enter 2 numbers :"))
    my_inputs.append(item)


for i in my_inputs:
    print(i)