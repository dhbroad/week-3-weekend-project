class RentalIncome():
    def __init__(self):
        self.income_dict = {
            "Total Monthly Income": 0,
            "Rent": 0,
            "Laundry": 0,
            "Storage": 0,
            "Misc Items": 0,
        }

        self.expenses_dict = {
            "Total Monthly Expenses": 0,
            "Tax": 0,
            "Insurance": 0,
            "Utilities": {
                "Electric": 0,
                "Water": 0,
                "Sewer": 0,
                "Garbage": 0,
                "Gas": 0
            },
            "HOA": 0,
            "Lawn/Snow": 0,
            "Vacancy": self.income_dict["Total Monthly Income"]*.05,
            "Repairs": 0,
            "CapEx": 0,
            "Property Management": self.income_dict["Total Monthly Income"]*.1,
            "Mortgage": 0,
        }

        self.monthly_cash_flow = (self.income_dict["Total Monthly Income"] - self.expenses_dict["Total Monthly Expenses"])
        self.annual_cash_flow = self.monthly_cash_flow*12

        self.roi_dict = {
            "Total Investment": 0,
            "Down Payment": 0,
            "Closing Costs": 0,
            "Rehab Budget": 0,
            "Misc Other Investments": 0
        }
        self.cocROI = 0

    def income(self):
        for item in self.income_dict:
            if item == "Total Monthly Income":
                continue
            else:
                while True:
                    try:
                        self.income_dict[item] = int(input(f"How much will you be charging for {item} per month? Please enter a positive integer or 0 if there is no charge: "))
                        break
                    except: print("That was not a recognizable integer. Please try again.")
        self.income_dict["Total Monthly Income"] = 0
        for value in self.income_dict:
            if value == "Total Monthly Income":
                continue
            else: self.income_dict["Total Monthly Income"] += value
        print(self.income_dict)
        print(f"Your total expected monthly income is ${self.income_dict['Total Monthly Income']}. You can see a breakdown of each value above.")
        

    def expenses(self):
        for item in self.expenses_dict:
            if item in ["Total Monthly Expenses", "Vacancy"]:
                continue
            elif item == "Utilities":
                while True:
                    utilities_bool = input("Will you be paying for the utilities? yes/no: ")
                    if utilities_bool.lower() == "yes":
                        for utility in self.expenses_dict["Utilities"]:
                            while True:
                                try:
                                    self.expenses_dict["Utilities"][utility] = int(input(f"How much will you be paying for {utility} per month? Please enter a positive integer or 0 if none: "))
                                    self.expenses_dict["Total Monthly Expenses"] += self.expenses_dict["Utilities"][utility]
                                    break
                                except: print("That was not a recognizable integer. Please try again.")
                    elif utilities_bool.lower() =="no":
                        break
                    else: print("Invalid response. Please enter yes or no.")
            elif item == "Property Management":
                while True:
                    management_bool = input("Will you have a property manager? yes/no: ")
                    if management_bool.lower() == "yes":
                        break
                    elif management_bool.lower() == "no":
                        self.expenses_dict["Property Management"] = 0
                        break
                    else: print("Invalid response. Please enter yes or no.")
            else:
                while True:
                    try:
                        self.expenses_dict[item] = int(input(f"How much will you be paying for {item} per month? Please enter a positive integer or 0 if none: "))
                        break
                    except: print("That was not a recognizable integer. Please try again.")
        self.expenses_dict["Total Monthly Expenses"] = 0
        for value in self.expenses_dict:
            if value == "Total Monthly Expenses":
                continue
            else: self.expenses_dict["Total Monthly Expenses"] += value            
        print(self.expenses_dict)
        print(f"Your total expected monthly expense cost is ${self.income_dict['Total Monthly Income']}. You can see a breakdown of each value above.")
        if self.income_dict["Total Monthly Income"] > 0:
            print(f"Based off of the expected Income and Expenses you entered, your total monthly cashflow would be ${self.monthly_cash_flow}.")
            print("You can now calculate your Cash on Cash Return on Investment from entering calculate and then ROI from the main menu.")
        else: print(f"Great job calculating your expenses! Now go calculate your expected income to see your Cash Flow and calculate your ROI.")
        print("Please note; the Vacancy and Property Management values wer calculated automatically, as they should equate to 5% and 10% of your total rental income, respectively.")
        print("If you would like to update the values manually, you can do so by entering update from the main menu and then the item you would like to change.")

    def roi(self):
        while True:
            if self.income_dict == 0:
                print("You have not calculated your income yet. Please select calculate and then income from the main menu and then come back and try again.")
                break
            elif self.expenses_dict == 0:
                print("You have not calculated your expenses yet. Please select calculate and then expenses from the main menu and then come back and try again.")
                break
            for item in self.roi_dict:
                if item == "Total Investment":
                    continue
                else:
                    while True:
                        try:
                            self.roi_dict[item] = int(input(f"How much will your {item} be? Please enter a positive integer or 0 if there is no charge: "))
                            self.roi_dict["Total Investment"] += self.roi_dict[item]
                            break
                        except: print("That was not a recognizable integer. Please try again.")
            print(f"Your total investment amount would be ${self.roi_dict['Total Investment']}. You can see a breakdown of each value below.")
            print(self.roi_dict)
            if self.roi["Total Investment"] > 0:
                self.cocROI = self.annual_cash_flow/self.roi["Total Investment"]
                print(f"Based on the information provided, your Cash on Cash ROI is {self.cocROI} or %{self.cocROI*100}.")
            break

    def update(self):
        while True:
            category = input("Which category would you like to make changes to? Income, expenses or ROI? You can also type home to return to the main menu. ")
            if category.lower() == "home":
                break
            elif category.lower() == "income":
                to_change_dict = self.income_dict
            elif category.lower() == "expenses":
                to_change_dict = self.expenses_dict
            elif category.lower() == "roi":
                to_change_dict = self.roi_dict
            else: print("I'm sorry. I didn't recognize your response. Please try again.")
            if category.lower() in ["income", "expenses", "roi"]:
                while True:
                    print(to_change_dict)
                    item = input("Please see the list of items in the line above. Which item would you like to manually change the value for? You can also type home to return to the main menu. ")
                    if item.lower() == "home":
                        return self.run()
                        break
                    elif item.lower().capitalize() in to_change_dict or item.lower().capitalize() in self.expenses_dict["Utilities"]:
                        if item.lower() == "utilities":
                            print("To change utilities, please type the specific utility you would like to change.")
                            continue
                        while True:
                            try:
                                value = int(input(f"What would you like to change the value to for {item}? Please enter a positive integer or 0. "))
                                if item.lower().capitalize() in ["Electric", "Water", "Sewer", "Garbage", "Gas"] and category.lower() =="expenses":
                                    to_change_dict["Utilities"][item.lower().capitalize()] = value
                                else:
                                    to_change_dict[item] = value
                            except: print("That was not a recognizable integer. Please try again."); continue
                            print(to_change_dict)
                            print(f"{item} has been updated to {value}. Please see the full list above.")
                            
                            break
                        break
                    else: print(f"{item.capitalize()} is not in the {category} list. Please try again. Note; the word you enter does NOT need apostrophes around it.")
                    
    def run(self):
        while True:
            user_input = input("Welcome to the the Rental Income Calculator. What would you like to do? Calculate, view, update, or quit? ")
            if user_input.lower() == "calculate":
                while True: 
                    calc_input = input("What would you like to calculate? Enter income, expenses, ROI, or type home to return to the main menu. ")
                    if calc_input.lower() == "income":
                        self.income()
                        break
                    elif calc_input.lower() == "expenses":
                        self.expenses()
                        break
                    elif calc_input.lower() == "roi":
                        if self.income_dict["Total Monthly Income"] == 0:
                            print("You have not calculated your income yet. Please return to the home screen to calculate and then come back.")
                            continue
                        self.roi()
                        break
                    elif calc_input.lower() == "home":
                        self.run()
                    else:
                        print("Invalid Response. Please type one of the following options. (income/expenses/ROI/all/home): ")
            elif user_input.lower() == "view":
                while True: 
                    view_input = input("What would you like to view? Enter income, expenses, ROI, all, or type home to return to the main menu. ")
                    if view_input.lower() == "income":
                        print(self.income_dict)
                        break
                    elif view_input.lower() == "expenses":
                        print(self.expenses_dict)
                        break
                    elif view_input.lower() == "roi":
                        print(self.roi_dict)
                        break
                    elif view_input.lower() == "all":
                        print(self.income_dict)
                        print(self.expenses_dict)
                        print(self.roi_dict)
                    elif view_input.lower() == "home":
                        break
                    else:
                        print("Invalid Response. Please type one of the following options. (income/expenses/ROI/home): ")
            elif user_input.lower() == "update":
                self.update()
            elif user_input.lower() == "quit":
                print("Thank you for using the Rental Income Calculator. Have a nice day!")
                break
            else: print("I'm sorry. I didn't recognize that response.")
            
ri = RentalIncome()
ri.run()