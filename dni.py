class DNI:

    @staticmethod
    def out_Letter(dniCompleted):
        dniNumbers = dniCompleted[:-1]
        return dniNumbers
    
    @staticmethod
    def correct_size(dniNumbers):
        if len(dniNumbers) == 8:
            return dniNumbers
        return False

    @staticmethod
    def transform_Int(dniNumbers):
        intNumbers = int(dniNumbers)     
        return intNumbers
    
    @staticmethod
    def resto_division(dniNumbers):
        resto = dniNumbers % 23     
        return resto
    
    @staticmethod
    def letter_dni(resto):
        diccionarioList = {0:"T", 1:"R", 2:"W", 3:"A", 4:"G", 5:"M", 6:"Y", 7:"F", 8:"P", 9:"D", 10:"X", 11:"B", 12:"N", 13:"J", 14:"Z", 15:"S", 16:"Q", 17:"V", 18:"H", 19:"L", 20:"C", 21:"K", 22:"E"}
        letter = diccionarioList[resto]
        return letter

    @staticmethod
    def compare_letters(letter, dniCompleted):
        if dniCompleted[-1] == letter:
            return True
        return False
    

