import webbrowser,pyperclip,sys
print('sys.argv')
print(sys.argv[0])
try:
    word = sys.argv[1]
except IndexError:
    word = pyperclip.paste()

#print(sys.argv[1:])
webbrowser.open('https://www.google.com/search?sxsrf=ALeKk02DtAgeJjC1ifMIYwz8EzoiJflwZQ%3A1600609497456&ei=2VxnX6e9G8mymAXD3LjADQ&q='+word+' meaning')