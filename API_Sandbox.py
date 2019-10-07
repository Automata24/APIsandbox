import requests
import sys

# Validate Content in API
def validateContent(parent, jsonContent, textToSearch, child = None):
    try:
        if child:
            for item in jsonContent[parent]:
                childItem = item[child]
                if textToSearch in childItem:
                    return childItem
                    print(textToSearch)

        else:
            childItem = jsonContent[parent]
            return childItem
    except:
        print('Object key does not exist')

# Get API request and store response        
try:
    response = requests.get('https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false',verify=False)
    json_response = response.json()
except:
    sys.exit('Cannot connect to API')

# Parameters for the test scenario
name = 'Carbon credits'
reList = str('True')
promoKey = 'Description'
promoKey2 = 'Name'
searchStringPromoDesc = "2x larger image"
searchStringPromoName = "Gallery"

# Call the method to validate that the search parameters exist
getName = validateContent('Name', jsonContent = json_response, textToSearch = name )
getRelist = validateContent('CanRelist', jsonContent = json_response, textToSearch = reList)
getPromoDesc = validateContent('Promotions', json_response, searchStringPromoDesc, promoKey)
getPromoName = validateContent('Promotions', json_response, searchStringPromoName, promoKey2)

# Validate that test acceptance conditions have passed
if getName == name:
    print('Success - found: ' + name)
else:
    print(name + ' does not exist')

if str(getRelist) == reList:
    print('Success - found: ' + reList)
else:
    print(reList + 'does not exist')

if (searchStringPromoDesc in getPromoDesc) and (searchStringPromoName in getPromoName):
    print('Success - found: ' + searchStringPromoName + ' + ' + searchStringPromoDesc )
else:
    print(searchStringPromoDesc + 'under ' + searchStringPromoName + ' does not exist')
