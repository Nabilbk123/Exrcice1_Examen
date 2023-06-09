import time


from selenium import webdriver
from selenium.webdriver.common.by import By

### 1- Seconnecter au site
driver=webdriver.Chrome()
driver.get("https://videotron.com/")
driver.maximize_window()
driver.implicitly_wait(15)
### 2- Trouver le nombre d'images sur ce site:
images=driver.find_elements(By.TAG_NAME,"img")
print("Le nombre d'image sur le site est =", len(images))

### 3 - Afficher la valeur de l'attribut "alt" des images

for image in images:
    alt_attribut=image.get_attribute("alt")

    print("alt texte pour est:",alt_attribut)
print("nombre total de alt trouvés est:",len(alt_attribut))

### 4 - Trouver le nombre de liens:

liens=driver.find_elements(By.TAG_NAME,"a")
print("nombre de liens dans cette page est:",len(liens))

### 5 - Le nombre de liesn dans la section footer:

footer=driver.find_element(By.TAG_NAME,"footer")
Liens_footer=footer.find_elements(By.TAG_NAME,"a")
print("Le nombre de liens dans la section footer est: ",len(Liens_footer))
time.sleep(2)
### 6 - Attribut (href)

for lien_f in Liens_footer:
    att_footer=lien_f.get_attribute("href")
    print("href_footer texte pour est:", att_footer)

driver.quit
