birthyear = 1970
repeat = 'y'
print("Hello! I'm CyHelp.")
name = input("What's your name?\n")
year = int(input("Nice to meet you " + name + "! What year is it?\n"))
print("Wow! Cybersecurity started " + str(year-birthyear) + " years ago!")
print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!")
input("[Press enter to continue.]\n")
print("Cybersecurity refers to the practices that people use to protect computer systems and networks from digital threats.")
input("[Press enter to continue.]\n")
print("These people can be governments, nations, companies, communities, organizations and individuals.")
input("[Press enter to continue.]\n")
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for: Confidentiality, Integrity and Availabiity. (not the central intelligence agency!)")

while repeat.lower() == 'y':
  topic = input("What would you like to learn more about? [Enter the lowercase letter of the following options: (a) confidentiality, (b) integrity, (c) availability, or (d) none.]\n")
  if topic.lower() == "a":
    print("Confidentiality makes sure data is private.")
  elif topic.lower() == "b":
    print("Integrity makes sure data has not been tampered with and can be trusted.")
  elif topic.lower() == "c":
    print("Availability makes sure authorized people can access the data.")
  elif topic.lower() == "d":
    print("Ok. :(")
    repeat = 'n'
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  repeat = input("Would you like to learn about another pillar? [Enter y for yes]\n")

print("Thanks for chatting with me, and I hope you learned something new!")