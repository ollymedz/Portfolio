
import requests
import urllib
import requests_cache


requests_cache.install_cache('cache_data')


def main():

    file_name = 'domain-names.txt'

    suspicious = []

    f = open(file_name, "r")#oppen in read mode
    for x in f:

        if "-" not in x:
            continue

        if "apple" in x and "support" in x:
            print("suspicious address found"+ x)
            suspicious.append(x.replace('\n', ''))

        elif "apple" in x and "id" in x:
            print("suspicious address found"+ x)
            suspicious.append(x.replace('\n', ''))

        elif 'barclays' in x:
            print("suspicious address found"+ x)
            suspicious.append(x.replace('\n', ''))


        elif 'icloud' in x:
            print("suspicious address found"+ x)
            suspicious.append(x.replace('\n', ''))


        elif 'paypal' in x:
            print("suspicious address found"+ x)
            #suspicious.append(x)
            suspicious.append(x.replace('\n', ''))

        elif 'facebook' in x:
            print("suspicious address found"+ x)
            #suspicious.append(x)
            suspicious.append(x.replace('\n', ''))

        elif 'microsoft' in x:
            print("suspicious address found"+ x)
            suspicious.append(x.replace('\n', ''))

        elif 'outlook' in x:
            print("suspicious address found"+ x)
            suspicious.append(x.replace('\n', ''))

        elif 'webapp' in x:
            print("suspicious address found"+ x)
            suspicious.append(x.replace('\n', ''))

        elif 'netflix' in x:
            print("suspicious address found"+ x)
            suspicious.append(x.replace('\n', ''))

        elif 'dhl' in x:
            print("suspicious address found"+ x)
            suspicious.append(x.replace('\n', ''))

        elif 'dropbox' in x:
            print("suspicious address found"+ x)
            suspicious.append(x.replace('\n', ''))

        elif 'wells' in x and 'fargo' in x :
            print("suspicious address found" + x)
            suspicious.append(x.replace('\n', ''))

    f.close()
