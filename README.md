# COVID Test Check
Ping my local COVID testing website and see if there is an appointment available in the date range I specified.

## Motivation:
This was just a small very simple script to ping my local COVID testing site and see if there is an available appointment. Then it will email me notifying me that there is an appointment available. Specifically, this was to make sure I got a test before Thanksgiving.

## Indended Use:
- This project isnt perfect and sometimes return false positives due to the script. I had to build it quickly and their website isnt necessarily setup well to run the request library off of. But I figured dont let perfect be the enemy of good enough. If anyone has a better way to do it I am always open to ideas/advice!
- [Link to COVID website](https://innovativecorona.com/testing/)

## Code Resources:
- **Python Version:** 3.8
- **Packages:** [requests](https://requests.readthedocs.io/en/master/), [smtplib](https://docs.python.org/3/library/smtplib.html), [ssl](https://docs.python.org/3/library/ssl.html), [email.mime.text](https://docs.python.org/3/library/email.mime.html)
