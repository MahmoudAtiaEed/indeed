import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import streamlit as st

url = st.text_input("paste an indeed url")

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
    def jops_num(self):
        print(len(self.df.index))
    def jops_excel(self):
        try:
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')  # finding desktop path windows
        except:
            desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')  # or finding it in mac
        path = desktop + "\indeed jops"  # path to creating the direktory

        with open(path, "w")as f:
            self.df.to_excel(f)

b = st.button("see data frame")
if b:
    jop = indeed(url)

    st.table(jop.get_jops())
