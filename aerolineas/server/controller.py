from Util_Constants import messages
from validations import Code_Country

def filterById(id,listToFilter):
    for x in listToFilter:
        if x.id == id:
            return x
    return messages["NOT_FOUND"]


