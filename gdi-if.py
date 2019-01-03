from flask import Flask, request

http = Flask(__name__)


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


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
