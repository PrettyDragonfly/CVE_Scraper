# CVE Monitoring

## Context

This repository contains a project designed to automatically monitor newly published CVEs on a daily basis. It retrieves the latest vulnerabilities, stores them in a database for tracking and analysis, and sends daily email notifications with the new CVEs to designated recipients.

## Author :bust_in_silhouette:

* **Camille Bour** _alias_ [@PrettyDragonfly](https://github.com/PrettyDragonfly)

## Usage 🚀

You need to install some packages to use the tool :
* json
* datetime
* os
* httpx
* psycopg2

For **psycopg2**, you need to install Postgres on your machine.

* **Mac OS**

    In your Terminal, run the following command:
    
  ``brew install postgresql@17``
   
    ``brew services start postgresql@17``

    
**CPE Dictionary**
You need to download the CPE dictionary and put it to the data folder:

* On this link, go to the section ``Schema Version 2.0 :  CPE Dictionary 2.0 Schema`` to download the directory:

      https://nvd.nist.gov/vuln/data-feeds#divJson20Feeds