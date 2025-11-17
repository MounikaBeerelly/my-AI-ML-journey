import pandas as pd
import matplotlib.pyplot as plt

class PatientRecord :
    def __init__(self, inPatientID, inAge, inBMI, inSmoker, inHasDisease) :
        self.inPatientID = inPatientID
        self.inAge = inAge
        self.inBMI = inBMI
        self.inSmoker = inSmoker
        self.inHasDisease = inHasDisease
        
class DieseaseProbabilityAnalyzer :
    def __init__(self) :
        self.patients = []
        
    # Adding patients
    def addPatient(self, inPatient) :
        self.patients.append(inPatient)
        
    def calculateProbabilities(self) :
        # This method calculates the compound probabilities for disease events
        
        # vars() function returns __dict__ attribute of an object i.e. it returns a dictionary of all the object attributes as name-value pairs
        df = pd.DataFrame([vars(outPatient) for outPatient in self.patients])
        
        
        