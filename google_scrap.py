import undetected_chromedriver as uc
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

import urllib
import time
import threading
import winsound
import msvcrt

# Cette fonction sera exécutée dans un thread pour attendre l'entrée de l'utilisateur
def wait_for_input():
    global continue_execution 
    continue_execution = True
    
    # Définir la durée maximale d'attente en secondes
    max_wait_time = 5
    
    try:
        print(f"\nDo you want to continue? Press Enter to continue, or type 'exit' to stop (Timeout in {max_wait_time} seconds): ")
        # Attendre au maximum max_wait_time secondes avant de se terminer
        start_time = time.time()
        while continue_execution and time.time() - start_time < max_wait_time:
            if msvcrt.kbhit():
                # Si une touche est enfoncée, terminer le thread
                key = msvcrt.getch().decode('utf-8').lower()
                if key == '\r':
                    # Entrée pressée, continuer le script
                    return
                elif key == 'e':
                    # 'e' pressée, arrêter le script
                    continue_execution = False
                    return
            time.sleep(0.1)
        
    except KeyboardInterrupt:
        # Cette exception se produit lorsque l'utilisateur appuie sur Ctrl+C
        pass
    
    # Si le temps est écoulé, terminer le thread
    if continue_execution:
        print("\nTime is up. Exiting the script.")
        exit()

def play_notification_sound():
    # Jouer un son pour notifier l'utilisateur
    winsound.PlaySound('sound.wav', winsound.SND_FILENAME) 


# Configure WebDriver
driver_path = "Users/[your path]/chromedriver-win64"  # Replace with the actual path to the downloaded driver

#La liste de mot clé principale
list = [ 
    "nature",
    "maison",
    "manoir",
    "montagne",
    "plage",
    "lac",
    "chateaux"
]

#Les vues que l'on souhaite associer à chaque terme
views = {
    '' : 1000,
    'été' : 1000,
    'hiver' : 1000,
    'automne' :1000,
    'printemps' : 1000,
    'jour' : 1000,
    'nuit' : 1000
    }

# Launch Browser and Open the URL
counter = 0
tmp = 0

def get_chrome_options():
    options = webdriver.ChromeOptions()
    #options.add_argument("start-maximized")
    options.add_argument("enable-automation")
    options.add_argument(f'--user-data-dir={"/Users/[your path]/Local/Google/Chrome/User Data"}')
    #options.add_argument('--incognito')
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-application-cache')
    options.add_argument('--disable-gpu')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-browser-side-navigation")  
    options.add_argument("--headless=new")
    #options.add_argument(f'--proxy-server={proxy}')
    return options

#Boucle d'ittération de scrapping
for model in list:
    verif = 0
    for angle, num_of_pics in views.items():
        if (tmp>=0):
            try:
                options = get_chrome_options()
                driver = uc.Chrome(options=options)
                url = str("https://www.google.com/search?q={0}+{1}&hl=en&tbm=isch&sxsrf=APwXEdeMCCcn15mo1obWv-xVcr_tpnFYQg%3A1684476865544&source=hp&biw=1737&bih=1032&ei=wRNnZNX-HtX4kPIP9umT2AY&iflsig=AOEireoAAAAAZGch0VXQnHgSIAIKBwcg5h0gf-nJjQvD&oq=toyota+supr&gs_lcp=CgNpbWcQAxgAMgQIIxAnMgQIIxAnMggIABCABBCxAzIICAAQgAQQsQMyBQgAEIAEMggIABCABBCxAzIICAAQgAQQsQMyCAgAEIAEELEDMggIABCABBCxAzIICAAQgAQQsQM6BwgjEOoCECc6CAgAELEDEIMBOgQIABADOgkIABAYEIAEEApQlglY7SNgpSxoB3AAeAGAAZIBiAHkDJIBBDEwLjeYAQCgAQGqAQtnd3Mtd2l6LWltZ7ABCg&sclient=img&safe=off".format(model, angle))        
                driver.get(url)

                # The execute script function will scroll down the body of the web page and load the images.
                driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                time.sleep(10)
                if num_of_pics > 50:
                    for _ in range(0, 3):
                        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                        time.sleep(10)
                elif num_of_pics > 20:
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
                    time.sleep(10)

                # Review the Web Page’s HTML Structure

                # We need to understand the structure and contents of the HTML tags and find an attribute that is unique only to images.
                img_results = driver.find_elements(By.XPATH, "//img[contains(@class, 'Q4LuWd')]")

                image_urls = []
                for img in img_results:
                    image_urls.append(img.get_attribute('src'))

                folder_path = '[Choose a path for your image]' + model  # change your destination path here
                modified_name = model.replace("+", " ")

                try:
                    os.makedirs(folder_path, exist_ok=True)
                except OSError as e:
                    print(f"Creation of the directory {folder_path} failed: {e}")

                for i in range(num_of_pics):
                    counter += 1
                    try:
                        urllib.request.urlretrieve(str(image_urls[i]), os.path.join(folder_path, "{0}_{1}_{2}.jpg".format(modified_name,counter,angle)))
                    except Exception as e:
                        counter = counter
                        #print(f"Failed to download image {i+1} for {model}: {e}")
                # Always close and quit the driver to avoid resource leaks
                if driver:
                    driver.close()
                    driver.quit()
                    del driver
            finally:
                print(model, ' ', angle)
        verif+=1  
    #Effet sonore
    play_notification_sound()
    # Créer un thread pour attendre l'entrée de l'utilisateur
    input_thread = threading.Thread(target=wait_for_input)
    input_thread.start()
    # Attendre que le thread se termine ou que l'utilisateur appuie sur Enter
    input_thread.join(timeout=6.0)
    # Si l'utilisateur n'a pas répondu, le thread sera terminé et le script continuera
    if continue_execution:
        print("Continuing...")
    else:
        print("Exiting the script.")
        exit() 
    # Sauvegarder la valeur de tmp dans le fichier texte
    tmp+=1
    counter = 0
