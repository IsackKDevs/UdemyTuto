#this program will use the requests module to download something from the web
import requests
#below you use requests.get('') and put in the url in the .get from the web you want
res = requests.get('http://www.southchurchschool.com/wp-content/uploads/2017/09/Romeo-Juliet.pdf')
res.status_code

print(len(res.text))