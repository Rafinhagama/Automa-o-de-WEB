#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui
import pyperclip
import time


# In[2]:


nav =  webdriver.Chrome()


# In[3]:


nav.get('https://crm.arboimoveis.com.br/login')


# In[4]:


nav.find_element(By.NAME, 'email-login').send_keys('daniel@aradam.com.br')
nav.find_element(By.NAME, 'password').send_keys('aradamtrocar')


# In[5]:


time.sleep(2)


# In[6]:


nav.find_element('xpath', '//*[@id="content"]/div/div/section/div[2]/form/div[3]/div/button').send_keys(Keys.ENTER)

time.sleep(4)


# In[7]:


pyautogui.press("f11")
time.sleep(1)
pyautogui.click(x=13, y=273)
time.sleep(1)
pyautogui.click(x=67, y=328)


# In[8]:


nav.find_element('xpath', '//*[@id="content"]/div/section/div[1]/div/form/div[1]/div[1]/div/span[1]/button').send_keys(Keys.ENTER)
time.sleep(3)

nav.find_element(By.XPATH,'//*[@id="status_imovel"]/div/button').click()
pyautogui.click(x=644, y=927)
time.sleep(3)
pyautogui.click(x=644, y=927)
time.sleep(1)
pyautogui.click(x=644, y=927)
time.sleep(1)
pyautogui.click(x=644, y=927)
time.sleep(1)
pyautogui.click(x=644, y=927)
time.sleep(1)
pyautogui.click(x=644, y=927)


# In[9]:


time.sleep(1)
pyautogui.click(x=644, y=927)
time.sleep(1)
nav.find_element('xpath' , '//*[@id="status_imovel"]/div/ul/li[1]/div/input').send_keys("Em anúncio")
pyautogui.click(x=644, y=927)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.click(x=1765, y=555)
time.sleep(1)
pyautogui.click(x=1773, y=605)
time.sleep(1)


# In[ ]:





# In[10]:


pyautogui.hotkey("ctrl","end")
time.sleep(1)


# In[11]:


for i in range(20):
    
    pyautogui.click(x=1723, y=791)
    time.sleep(2)
    nav.find_element(By.XPATH,'//*[@id="view_imovel"]/div/form/div/div/ul/li[9]/a').click()
    time.sleep(2)
    nav.find_element(By.XPATH,'//*[@id="imv_titulo"]').click()
    time.sleep(2)
    #nav.find_element('xpath' , '//*[@id="imv_titulo"]').send_keys(".")
    pyautogui.press("backspace")
    pyautogui.press("tab")
    pyautogui.hotkey("ctrl","end")
    time.sleep(2)
    nav.find_element(By.XPATH,'//*[@id="submit-form"]').click()
    time.sleep(6)
    pyautogui.hotkey("ctrl","end")
    time.sleep(2)
    

nav.find_element(By.XPATH,'//*[@id="content"]/div/section/div[3]/div[1]/ul/li[4]/a').click()
time.sleep(2)
pyautogui.click(x=989, y=281)
pyautogui.hotkey("ctrl","end")
time.sleep(1)


# In[ ]:





# In[12]:


for i in range(15):
    
    pyautogui.click(x=1723, y=791)
    time.sleep(2)
    nav.find_element(By.XPATH,'//*[@id="view_imovel"]/div/form/div/div/ul/li[9]/a').click()
    time.sleep(2)
    nav.find_element(By.XPATH,'//*[@id="imv_titulo"]').click()
    time.sleep(2)
    #nav.find_element('xpath' , '//*[@id="imv_titulo"]').send_keys(".")
    pyautogui.press("backspace")
    pyautogui.press("tab")
    pyautogui.hotkey("ctrl","end")
    time.sleep(2)
    nav.find_element(By.XPATH,'//*[@id="submit-form"]').click()
    time.sleep(6)
    pyautogui.hotkey("ctrl","end")
    time.sleep(2)

print("Loop executado com sucesso!")

    

    


# In[13]:


time.sleep(5)
print(pyautogui.position())


# In[ ]:





# In[ ]:




