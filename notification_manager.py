import smtplib

EMAIL = "landerbui13@gmail.com"
PW = "huy,pro,13,02,!"
TO_EMAIL = "huy.130297@gmail.com"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_email(self, email, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PW)
            connection.sendmail(from_addr=EMAIL, to_addrs=email,
                                msg=f"Subject: Automated flight deal finder\n\nHere are some good flight deals:\n\n"
                                    f"{message}")
