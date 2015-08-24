class TransformedSignalData():

    transformedParams = {'Original Transform': None, 'Filter Transform': None, 'Original Freq': None, 'Filter Freq': None}

    @classmethod
    def Set_Original_Transformed_Data(transformedData,originalData):
        transformedData.transformedParams['Original Transform'] = originalData
    @classmethod
    def Get_Original_Transformed_Data(transformedData):
        return transformedData.transformedParams['Original Transform']

    @classmethod
    def Set_Filtered_Transformed_Data(transformedData,filteredData):
        transformedData.transformedParams['Filter Transform'] = filteredData
    @classmethod
    def Get_Filtered_Transformed_Data(transformedData):
        return transformedData.transformedParams['Filter Transform']

    @classmethod
    def Set_Original_Frequency_Data(transformedData,originalFreqData):
        transformedData.transformedParams['Original Freq'] = originalFreqData
    @classmethod
    def Get_Original_Frequency_Data(transformedData):
        return transformedData.transformedParams['Original Freq']

    @classmethod
    def Set_Filtered_Frequency_Data(transformedData,filteredFreqData):
        transformedData.transformedParams['Filter Freq'] = filteredFreqData
    @classmethod
    def Get_Filtered_Frequency_Data(transformedData):
        return transformedData.transformedParams['Filter Freq']
