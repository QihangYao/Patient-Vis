# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 11:05:31 2019

@author: zhn
"""
import os
from flask import Flask, url_for, request, render_template, flash, jsonify, redirect
from backend import create_patient_dict
from mimic_db import conn

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/patient_info_query", methods=["GET", "POST"])
def patient_info_query():
    if request.method == "POST":

        patient_id = request.json["text"]

        error = None
        # Retrieve admission id from subject id
        cursor = conn.cursor()
        cursor.execute(
            """
                SELECT hadm_id FROM ADMISSIONS
                WHERE SUBJECT_ID = 
                """
            + str(patient_id)
        )
        hadm_id = cursor.fetchone()

        if hadm_id is None:
            error = "Input patient ID doesn't exist."
        if error is None:
            cursor.execute(
                """
                SELECT hadm_id FROM ADMISSIONS
                 WHERE subject_id = 
                 """
                + str(patient_id)
            )
            hadm_list = []
            for row in cursor:
                hadm_list.append(row[0])
            return jsonify(hadm_list)

        flash(error)

    return render_template("query-remake.html")



@app.route("/patient_query", methods=["GET", "POST"])
def patient_query():
    if request.method in ["POST", "GET"]:
        patient_id = request.form.get("p_id")
        hadm_id = request.form.get("h_id")
        if not patient_id:
            return render_template("query-remake.html")
        patient_json = create_patient_dict(conn, patient_id, hadm_id)
        return render_template("patient-vis.html", patient_data=patient_json)
    else:
        return render_template("query-remake.html")


@app.route("/")
def initialize():
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return render_template("query-remake.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
