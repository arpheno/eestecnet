import urllib2

__author__ = 'swozn'
OLDHOST = "http://localhost:8010"
NEWHOST = "http://localhost:8000"
CHUNK_SIZE = 1 # dont change this motherfucker


def accounts(host, chunksize, start):
    base = host + "/legacy/accounts"
    while True:
        url = base+"?limit="+str(chunksize)+"&offset="+str(start)
        response= urllib2.urlopen(url).read()
        response=response[response.find("result"):]
        response=response[response.find("{"):response.find("}")+1]
        yield response
        start+=1

def send_account(host,data):
    url=host+"/legacy/accounts/"
    req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    try:
        f = urllib2.urlopen(req)
    except urllib2.HTTPError as e:
        # import pdb;pdb.set_trace()
        pass

if __name__ == "__main__":
    test = accounts(OLDHOST,5,0)
    for account in test:
        send_account(NEWHOST,account)

