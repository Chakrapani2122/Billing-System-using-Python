import streamlit as st
import random
import os

# ============main============================
class Bill_App:
    def __init__(self):
        self.initialize_variables()
        self.create_ui()

    def initialize_variables(self):
        self.items = {
            "sanitizer": 0,
            "mask": 0,
            "hand_gloves": 0,
            "dettol": 0,
            "newsprin": 0,
            "thermal_gun": 0,
            "rice": 0,
            "food_oil": 0,
            "wheat": 0,
            "daal": 0,
            "flour": 0,
            "maggi": 0,
            "sprite": 0,
            "limka": 0,
            "mazza": 0,
            "coke": 0,
            "fanta": 0,
            "mountain_duo": 0
        }
        self.prices = {
            "sanitizer": 30,
            "mask": 10,
            "hand_gloves": 20,
            "dettol": 50,
            "newsprin": 10,
            "thermal_gun": 80,
            "rice": 500,
            "food_oil": 110,
            "wheat": 60,
            "daal": 30,
            "flour": 35,
            "maggi": 20,
            "sprite": 110,
            "limka": 55,
            "mazza": 45,
            "coke": 60,
            "fanta": 35,
            "mountain_duo": 20
        }
        self.medical_price = ""
        self.grocery_price = ""
        self.cold_drinks_price = ""
        self.c_name = ""
        self.c_phone = ""
        self.bill_no = str(random.randint(1000, 9999))
        self.search_bill = ""
        self.medical_tax = ""
        self.grocery_tax = ""
        self.cold_drinks_tax = ""
        self.total_bill = 0.0
        self.bill_content = ""

    def create_ui(self):
        st.title("Billing Software")

        st.header("Customer Details")
        self.c_name = st.text_input("Name")
        self.c_phone = st.text_input("Phone Number")
        self.search_bill = st.text_input("Bill Number")
        if st.button("Search"):
            self.find_bill()

        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("Medical Purpose")
            self.items["sanitizer"] = st.number_input("Sanitizer", min_value=0)
            self.items["mask"] = st.number_input("Mask", min_value=0)
            self.items["hand_gloves"] = st.number_input("Hand Gloves", min_value=0)
            self.items["dettol"] = st.number_input("Dettol", min_value=0)
            self.items["newsprin"] = st.number_input("Newsprin", min_value=0)
            self.items["thermal_gun"] = st.number_input("Thermal Gun", min_value=0)

        with col2:
            st.header("Grocery Items")
            self.items["rice"] = st.number_input("Rice", min_value=0)
            self.items["food_oil"] = st.number_input("Food Oil", min_value=0)
            self.items["wheat"] = st.number_input("Wheat", min_value=0)
            self.items["daal"] = st.number_input("Daal", min_value=0)
            self.items["flour"] = st.number_input("Flour", min_value=0)
            self.items["maggi"] = st.number_input("Maggi", min_value=0)

        with col3:
            st.header("Cold Drinks")
            self.items["sprite"] = st.number_input("Sprite", min_value=0)
            self.items["limka"] = st.number_input("Limka", min_value=0)
            self.items["mazza"] = st.number_input("Mazza", min_value=0)
            self.items["coke"] = st.number_input("Coke", min_value=0)
            self.items["fanta"] = st.number_input("Fanta", min_value=0)
            self.items["mountain_duo"] = st.number_input("Mountain Duo", min_value=0)

        if st.button("Total"):
            self.total()
        if st.button("Generate Bill"):
            self.bill_area()
        if st.button("Clear"):
            self.clear_data()
        if st.button("Exit"):
            st.stop()

    def total(self):
        self.total_medical_price = sum(self.items[item] * self.prices[item] for item in ["sanitizer", "mask", "hand_gloves", "dettol", "newsprin", "thermal_gun"])
        self.medical_price = "$ " + str(self.total_medical_price)
        self.c_tax = round((self.total_medical_price * 0.05), 2)
        self.medical_tax = "$ " + str(self.c_tax)

        self.total_grocery_price = sum(self.items[item] * self.prices[item] for item in ["rice", "food_oil", "wheat", "daal", "flour", "maggi"])
        self.grocery_price = "$ " + str(self.total_grocery_price)
        self.g_tax = round((self.total_grocery_price * 0.05), 2)
        self.grocery_tax = "$ " + str(self.g_tax)

        self.total_cold_drinks_price = sum(self.items[item] * self.prices[item] for item in ["sprite", "limka", "mazza", "coke", "fanta", "mountain_duo"])
        self.cold_drinks_price = "$ " + str(self.total_cold_drinks_price)
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax = "$ " + str(self.c_d_tax)

        self.total_bill = float(self.total_medical_price + self.total_grocery_price + self.total_cold_drinks_price + self.c_tax + self.g_tax + self.c_d_tax)

        st.success(f"Total Bill: $ {self.total_bill}")
        st.info(f"Medical Tax: {self.medical_tax}, Grocery Tax: {self.grocery_tax}, Cold Drinks Tax: {self.cold_drinks_tax}")

    def welcome_bill(self):
        self.bill_content = f"""
        \tWelcome Infinite Retail
        \t------------------------
        Bill Number: {self.bill_no}
        Customer Name: {self.c_name}
        Phone Number: {self.c_phone}
        ======================================
        Products\t\tQTY\t\tPrice
        """

    def bill_area(self):
        if not self.c_name or not self.c_phone:
            st.error("Customer Details Are Must")
        elif self.medical_price == "\$ 0.0" and self.grocery_price == "\$ 0.0" and self.cold_drinks_price == "$ 0.0":
            st.error("No Product Purchased")
        else:
            self.welcome_bill()
            for item, qty in self.items.items():
                if qty != 0:
                    self.bill_content += f"\n {"\t" + item.capitalize()}\t\t\t{qty}\t\t{self.prices[item] * qty}"
            self.bill_content += f"\n--------------------------------"
            self.bill_content += f"\n Medical Tax\t\t\t ${self.medical_tax}"
            self.bill_content += f"\n Grocery Tax\t\t\t ${self.grocery_tax}"
            self.bill_content += f"\n Cold Drinks Tax\t\t ${self.cold_drinks_tax}"
            self.bill_content += f"\n Total Bill:\t\t\t\t ${self.total_bill}"
            self.bill_content += f"\n--------------------------------"
            st.text_area("Bill Area", value=self.bill_content, height=400)
            self.save_bill()

    def save_bill(self):
        st.download_button(
            label="Save Bill",
            data=self.bill_content,
            file_name=f"bill_{self.bill_no}.txt",
            mime="text/plain"
        )

    def find_bill(self):
        present = "no"
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill:
                with open(f"bills/{i}", "r") as f1:
                    st.text_area("Bill Area", value=f1.read(), height=400)
                present = "yes"
        if present == "no":
            st.error("Invalid Bill No")

    def clear_data(self):
        self.initialize_variables()
        st.text_area("Bill Area", value="", height=400)

if __name__ == "__main__":
    Bill_App()