#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# JingyinChen, 2021-Aug-28, added class CD, added import pickle
# JingyinChen, 2021-Aug-29, added class FileIO, class IO and the script main body
#------------------------------------------#

# -- DATA -- #
import pickle # added to handle binary data

strFileName = 'CDInventory.txt' # changed the file name from 'cd' to 'CD'
lstOfCDObjects = []
strChoice = '' # user input
dicRow = {}  # list of data row
objFile = None  # file object

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TODone Add Code to the CD class
    # -- Fields -- #
    # --Constuctor --#
    def __init__(self, cd_id, cd_title, cd_artist):
        # --Attributes --#
        self.__cd_id = cd_id
        self.__cd_title = cd_title
        self.__cd_artist = cd_artist
    
    # --Properties --#
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, value):
        if type(value) == int:
            self.__cd_id = value
        else:
            raise Exception('ID must be an integer')
        
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, value):
        if type(value) == str:
            self.__cd_title = value
        else:
            raise Exception('Title must be a string')
            
    @property
    def cd_artist(self):
        return self.__cd_artist
    
    @cd_artist.setter
    def cd_artist(self, value):
        if type(value) == str:
            self.__cd_artist = value
        else:
            raise Exception('Artist must be a string')
    
    # --Methods --#
    def __str__(self):
        return str(self.__cd_id) + ',' + self.__cd_title + ',' + self.__cd_artist

# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties: None

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)
        add_lst_Inventory(lstInput, lst_Inventory): -> (a list of CD objects to put in the inventory)

    """
    # TODone Add code to process data from a file
    # -- Fields -- #
    # --Constuctor --#
        # --Attributes --#
    # --Properties --#
    # --Methods --#
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of dictionaries

        Read the data from file identified by file_name into a 2D table

        Args:
            file_name (string): name of file used to read the data form
        
        Returns:
            None.
        """
        try:
            with open(file_name, 'rb') as fileObj:
                data = pickle.load(fileObj)
            return data
        except FileNotFoundError as e:
            print('\nText file does not exist! Please check the folder.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except ValueError as e:
            print('\nLooks like the file is a plain text file.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except Exception as e:
            print('\nGeneral error.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
            
    # TODone Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        """Save the user input data to the file with binary data

        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory (list of dict): 2D data structure (list of dicts) that holds 
        the data during runtime

        Returns: None

        """
        try:
            with open(file_name, 'wb') as objFile:
                pickle.dump(lst_Inventory, objFile)
        except FileNotFoundError as e:
            print('\nText file does not exist! Please check the folder.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except FileExistsError as e:
            print('\nText file with the same name exists! Please check the folder.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except Exception as e:
            print('\nGeneral error.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
            
    @staticmethod
    def add_lst_Inventory(lstInput, lst_Inventory):
        """Firstly store the new user inputs of ID, CD Title and Artist Name as 
        a tuple of threes string, to a dictionary in the memory. 
           Then add the dictionary to the table, which is a 2D data structure 
        as list of dicts

        Args:
            lstInput (new list from userinput): the list that holds the data from 
        userinput
            lst_Inventory (list of dict): 2D data structure (list of dicts) that holds the 
        dicts of data during runtime.

        Returns:
            None.
        """
        try:
            dicRow = {'ID': int(lstInput[0]), 'Title': lstInput[1], 'Artist': lstInput[2]}
            lst_Inventory.append(dicRow)
        except ValueError as e:
            print('\nMust enter an integer for ID')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except Exception as e:
            print('\nGeneral error.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODone add docstring
    """Stores data about a CD:

    properties: None
    
    methods: 
        print_menu(): -> None
        menu_choice(): -> user's choice from user input
        show_inventory(lst_Inventory): -> None
        input_data(): -> a list of three strings: new id, cd title and artist 

    """
    # -- Fields -- #
    # --Constuctor --#
        # --Attributes --#
    # --Properties --#
    # --Methods --#
    # TODone add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args: None.

        Returns: None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
    # TODone add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args: None.

        Returns:
            choice (string): a lower case string of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice
    # TODone add code to display the current data on screen
    @staticmethod
    def show_inventory(lst_Inventory):
        """Displays current inventory 

        Args:
            lst_Inventory (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns: None.

        """
        try:
            print('======= The Current Inventory: =======')
            print('ID\tCD Title (by: Artist)\n')
            for row in lst_Inventory:
                print('{}\t{} (by:{})'.format(*row.values()))
            print('======================================')
            print()
        except AttributeError as e:
            print('\nInventory list has datatype error. Try exit and reload.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')
        except Exception as e:
            print('\nGeneral error.')
            print('\nBuild in error info:')
            print(type(e), e, e.__doc__, sep='\n')

    # TODone add code to get CD data from user
    @staticmethod
    def input_data():
        """Ask user to enter new ID, CD Title and Artist Name
        
        Args: None

        Returns:
            A list of three strings: ID, CD Title, and Artist Name 
            
        """
        cd_id = input('Enter ID: ').strip()
        cd_title = input('What is the CD\'s title? ').strip()
        cd_artist = input('What is the Artist\'s name? ').strip()
        return [cd_id, cd_title, cd_artist]

# -- Main Body of Script -- #
# TODone Add Code to the main body
# Load data from file into a list of CD objects on script start
FileIO.load_inventory(strFileName)
# Display menu to user
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()
    # show user current inventory
    if strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue
    # let user add data to the inventory
    elif strChoice == 'a':
        lstInput = IO.input_data()
        FileIO.add_lst_Inventory(lstInput, lstOfCDObjects)
        print('Current inventory:')
        IO.show_inventory(lstOfCDObjects)
        continue
    # let user save inventory to file
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        print()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue
    # let user load inventory from file
    elif strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        print('reloading...')
        lstOfCDObjects = FileIO.load_inventory(strFileName)
        IO.show_inventory(lstOfCDObjects)
        continue
    # let user exit program
    if strChoice == 'x':
        break
    else:
        print('General Error')
