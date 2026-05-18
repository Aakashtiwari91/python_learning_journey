#password checker
# password length  <6 - week 6 -10 - medium >10 strong

password = "ffkgf848wertyuio2"

if len(password) <6:
    print("week")
elif len(password) <10:
    print("medium")
else:
    print("strong")