birthyear = 1970
print("Hello! I'm CyHelp.")
name = input("What's your name?\n")
year = int(input("Nice to meet you " + name + "! What year is it?\n"))
print("Wow! Cybersecurity started " + (year-birthyear) + " years ago!")
print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!")
input("[Press enter to continue.]\n")
print("Cybersecurity refers to the practices that people use to protect computer systems and networks from digital threats.")
input("[Press enter to continue.]\n")
print("These people can be governments, nations, companies, communities, organizations and individuals.")
input("[Press enter to continue.]\n")
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for: Confidentiality, Integrity and Availabiity. (not the central intelligence agency!)")
topic = input("What would you like to learn more about? [Enter the lowercase letter of the following options: (a) confidentiality, (b) integrity, (c) availability, or (d) none.]\n")

if topic == "a":
  print("Confidentiality makes sure data is private.")
  elif topic == "b":
  print("Integrity ensures data can be trusted and has not been tampered with.")
  elif topic == "c":
  print("Availability ensures networks, systems, and applications are up and running to authorized users whenever they hope to use them.")
  elif topic == "d":
  print("Ok. :(")
print("Thanks for chatting with me, and I hope you learned something new!")