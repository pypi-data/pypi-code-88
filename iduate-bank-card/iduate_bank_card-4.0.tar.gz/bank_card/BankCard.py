class BankCard():
    """ The purpose of BankCard class is for calculating checksum from card number and 
    if it is divisible by 10 which would be a valid card number by luhn's algorithm.
    
    Attributes:
        number (int) bank card number
        checksum (int) representing the checksum of the bank card number
        isValid (boolean) representing whether the bank card number is valid or not
            
    """
    def __init__(self, num):
        
        self.number = num
        self.checksum = self.luhn_checksum()
        self.isValid = self.luhn_isValid()
        self.reason = self.isValid_reason()
    
    def luhn_checksum(self):
    
        """Method to calculate the checksum of the credit card number.
        
        Args: 
            None
        Returns: 
            int: checksum of the bank card number
    
        """
        
        cc_num = []
        results = []
        num_str = str(self.number)

        for i in range(len(num_str)):
    
            cc_num.append(num_str[i])
            cc_num_r = cc_num[::-1]
    
        for i in range(len(cc_num_r)):
    
            if (i + 1) % 2 == 0:
                result = int(cc_num_r[i]) * 2
                results.append(sum(int(i) for i in str(result)))
            else:
                results.append(int(cc_num_r[i]))

        checksum = sum(results)
        
        return checksum
    
    def luhn_isValid(self):
    
        """Method to calculate whether card number is valid by Luhn's algorithm.
        
        Args: 
            None
        Returns: 
            boolean: True/False
    
        """
        if len(str(self.number)) < 8:
            Valid = False
        
        else:
            Valid = (self.checksum % 10 == 0)
            
        return Valid
    
    def isValid_reason(self):
    
        """Method to give user reason as to why card is valid or invalid.
        
        Args: 
            None
        Returns: 
            string: reason
    
        """
        if len(str(self.number)) < 8:
            reason = "Number does not meet minimum requirements"
        else:
            reason = "checksum"
        
        self.isValid_reason = reason
        return reason