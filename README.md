# GTP logs in ELK

## Setup
* Clone the repo
  * `git clone https://github.com/madelinemccombe/gtp_elk.git`
* Create virtual environment
  * `python3 -m venv env`
  * `source env/bin/activate`
* Install packages
  * All at once:
     * `pip install -r requirements.txt`
  *  _OR_ individually:
     * `pip install eland`
     * `pip install datetime`

## Files
* test_elk_connection.py
  * Edit `lines 38-39` to reflect the IP address and index name of the ELK stack and data of interest
  * _Output: information about the index, number of entries in index, and event code distribution_

* ELK_GTP_processing.py
  * Edit `lines 38-39` to reflect the IP address and index name of the ELK stack and data of interest
  * Edit `line 40` to  reflect the number of minutes of data to analyze, starting from the most recent entry (default 15)
  * _Output: IMSI/IMEI pair statistics, count of potentially fraudulent IMSIs_


