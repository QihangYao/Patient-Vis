# Patient-Vis

Repository for group `7Under6`'s course project for Georgia Tech CSE 6242.

## DESCRIPTION

Patient-vis is a patient-centered clinical data visualizaiton tool, featuring timeline scaling, multi-condition filtering, abnormal event extraction, and flexible vital ordering. This tool is designed with the hope to reduce the doctor's cognitive load when thry explore patient's data, while maintaining the information density and fast information retrieval.

It is a web-based tool with its front-end built based upon [d3](https://d3js.org/), [jQuery](https://jquery.com/), and [dc.js](https://dc-js.github.io/dc.js/), styled using [bulma](https://bulma.io/), and its backend built primarily with [python](https://www.python.org/), [Flask](http://flask.palletsprojects.com/), [pandas](https://pandas.pydata.org/), and [NumPy](https://numpy.org/).

The [MIMIC dataset](https://mimic.physionet.org/) is used as the major reference dataset in designing this visualizaiton, which provided the reference for intensive care unit (ICU) data format and patient characteristics. While **patient-vis** contains codes for parsing of the dataset which can't be directly used on other dataset, this work should be able to generalize to other dataset with minor modification.

## INSTALLATION

Python environment with following modules is the basic requirement for running this work:
- Flask
- pandas
- NumPy

(optional) Meanwhile, this work expects a MIMIC-III database, and also provide patient record searching based on that. MIMIC-III database could be installed [locally](https://mimic.physionet.org/tutorials/install-mimic-locally-ubuntu/) or accessed through [AWS Athena](https://aws.amazon.com/blogs/big-data/perform-biomedical-informatics-without-a-database-using-mimic-iii-data-and-amazon-athena/). By Modifying the `mimic_db.py` and filling in the required fields, MIMIC-III database could be easily configured.

## EXECUTION

Run `python main.py` to set up a locally hosted webserver with a default port of 8080. If database is configured, the root entry will be a patient query page; Otherwise, it will be a demo webpage using a sample data.