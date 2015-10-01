import json
import urllib2

__author__ = 'swozn'
OLDHOST = "http://localhost:8010"
NEWHOST = "http://localhost:8000"
CHUNK_SIZE = 1  # dont change this motherfucker



def resource(host, start, point):
    base = host + "/legacy/" + point
    while True:
        url = base + "?limit=1"+ "&offset=" + str(start)
        try:
            response = json.loads(urllib2.urlopen(url).read())
            result= response["results"]
            if not result:
                raise StopIteration
            yield result[0]
        except:
            pass
        start += 1


def send(host, data,point):
    url = host + "/legacy/"+point+"/"
    req = urllib2.Request(url, json.dumps(data), {'Content-Type': 'application/json'})
    try:
        f = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        pass
        #print data
        # import pdb;pdb.set_trace()


if __name__ == "__main__":
    # test = accounts(OLDHOST,5,0)
    # for account in test:
    #     send_account(NEWHOST,account)
    for point in ["accounts","teams","events","entries"]:
        for res in resource(OLDHOST, 0,point):
            send(NEWHOST, res,point)
