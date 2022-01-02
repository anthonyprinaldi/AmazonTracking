import smtplib


def sendMsg(body: str) -> None:
    smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login("anthony.rinaldi04@gmail.com", "mxsrhrypjgkoposc")
    smtpObj.sendmail("anthony.rinaldi04@gmail.com", "6479914878@pcs.rogers.com", body)
    smtpObj.quit()


if __name__ == "__main__":
    sendMsg("test message")
