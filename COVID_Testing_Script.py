import requests
import smtplib,ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

url = 'https://nextpatient.co/p/1118/13313/schedule-widget.js?id=1'

r = requests.get(url)

website_text = r.text

# I am looking to get a test on November 20th, 21st, or 22nd
# I know that the date format for those dates will be Fri, Nov 20 ; Sat, Nov 21; Sun, Nov 22
# I will need to search for those specific strings
# If the string sorry exsists anywhere do nothing
# if all the checks are equal to -1 do nothing
# if one of the checks gives an index see if there is a time associated with it

def send_email_function():
    port = 465
    password = ""

    sender_email = ""
    receiver_email = ""

    message = MIMEMultipart("alternative")
    message["Subject"] = "COVID Test Available"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """    There appears to be an open appointment available for November 20/21/22.
    Link: https://innovativecorona.com/testing/
    """
    html = """    <html>
        <body>
            <p> There appears to be an open appointment available for November 20/21/22.<br>
            Link: <a href="https://innovativecorona.com/testing/">Link</a>
            </p>
        </body>
    </html>"""

    part1 = MIMEText(text,"plain")
    part2 = MIMEText(html,"html")

    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",port,context = context) as server:
        server.login("grantculpautomated@gmail.com",password)
        server.sendmail(sender_email,receiver_email,message.as_string())
    return "Sent Email"



fri_check = website_text.find("Fri, Nov 20")
sat_check = website_text.find("Sat, Nov 21")
sun_check = website_text.find("Sun, Nov 22")
appointment_check = website_text.find("Sorry")

if fri_check != -1 and sat_check != -1 and sun_check != -1:
    if appointment_check == -1:
            send_email_function()
    else:
        print("Day does exist but no appointments")
else:
    print("Day does not exist yet do nothing")
