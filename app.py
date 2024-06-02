from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def scrap_jobs(known_skills):
    try:
        response = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
        soup = BeautifulSoup(response.text, 'lxml')
        jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
        job_list = []

        for job in jobs:
            date_posted = job.find("span", class_='sim-posted').text.strip()
            skills = job.find("span", class_="srp-skills").text.replace(" ", "").strip().split(",")
            if set(known_skills) & set(skills):
                company_name = job.find("h3", class_='joblist-comp-name').text.strip()
                jd = job.header.h2.a['href']
                job_list.append({
                    'company_name': company_name,
                    'skills': skills,
                    'jd': jd,
                    'date_posted': date_posted
                })

        return job_list
    except requests.RequestException as e:
        print(f"Error occurred while scraping jobs: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    known_skills = request.form.get('skills', '').split(',')
    if not known_skills:
        return render_template('error.html', message="Please provide skills")
    
    job_list = scrap_jobs(known_skills)
    return render_template('results.html', jobs=job_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
