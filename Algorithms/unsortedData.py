class unsortedData:
    def __init__(self, unsortedList, focusNode, iterativeNode, completion, switchPlaces):
        self.unsortedList = unsortedList
        self.focusNode = focusNode
        self.iterativeNode = iterativeNode
        self.completion = completion
        self.switchPlaces = switchPlaces

    def getUnsortedList(self):
        return self.unsortedList

    def getFocusNode(self):
        return self.focusNode

    def getIterativeNode(self):
        return self.iterativeNode
    
    def getCompletion(self):
        return self.completion

    def getSwitchPlaces(self):
        return self.switchPlaces

    def setUnsortedList(self, unsortedList):
        self.unsortedList = unsortedList

    def setFocusNode(self, focusNode):
        self.focusNode = focusNode

    def setIterativeNode(self, iterativeNode):
        self.iterativeNode = iterativeNode
    
    def setCompletion(self, completion):
        self.completion = completion

    def setSwitchPlaces(self, switchPlaces):
        self.switchPlaces = switchPlaces