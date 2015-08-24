class InputData():

    #Create the empty dictionary to avoid exceptions
    inputparams = {'Start Frequency': None, 'Stop Frequency': None, 'Step Frequency': None, 'TDMS Time': None, 'TDMS Data': None}
    @classmethod  
    def Set_Start_Freq(inputdata,Start_Freq):
        inputdata.inputparams['Start Frequency'] = Start_Freq
    @classmethod
    def Get_Start_Freq(inputdata):
        return inputdata.inputparams['Start Frequency']
        
    @classmethod
    def Set_Stop_Freq(inputdata,Stop_Freq):
        inputdata.inputparams['Stop Frequency'] = Stop_Freq
    @classmethod
    def Get_Stop_Freq(inputdata):
        return inputdata.inputparams['Stop Frequency']
        
    @classmethod  
    def Set_Step_Freq(inputdata,Step_Freq):
        inputdata.inputparams['Step Frequency'] = Step_Freq
    @classmethod
    def Get_Step_Freq(inputdata):
        return inputdata.inputparams['Step Frequency']
        
    @classmethod
    def Set_TDMS_Time(inputdata,TDMS_Time):
        inputdata.inputparams['TDMS Time'] = TDMS_Time
    @classmethod
    def Get_TDMS_Time(inputdata):
        return inputdata.inputparams['TDMS Time']
        
    @classmethod    
    def Set_TDMS_Data(inputdata,TDMS_Data):
        inputdata.inputparams['TDMS Data'] = TDMS_Data
    @classmethod
    def Get_TDMS_Data(inputdata):
        return inputdata.inputparams['TDMS Data']
