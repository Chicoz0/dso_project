class LoggedAdminView:
    def show_logged_admin_menu(self):
        print("\n----- Admin Dashboard -----")
        print("1 - Manage Users")
        print("2 - Manage Events")
        print("3 - View System Reports")
        print("0 - Logout")
        choice = input("Choose an option: ")
        return choice
    
    def show_manage_users_menu(self):
        print("\n----- Manage Users -----")
        print("1 - Check User Details")
        print("2 - (Un)Suspend a User")
        print("0 - Return to Admin Dashboard")
        return input("Choose an option: ")
    
    def show_user_details(self, user_data: dict):
        print("\n----- User Details -----")
        if not user_data:
            print("User not found.")
            print("Press any key to return...")
            return None

        print(f"ID: {user_data['id']}")
        print(f"Username: {user_data['username']}")
        print(f"Email: {user_data['email']}")
        print(f"Status: {user_data['status']}")
        print("Press any key to return...")
        input()
        return None
    
    def show_suspension_menu(self):
        print("\n----- (Un)Suspend User -----")
        user_id = input("Enter the ID of the user to suspend or unsuspend: ")
        return user_id

    # Manage Events - a ser construído...

    def show_system_reports_menu(self):
        print("\n----- System Reports -----")
        print("1 - Total Users")
        print("2 - Total Events") #ainda n construído
        print("3 - Top 10 Most Popular Events") #ainda n construído
        print("4 - Top 10 Most Popular Attractions") #ainda n construído
        print("5 - Top 10 Most Used Tags") #ainda n construído
        print("0 - Return to Admin Dashboard")
        return input("Choose an option: ")