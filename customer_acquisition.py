import pandas


class CustomerInfo:

    def ask_for_info(self):
        f_name = input(f"What is your first name? ").title()
        l_name = input(f"What is your last name? ").title()
        email = input(f"What is your email address? ").lower()
        confirm_email = input(f"Please confirm your email address: ").lower()
        if confirm_email == email:
            content = {
                "f_name": [f_name],
                "l_name": [l_name],
                "email": [email]
            }
            df = pandas.DataFrame(content)
            self.save_info(df)
        else:
            if input("Emails don't match. Would you like to try that again? Y or N: ").upper() == "Y":
                self.ask_for_info()
            else:
                print("Bye.")

    def save_info(self, dataframe):
        try:
            customer_info = pandas.read_csv("customer_info.csv")
        except FileNotFoundError:
            with open("customer_info.csv", "w"):
                content = {
                    "f_name": ["Huy", "Eisen"],
                    "l_name": ["Bui", "Allaire-Bui"],
                    "email": ["huy.130297@gmail.com", "eisen.ab@hotmail.com"]
                }
                df = pandas.DataFrame(content)
                df.to_csv("customer_info.csv", index=False)
        finally:
            email_list = [row["email"] for index, row in customer_info.iterrows()]
            if dataframe["email"][0] in email_list:
                print("This email already exists in the system.")
            else:
                final_df = pandas.concat([customer_info, dataframe], ignore_index=True)
                final_df.to_csv("customer_info.csv", index=False)
                print("Info added to database successfully.")

    def get_info(self):
        customer_info = pandas.read_csv("customer_info.csv")
        email_list = [row["email"] for index, row in customer_info.iterrows()]
        return email_list


# info = CustomerInfo()
# info.ask_for_info()
