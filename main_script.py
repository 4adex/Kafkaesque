from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


clname = ".css-175oi2r"

profile_url = "https://x.com/AmschelKavka"
driver.get(profile_url)

time.sleep(180) #Wait time to do the login
profile_url = "https://x.com/AmschelKavka"
driver.get(profile_url)

Texts = []
scroll = 0
time.sleep(5)
oldset = set()
newset = set()
crr = 0
while True:
    oldset = newset
    driver.execute_script(f"window.scrollTo(0, {scroll});")
    print("---------------------")
    time.sleep(2)
    spans = driver.find_elements(By.CSS_SELECTOR, "span.css-1jxf684.r-bcqeeo.r-1ttztb7.r-qvutc0.r-poiln3")
    texts = [span.text for span in spans]
    Texts.extend(texts)
    
    if scroll <10000:
        oldset = set(Texts)
    else:
        newset = set(Texts)
    
    scroll+=5000
    
    if oldset==newset:
        crr +=1
        
    if crr>10:
        break
    

# Close the driver
driver.quit()

real_tweets = []
for text in Texts:
    if not text:
        continue
    elif text.isnumeric():
        continue
    elif text.isspace():
        continue
    elif text =='.':
        continue
    elif text == "·":
        continue
    if not '\n\n' in text:
        continue
    elif text[-1]=='K':
        continue
    elif text[-1]=='k':
        continue
    else:
        real_tweets.append(text)

real_tweets = list(set(real_tweets))


# Open the file in write mode
with open('lines.md', 'w', encoding='utf-8') as file:
    file.write('# Quotes by Franz Kafka' +'\n')
    file.write("### Source @AmschelKavka on X" + '\n')
    ct = 0
    for line in real_tweets:
        # Write the line to the file and add a newline character
        if ct!=0:
            if len(line.split('\n\n'))==2:
                quote, cred = line.split('\n\n')
                file.write(str(ct)+'.'+'\n')
                file.write('> "'+quote+'"' +'\n')
                file.write('> \n')
                file.write('> — '+cred +'\n')
        ct+=1

print("Lines have been written to lines.md")
