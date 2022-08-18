from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = r"C:\Users\bodriscoll\Documents\ChromeDriver\chromedriver.exe"

def freeEnergy(fragmentCode):

    web = webdriver.Chrome(path)
    web.get('http://www.unafold.org/mfold/applications/dna-folding-form.php')

    time.sleep(2)

    fragmentName="BODtest"

    webpageNameBox = web.find_element_by_xpath('/html/body/main/div[2]/form/div[1]/input')
    webpageNameBox.send_keys(fragmentName)
    webpageCodeBox = web.find_element_by_xpath('/html/body/main/div[2]/form/div[2]/textarea')
    webpageCodeBox.send_keys(fragmentCode)
    Submit = web.find_element_by_xpath('/html/body/main/div[2]/form/input[6]')
    Submit.click()

    time.sleep(5)

    main = web.find_element_by_xpath("/html/body/main")

    # Now find the delta symbol:
    textOut=main.text
    index=0
    valueList=[]
    while index < len(textOut):
        index = textOut.find("Δ",index)
        index2=textOut.find("kcal/mol", index)
        if index == -1:
            break

        value=(textOut[index+5:index2])
        valueList.append(float(value))
        index +=1

    web.quit()

    return(valueList)


if __name__ == "__main__":
    print("Started in here")
    codeTest="AAGATAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTGAGTAGCTAGCTAGCTAGCTAGCTAGCAT"
    codeTest1="TAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTGAGTAGCTAGCTAGCTAGCTAGCTAGCAT"
    a=freeEnergy(codeTest1)
    print("The list of free energy outputs is",a)
# ΔG = -62.70 kcal/mol,


# /html/body/main/div[2]/p[8]/text()[1]

# LastName = "Kattimani"
# last = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
# last.send_keys(LastName)

# FirstName = "Rishab"
# first = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
# first.send_keys(FirstName)

# RadioButtonPeriod = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]/label/div/div[1]/div/div[3]/div')
# RadioButtonPeriod.click()

# Submit = web.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
# Submit.click()

# get_confirmation_div_text = web.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
# print(get_confirmation_div_text.text)
# if ((get_confirmation_div_text.text) == "Thank you for attending"):
#     print ("Test Was Successful")
# else:
#     print("Test Was Not Successful")