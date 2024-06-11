import urllib.request as urlib


def main(url):
    print("checking connectivity ")

    response = urlib.urlopen(url)
    print("connected to", url, "sucessfully")
    print("the response code was :", response.getcode())


print("this is a site conectivity checker program ")
input_url = input("input the url ")
main(input_url)
