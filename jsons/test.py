import urllib

for x in range(1, 612):
	testfile = urllib.URLopener()
	testfile.retrieve('https://www.easports.com/uk/fifa/ultimate-team/api/fut/item?jsonParamObject=%7B%22page%22:{}%7D'.format(x), 'file{}.json'.format(x))