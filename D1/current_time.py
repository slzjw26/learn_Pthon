from datetime import datetime
now = datetime.now()
text = now.strftime('%a, %Y-%m-%d %H:%M:%S')
print(text)
