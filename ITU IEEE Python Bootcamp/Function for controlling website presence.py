import requests

#Funtion used for checking website presence
def chec_website_status(url):
  response=requests.get(url)
  if (response):
    print("Website is up and running")
    return print(response.status_code)
  else:
    print("Website is returned a status code of 404")
    return print(response.status_code)


#url=input("Enter the URL of the website to check: ")

print("https://www.ituieee.com/")
url="https://www.ituieee.com/"
chec_website_status(url)

print("\nhttps://www.ituieee.com/deneme")
url="https://www.ituieee.com/deneme"
chec_website_status(url)
