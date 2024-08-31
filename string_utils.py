class StrManupulation:

    def strReverse(self, str):
        for i in range(len(str)-1, 0, -1):
            print(str[i], end = "")

    def reverse(self, str):
        str = str [::-1]
        return str
    
    def capitalize(self,str):
        str = str.upper()
        return str

