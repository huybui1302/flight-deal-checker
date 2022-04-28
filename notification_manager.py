import smtplib

EMAIL = #insert your email here
PW = #insert email password here
TO_EMAIL = #insert recipient


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_email(self, email, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PW)
            connection.sendmail(from_addr=EMAIL, to_addrs=email,
                                msg=f"Subject: Automated flight deal finder\n\nHere are some good flight deals:\n\n"
                                    f"{message}")
