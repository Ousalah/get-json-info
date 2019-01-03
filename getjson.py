import urllib.request
import json

denomination = "atlantis solutions"
print(denomination)
denomination = denomination.replace(" ", "%20")
print(denomination)
with urllib.request.urlopen("https://www.directinfo.ma/directinfo-backend/api/queryDsl/search/" + denomination) as url:
    results = json.loads(url.read().decode())
    # print(results)
    # print(len(results))

    if len(results) <= 0:
        print("there's no result")
    elif len(results) == 1:
        print("there's " + str(len(results)) + " row")
    else:
        print("there's " + str(len(results)) + " rows")

        for result in results:
            print(result)

    # fill one to many (0.0)
