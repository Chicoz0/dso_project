class ConnectionView:
    def show_connection_details(self, connection_data: dict):
        print("\n----- Connection Details -----")
        print(f"Connection ID: {connection_data['id']}")
        print(f"Status: {connection_data['status']}")
        print(f"Users involved: {connection_data['user1_name']} and {connection_data['user2_name']}")
        
        print("\nWhat do you want to do?")
        print("1 - Dismiss Connection")
        print("0 - Return to the Connections Menu")
        
        return input("Your choice: ")