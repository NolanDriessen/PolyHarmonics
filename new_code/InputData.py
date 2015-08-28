class InputData(object):

    #Create the empty dictionary to avoid exceptions
    inputparams = {u'Start Frequency': None, u'Stop Frequency': None, u'Step Frequency': None, u'TDMS Time': None, u'TDMS Data': None}
    @classmethod  
    def Set_Start_Freq(inputdata,Start_Freq):
        inputdata.inputparams[u'Start Frequency'] = Start_Freq
    @classmethod
    def Get_Start_Freq(inputdata):
        return inputdata.inputparams[u'Start Frequency']
        
    @classmethod
    def Set_Stop_Freq(inputdata,Stop_Freq):
        inputdata.inputparams[u'Stop Frequency'] = Stop_Freq
    @classmethod
    def Get_Stop_Freq(inputdata):
        return inputdata.inputparams[u'Stop Frequency']
        
    @classmethod  
    def Set_Step_Freq(inputdata,Step_Freq):
        inputdata.inputparams[u'Step Frequency'] = Step_Freq
    @classmethod
    def Get_Step_Freq(inputdata):
        return inputdata.inputparams[u'Step Frequency']
        
    @classmethod
    def Set_TDMS_Time(inputdata,TDMS_Time):
        inputdata.inputparams[u'TDMS Time'] = TDMS_Time
    @classmethod
    def Get_TDMS_Time(inputdata):
        return inputdata.inputparams[u'TDMS Time']
        
    @classmethod    
    def Set_TDMS_Data(inputdata,TDMS_Data):
        inputdata.inputparams[u'TDMS Data'] = TDMS_Data
    @classmethod
    def Get_TDMS_Data(inputdata):
        return inputdata.inputparams[u'TDMS Data']
