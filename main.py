import requests
# pip install cssselect
from lxml import html


# start get "IF" of company
def get_if(ice):
    url = "https://simpl-recherche.tax.gov.ma/RechercheEntreprise/result"
    payload = {"param['type']": "ICE",
               "param['criteria']": ice,  # numeroIce
               "param['btnType']": "Rechercher"
               }
    r = requests.post(url, payload)
    root = html.fromstring(r.content)

    for result in root.cssselect('input#mCriteria'):
        if result.name == "param['ifu']":
            return result.value

    return
# end get "IF" of company


# start get company info
def get_company_infos(denomination):
    output = {}
    denomination = denomination.replace(" ", "%20")
    url = "https://www.directinfo.ma/directinfo-backend/api/queryDsl/search/"
    r = requests.get(url + denomination)
    results = r.json()
    # get only json info [[{jsoninfo}], count]
    results = results[0]

    if len(results) <= 0:
        # if there's no result
        output = {}
    else:
        # if there's 1 OR many results
        for result in results:
            key = results.index(result)
            output[key] = {
                'denomination': result['denomination'],
                'city': result['libelle'],
                'ice': result['numeroIce'],
                'rc': result['numeroRc'],
                'idf': get_if(result['numeroIce'])
            }

    return output
# end get company info


# rr = get_company_infos("atlantis solutions")
resl = get_company_infos("atlantis solutions")
print(resl[0]['rc'])
print(resl[1]['rc'])
for k, v in resl.items():
    print(k)
    print(v['rc'])
