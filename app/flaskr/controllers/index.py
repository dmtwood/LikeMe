import os
from datetime import datetime
from ..app import app, db_session
from flask import render_template, request, flash
import requests
from ..models.people import People
import os



@app.route("/")
def index():

    if not request.args.get("dir"):
        person = db_session.query(People).order_by(People.id.asc()).first()
    else:
        pass
    return render_template("index.html",
                           person=person)


@app.route("/add-people/", methods=["GET", "POST"])
def add_people():
    add_templ = "add_people.html"
    if request.method == "POST":
        try:
            qty = int(request.form.get("qty"))
        except ValueError:
            flash("Excepting a number", "error")
            return render_template(add_templ)

        if 0 < qty < 11:
            pass
            api_uri = "https://randomuser.me/api"
            for _ in range(qty):
                r = requests.get(api_uri)
                if r.status_code == 200:
                    data = r.json()
                    person = data['results'][0]
                    p = People(
                        person['name']['first'],
                        person['name']['last'],
                        person['gender'][:1].upper(),
                        person['email'],
                        datetime.strptime(person['dob']['date'], '%Y-%m-%dT%H:%M:%S.%fZ')
                    )
                    db_session.add(p)
                    db_session.flush()
                    db_session.commit()

                    person_id = p.id

                    pict_uri = person["picture"]["large"]
                    # get file ext
                    file_ext = pict_uri[pict_uri.rfind(".") + 1:]
                    # get location of file
                    filename = os.path.join(app.root_path, 'static/img/people', "".join([str(person_id), file_ext]))
                    img_resp = requests.get(pict_uri)

                    if img_resp.status_code == 200:
                        with open(filename, "wb") as file:
                            file.write(img_resp.content)

    return render_template(add_templ)
