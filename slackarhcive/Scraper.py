import os
from selenium import webdriver
url = (input("Enter the url: "))
#starts firefox
driver = webdriver.Firefox()
#url = 'https://gostream.is/film/cars-3-21095/watching.html?ep=682669'
#url = 'https://gostream.is/film/the-matrix-1967/watching.html?ep=789399'
driver.get(url)
sauce = driver.page_source
#getting the true movie link
print(sauce)
#downloading
