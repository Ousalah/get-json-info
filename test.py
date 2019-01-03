import requests
# pip install cssselect
from lxml import html
"""  WORK

url = "https://simpl-recherche.tax.gov.ma/RechercheEntreprise/result"
payload = {"param['type']": "ICE",
           "param['criteria']": '001986619000056',  # numeroIce
           "param['btnType']": "Rechercher"
           }
#
# payload = {"param['type']": "RC",
#            "param['criteria']": numeroRc, # 388705
#            "param['codeRC']": libelle, # CASABLANCA
#            "param['btnType']": "Rechercher"
#            }

# r = requests.request("POST", url, data=payload, headers=headers)
r = requests.post(url, payload)
root = html.fromstring(r.content)

for result in root.cssselect('input#mCriteria'):
    if result.name == "param['ifu']":
        print(result.value)
"""

denomination = "atlantis solutions"
print(denomination)
denomination = denomination.replace(" ", "%20")
print(denomination)
url = "https://www.directinfo.ma/directinfo-backend/api/queryDsl/search/"
print(url + denomination)
r = requests.get(url + denomination)
# print(r.text.json())
print(r.json())

""" EXAMPLE
@http.route('/customer/company/getinfo/', type='json', auth='user')
def get_company_infos(self, **kwargs):
    data = request.jsonrequest
    # print( str(data) )
    url = "https://simpl-recherche.tax.gov.ma/RechercheEntreprise/result"
    payload = "param%5B'type'%5D=IF&param%5B'criteria'%5D=" + \
        data['idf'] + "&param%5B'codeRC'%5D=552&param%5B'btnType'%5D=Rechercher"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "e1fcc6dd-d4d1-4483-b133-90d1dd6639da"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    d = pq(response.text)
    elements = d("#mCriteria")
    infos = []
    for elem in elements:
        infos.append(elem.attrib['value'])
    return json.dumps(infos)

"""
