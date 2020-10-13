import pandas as pd 
import numpy as np

##########################################################################################################################################################################
# CHANGE FILE NAME IN read_scv TO CHANGE THE FILE THAT IS READ INTO THE PROGRAM
##########################################################################################################################################################################
classOptions = pd.DataFrame()
classOptions = pd.read_csv("Example.csv")
classOptions = classOptions.fillna(-1)
rows = classOptions.shape[0]
stepIteration = []
sceduleCount = 1

#remove any iterations with over laps
def chkIteration(myList):
    global stepIteration
    global sceduleCount
    schedule = pd.DataFrame()
    for c in range(len(stepIteration)):
        classStep = stepIteration[c]
        if c == 0:
            schedule = myList[c].iloc[classStep * 2: (classStep * 2) + 2]
        else:
            schedule = schedule.append(myList[c].iloc[classStep * 2: (classStep * 2) + 2])
            
        schedule.index = range(schedule.shape[0])
    valid = validate(schedule)
    if valid:
        #prints scheduel number, valid schedule, converts float64 to int64 and adds a divider for readability 
        titles = schedule.columns
        for p in range (0, len(titles)):
            if  schedule[titles[p]].dtype == np.float64:
                schedule[titles[p]] = schedule[titles[p]].astype(np.int64)

        print("##############################################################################################################################################################")
        print("Schedule #" + str(sceduleCount))
        print(schedule)
        sceduleCount += 1

def validate(mySchedule):
    days = ['M', 'T', 'W', 'R', 'F']
    global sceduleCount
    for c in range(len(days)):
        #CED stands for Classes Each Day
        CED = mySchedule[[days[c]]]

        labDay = mySchedule[["Lab_Day"]]
        labTime = mySchedule[["Lab_Time"]]
        for i in range (0, labDay.shape[0]):
            test = labDay.iloc[i, 0]
            if test != -1:
                if (str(test) == days[c]):
                    #Lab must be defined in this mannor or it will not correctly be appened onto CED
                    lab = [{days[c] : labTime.iloc[i, 0]}, {days[c] : labTime.iloc[i + 1, 0]}]
                    CED = CED.append(lab, ignore_index=True)

        #Compare start and end times of classes to see if any over laps. disregards inputs of -1 which represents NaN         
        valid = True;
        for i in range (0, int((CED.shape[0])/2)):
            startTime = CED.iloc[i * 2, 0]
            endTime = CED.iloc[i * 2 + 1, 0]
            if startTime != -1 or endTime != -1:   
                for j in range (0, int((CED.shape[0])/2)):
                    #o means other; other class. oStartTime = other class start time 
                    oStartTime = CED.iloc[j * 2, 0]
                    oEndTime = CED.iloc[j * 2 + 1, 0]
                    if j != i and oStartTime != -1 and oEndTime != -1:
                        chk1 = False
                        chk2 = False
                        
                        #Checks to see if the initial class is before the other class
                        if startTime < oStartTime and startTime < oEndTime and endTime < oEndTime and endTime < oStartTime:
                            chk1 = True
                        #Checks to see if the inital class is after the other class
                        if startTime > oStartTime and startTime > oEndTime and endTime > oEndTime and endTime > oStartTime:
                            chk2 = True
                 
                        if chk1 == False and chk2 == False:
                            return False;

    #returns true as defualt, false is returned if the scheudle is deemed to have over laps        
    return True;

                

#generations all possible iterations of classes 
def generateSchedule(mylist, currentStep):
    #mylist is a list of dataframes
    global stepIteration

    #.shape[0] returns the number of rows
    stepLength = mylist[currentStep].shape[0] / 2
    for c in range(0, int(stepLength)):
        if currentStep != (len(mylist) - 1):   
            generateSchedule(mylist, currentStep + 1)
        else:
            chkIteration(mylist)
            
        stepIteration[currentStep] += 1
        if stepIteration[currentStep] == stepLength:
            stepIteration[currentStep] = 0


#Identifies the rows in which a new class is begins
className = []
classNum = 0   
for c in range(rows):
    if c % 2 == 0:
        if classOptions.iloc[c, 0] == 1:
            className.append(classOptions.iloc[c, 2])
            classNum += 1

#Sorts each class into their own datafarm for that particular class then
#add them to a list of dataframes
classSorted = []
for c in range(classNum):
    df = classOptions.loc[classOptions['Class'] == className[c]]
    classSorted.append(df)

step = 0
generateSchedule(classSorted, step)
