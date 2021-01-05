import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

NumeSite = "www.pbinfo.ro"

sleepTimeDuration = 1.5
NrOfProblem = 0

def LogIn(driver, username, pasword) :
    driver.find_element_by_id("user").send_keys(username)
    driver.find_element_by_id("parola").send_keys(pasword)
    driver.find_element_by_xpath("//*[@id=\"form-login\"]/div/div[2]/div[4]/button").click()
    time.sleep(3)

def isproblem(driver) :
    if driver.title == NumeSite :
        return 0
    else :
        return 1

def writeProblem(driver) :
    message = driver.find_element_by_xpath("//*[@id=\"form-incarcare-solutie\"]/div[2]/div/div[6]/div[1]/div/div/div/div[5]/div/pre")
    message.send_keys(Keys.SHIFT, Keys.INSERT)
    driver.find_element_by_xpath("//*[@id=\"btn-submit\"]").click()
    time.sleep(3)


def CopyProblem(driver) :
    SolvedProblem = driver.find_element_by_xpath("//*[@id=\"zona-mijloc\"]/div/div[10]/div[2]/pre")
    SolvedProblem.click()
    SolvedProblem.send_keys(Keys.CONTROL, 'a')
    time.sleep(1)
    SolvedProblem.send_keys(Keys.CONTROL, 'c')


driverChrome = webdriver.Chrome(executable_path=r"C:\Users\jmogo\AppData\Local\Temp\Temp1_chromedriver_win32.zip\chromedriver.exe")
driverChrome.get("https://www.pbinfo.ro/")
LogIn(driverChrome, "test", "test")


driverFirefox = webdriver.Firefox(executable_path=r"C:\Users\jmogo\AppData\Local\Temp\Temp1_geckodriver-v0.28.0-win64.zip\geckodriver.exe")
driverFirefox.get("https://www.pbinfo.ro/")
LogIn(driverFirefox, "test1", "test1")


for x in range (0, 4000) :
    time.sleep(sleepTimeDuration)
    NrOfProblem += 1
    NewUrl = "https://www.pbinfo.ro/probleme/" + str(NrOfProblem)
    UrlSolOF = "https://www.pbinfo.ro/?pagina=solutie-oficiala&id=" + str(NrOfProblem)
    driverChrome.get(NewUrl)
    driverFirefox.get(NewUrl)

#Chrome cont gol
#firefox cont test

    if isproblem(driverChrome) == 1 :
        driverChrome.get(UrlSolOF)
        driverFirefox.get(UrlSolOF)
        time.sleep(1.5)
        if "numai de utilizatorii" in driverChrome.page_source:
            if "numai de utilizatorii" in driverFirefox.page_source:
                driverChrome.title
            else :
                CopyProblem(driverFirefox)
                driverChrome.get(NewUrl)
                writeProblem(driverChrome)


