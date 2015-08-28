class FilterData(object):

    filterparams = {u'Approximate Coefficients': None, u'Detailed Coefficients': None}

    @classmethod
    def Set_Approximate_Coefficients(filterdata,approx):
        filterdata.filterparams[u'Approximate Coefficients'] = approx
    @classmethod
    def Get_Approximate_Coefficients(filterdata):
        return filterdata.filterparams[u'Approximate Coefficients']

    @classmethod
    def Set_Detailed_Coefficients(filterdata,detail):
        filterdata.filterparams[u'Detailed Coefficients'] = detail
    @classmethod
    def Get_Detailed_Coefficients(filterdata):
        return filterdata.filterparams[u'Detailed Coefficients']
