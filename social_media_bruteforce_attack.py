from utils import *
from rich.console import Console
import platform
console = Console()


start()
# select social media
choice = c1()






if choice == 1:
	choice = start_instagram()
	if choice == 1:
		username = get_username()
		wordlist = get_wordlist()
		insta_bruteforce(username, wordlist )
	if choice == 2:
		username = get_username()
		amount = get_amount()
		insta_massreport(username, amount, 1)
	if choice == 3:
		insta_phishing()
elif choice == 2:
	choice = start_instagram()
	if choice == 1:
		username = get_facebook()
		wordlist = get_wordlist()
		facebook_bruteforce(username, wordlist)
	if choice == 2:
		facebook_massreport()
	if choice == 3:
		facebook_phishing()
elif choice == 3:
	choice = start_instagram()
	if choice == 1:	
		username = get_email()
		wordlist = get_wordlist()
		gmail_bruteforce(username, wordlist)
	if choice == 2:
		gmail_massreport()
	if choice == 3:
		gmail_phishing()


elif choice == 4:
	choice = start_instagram()
	if choice == 1:	
		from utils import *
from rich.console import Console
import platform
console = Console()


start()
# select social media
choice = c1()







if choice == 1:
	choice = start_instagram()
	if choice == 1:
		username = get_username()
		wordlist = get_wordlist()
		insta_bruteforce(username, wordlist)
	if choice == 2:
		username = get_username()
		amount = get_amount()
		insta_massreport(username, amount, 1)
	if choice == 3:
		insta_phishing()
elif choice == 2:
	choice = start_instagram()
	if choice == 1:
		username = get_facebook()
		wordlist = get_wordlist()
		facebook_bruteforce(username, wordlist)
	if choice == 2:
		facebook_massreport()
	if choice == 3:
		facebook_phishing()
elif choice == 3:
	choice = start_instagram()
	if choice == 1:	
		username = get_email()
		wordlist = get_wordlist()
		gmail_bruteforce(username, wordlist)
	if choice == 2:
		gmail_massreport()
	if choice == 3:
		gmail_phishing()


elif choice == 4:
	choice = start_instagram()
	if choice == 1:	
		username = get_username()
		wordlist = get_wordlist()
		twitter_bruteforce(username, wordlist)
	if choice == 2:
		twitter_massreport()
	if choice == 3:
		twitter_phishing()

