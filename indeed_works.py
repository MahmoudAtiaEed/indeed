import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import streamlit as st



class indeed:
    df = pd.DataFrame({"jop title": [],
                       "company ": [],
                       "company location": [],
                       "date": [],
                    #  "summary": [],
                     # "link ": []
                       })
    def __init__(self, url ): # what i want to do when i call the class , i want to create a dataframe, functions what the user want
        self.url = url
        html = requests.get(self.url)
        soup = bs(html.content, "lxml")
        jops = soup.find_all(class_="job_seen_beacon")
        time.sleep(7)
        for jop in jops:
            title = jop.find(class_="jobTitle").text
            company = jop.find(class_="companyName").text
            company_location = jop.find(class_="companyLocation").text
            date = jop.find(class_="date").text
            summary = jop.find(id="jobDescriptionText")
            link = jop.find("a",class_="jcs-JobTitle" ).get("href")
            self.df.loc[len(self.df.index)] = [title, company, company_location, date
               # , summary
             #, f"https://tr.indeed.com{link}"
            ]
           
    def get_jops(self):
        return(self.df)

url = st.text_input("paste an indeed url")
b = st.button("see data frame")
if b:
    jop = indeed(url)

    st.table(jop.get_jops())
