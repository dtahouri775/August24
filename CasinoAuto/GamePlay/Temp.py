import sys


def main():
    try:
        print(sys.version)
        import pyautogui
        #import gw_utility.Book
    except:
        import pyautogui
        print("Second time is exported")
    '''    
    except ImportError as error:
        # Output expected ImportErrors.
        print(error.__class__.__name__ + ": " + error.message)
    except Exception as exception:
        # Output unexpected Exceptions.
        print(exception, False)
        print(exception.__class__.__name__ + ": " + exception.message)
    '''

if __name__ == "__main__":
    main()