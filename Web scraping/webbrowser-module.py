#this program will create a web scraper that will open up a map on the web
#wo basically this program will copy anything from the clip board and then will add it to the "address" variable
#and with using the url it will add it on the url and then lunch it to google, so if anything other then an address is copied it will copy that
#basically you have to copy an address, and if your clip board doesn't have any address it will paste whatever is first on it
import webbrowser, sys, pyperclip
sys.argv #['webbrowser-module.py'+ '400'+ 'W Main'+ 'St.']

#check if commands line arguements were passed

if len(sys.argv) > 1:
    #['webbrowser-module.py, '400', 'W Main', 'St.'] -> '400 W Main St.'
    address = ''.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


