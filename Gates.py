class Gate:

    """Base class for all the gates.

    Common functions like setIn, connect defined here"""

    def __init__(self, numOfInputs, type, data):

        self.numOfInputs = numOfInputs

        self.type = type

    

    def setIn(self, inNum, value):

        if inNum > self.numOfInputs:

            raise RuntimeError(f"{self.type} gate only has {self.numOfInputs} input{'(s)'}.\nCan't set input {inputNum}")

            

        if value not in [0, 1]:

            raise RuntimeError(f"Invalid state {value} for input {inputNum}")

            

        self.data[inNum] = value

    

    def connect(self, newGate, inNum):

        newGate.setIn(inNum, self.getOutput())

class Not(Gate):

    def __init__(self, in1):

        self.data = {1: in1}

        super().__init__(1, "NOT", self.data)

        

    def getOutput(self):

        return int(not self.data[1])

        

        

class Or(Gate):

    def __init__(self, in1, in2):

        self.data = {1: in1, 2: in2}

        super().__init__(2, "OR", self.data)

        

    def getOutput(self):

        return int(self.data[1] or self.data[2])

        

class And(Gate):

    def __init__(self, in1, in2):

        self.data = {1: in1, 2: in2}

        super().__init__(2, "AND", self.data)

        

    def getOutput(self):

        return int(self.data[1] and self.data[2])

class Exor(Gate):

    def __init__(self, in1, in2):

        self.data = {1: in1, 2: in2}

        super().__init__(2, "EX-OR", self.data)

        

    def getOutput(self):

        return int(self.data[1] ^ self.data[2])

class Nand(Gate):

    def __init__(self, in1, in2):

        self.data = {1: in1, 2: in2}

        super().__init__(2, "NAND", self.data)

        

    def getOutput(self):

        return int(not self.data[1] and self.data[2])
