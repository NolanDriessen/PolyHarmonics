class TransformedSignalData(object):

    transformedParams = {u'Original Transform': None, u'Filter Transform': None, u'Original Freq': None, u'Filter Freq': None}

    @classmethod
    def Set_Original_Transformed_Data(transformedData,originalData):
        transformedData.transformedParams[u'Original Transform'] = originalData
    @classmethod
    def Get_Original_Transformed_Data(transformedData):
        return transformedData.transformedParams[u'Original Transform']

    @classmethod
    def Set_Filtered_Transformed_Data(transformedData,filteredData):
        transformedData.transformedParams[u'Filter Transform'] = filteredData
    @classmethod
    def Get_Filtered_Transformed_Data(transformedData):
        return transformedData.transformedParams[u'Filter Transform']

    @classmethod
    def Set_Original_Frequency_Data(transformedData,originalFreqData):
        transformedData.transformedParams[u'Original Freq'] = originalFreqData
    @classmethod
    def Get_Original_Frequency_Data(transformedData):
        return transformedData.transformedParams[u'Original Freq']

    @classmethod
    def Set_Filtered_Frequency_Data(transformedData,filteredFreqData):
        transformedData.transformedParams[u'Filter Freq'] = filteredFreqData
    @classmethod
    def Get_Filtered_Frequency_Data(transformedData):
        return transformedData.transformedParams[u'Filter Freq']
