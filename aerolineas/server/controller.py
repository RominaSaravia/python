from Util_Constants import messages
from validations import Code_Country
from fastapi import  Cookie

def filterById(id,listToFilter):
    for x in listToFilter:
        if x.id == id:
            return x
    return messages["NOT_FOUND"]


def auth_user(requestData : Cookie):
    return requestData.cookies.get('loggedUser')
