# -*- coding: utf-8 -*-
import io
import sys
import json
from flask import Flask, render_template

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf8")

app = Flask(__name__)

with open("json/english.json", encoding="utf-8") as json_file:
    data = json.load(json_file)

# header
headers = data["headers"]

# title
title = data["title"][0]

# contact
contact = data["contact"][0]

# skills
skills_adv = data["skills_adv"]
skills_basic = data["skills_basic"]

# experience
experiences = data["experiences"]
selected = [0, 2, 1]
experiences = [experiences[idx] for idx in selected]

# projects
projects = data["projects"]
selected = [0, 1, 3]
projects = [projects[idx] for idx in selected]

# educations
educations = data["education"]

# qualifications
qualifications = data["qualifications"]


@app.route("/")
def home():
    return render_template(
        "dynamic_resume.html",
        headers=headers,
        title=title,
        experiences=experiences,
        contact=contact,
        projects=projects,
        educations=educations,
        skills_adv=skills_adv,
        skills_basic=skills_basic,
        qualifications=qualifications,
    )


if __name__ == "__main__":
    app.run(debug=True)

