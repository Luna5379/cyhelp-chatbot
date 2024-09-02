#variables
birthyear = 1970
breachyear = 2017
repeat = 'y'

#introduction
print("Hello! I'm CyHelp.")
name = input("What's your name?\n")
year = int(input("Nice to meet you " + name + "! What year is it?\n"))
print("Wow! Cybersecurity started " + str(year-birthyear) + " years ago!")

#information
print("The field of Cybersecurity started in the 1970s when more and more information started being stored on computer systems and networks!")
input("[Press enter to continue.]\n")
print("Cybersecurity refers to the practices that people use to protect computer systems and networks from digital threats.")
input("[Press enter to continue.]\n")
print("These people can be governments, nations, companies, communities, organizations and individuals.")
input("[Press enter to continue.]\n")
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for: Confidentiality, Integrity and Availabiity. (not the central intelligence agency!)\n")

#revealing information they want to hear
while repeat.lower() == 'y':
  topic = input("What would you like to learn more about?\n[Enter the lowercase letter of the following options: (a) confidentiality, (b) integrity, (c) availability, or (d) none.]\n")
  if topic.lower() == "a":
    print("Confidentiality makes sure data is private.\n")
  elif topic.lower() == "b":
    print("Integrity makes sure data has not been tampered with and can be trusted.\n")
  elif topic.lower() == "c":
    print("Availability makes sure authorized people can access the data.\n")
  elif topic.lower() == "d":
    print("Ok. :(\n")
    repeat = 'n'
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  repeat = input("Would you like to learn about another pillar? [Enter y for yes]\n")

#introducing data breach
print("It has also been " + str(year-breachyear) + " years since the NHS WannaCry breach happened.\n")
repeat = 'y'

#revealing information on breach that they want to hear
while repeat.lower() == 'y':
  topic = input("What would you like to learn about it?\n[Enter the lowercase letter of the following options: (a) breach details, (b) my reflection, or (c) nothing.]\n")
  if topic.lower() == "a":
    print("The breach occurred in 2017 affecting 16 NHS hospitals in the UK due to the computers within not having the most recent updates. The breach was caused by the Wanna Decrypt ransomware, using the EternalBlue exploit that had been leaked by the Shadow Brokers hacker group but had already been patched by Microsoft in a recent update. The ransomware froze systems and encrypted files, requiring a $300 payment to unlock these, however there is no evidence to suggest that patient data was compromised.\n")
  elif topic.lower() == "b":
    print("The breach complied with the confidentiality pillar of the CIA triad, as the data remained encrypted and confidential, however it was encrypted by the hackers, and so the data was hidden to the victims, not to the hackers, and so the confidentiality pillar was not followed as the hackers had access to data that was meant to be private. This meant that the availability pillar was also not followed as the data was not available for the victim to use. Furthermore, this lead to the services being provided by the NHS no longer being available to the public as many of their devices were no longer functioning. The integrity of the data was also compromised as the victim can not be certain the data was not tampered with as they do not have access to it, and the ransomware scrambled the data, making it impossible to access and leading to a risk of permanent damage being done to the data. This means the data can no longer be trusted.\nI would recommend that a victim do some research online to see if there was a cure to the virus available online, however if it was not available, and if it was the only way for life to continue and less money to be wasted, I would recommend paying for the payload so that life can continue as quickly as possible.")
  elif topic.lower() == "c":
    print("Ok. :(\n")
    repeat = 'n'
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")

  repeat = input("Would you like to learn somethine else? [Enter y for yes]\n")

#goodbye
print("Thanks for chatting with me, and I hope you learned something new!")