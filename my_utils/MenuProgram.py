class MenuProgram:
    
    exit_message = "Exiting program. Goodbye!"
    
    def __init__(self):
        """
        menu program class for terminal menu user interface
        """
        self.menu_options = {}
        self.exit_option = "0"  # Default exit option key

    def add_option(self, description, target_function):
        """
        Add a menu option for a target function
        """
        option_number = str(len(self.menu_options) + 1)
        self.menu_options[option_number] = {"key": option_number, "description": description, "function": target_function}
        
    def run(self):
        """
        Run the menu program in a loop until the exit option is provided
        """
        while True:
            # print menu
            for key, option in self.menu_options.items():
                print(f"{key}: {option['description']}")
            print(f"{self.exit_option}: Exit")
            
            # user input
            choice = input("\nSelect an option: ").strip()

            if choice == self.exit_option:
                print(MenuProgram.exit_message)
                break

            # error handling for choosing an option
            if choice in self.menu_options:
                try:
                    self.menu_options[choice]["function"]()
                except Exception as e:
                    print(f"An error occurred: {e}")
            else:
                print("Invalid option. Please try again.")