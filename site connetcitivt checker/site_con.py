import urllib.request as urllib

def main(url):
      print("Checking connectivity")

      respons = urllib.urlopen(url)
      print(f"Connected to {url} succesfully")
      print(f"The respons code was: {respons.getcode()}")
      
print("This is a site connectivity checker program! ")     
url_in = input("Input the url of the site you want to check: ")

main(url_in) 