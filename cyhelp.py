#variables
birthyear = 1970
breachyear = 2017
repeat = 'y'
threat = ["Data breaches are incidents where information is taken without permission.\n", "Identity theft is when a person uses someone else's personal information without permission.\n", "Phishing emails are emails crafted to look real and convince people to share personal information.\n", "Social engineering is when a person manipulates a victim to give up information.\n", "Ok. :(\n"]
cia = ["Confidentiality makes sure data is private.\n", "Integrity makes sure data has not been tampered with and can be trusted.\n", "Availability makes sure authorized people can access the data.\n", "Ok. :(\n"]
wannacry = ["The breach occurred in 2017 affecting 16 NHS hospitals in the UK due to the computers within not having the most recent updates. The breach was caused by the Wanna Decrypt ransomware, using the EternalBlue exploit that had been leaked by the Shadow Brokers hacker group but had already been patched by Microsoft in a recent update. The ransomware froze systems and encrypted files, requiring a $300 payment to unlock these, however there is no evidence to suggest that patient data was compromised.\n", "The breach complied with the confidentiality pillar of the CIA triad, as the data remained encrypted and confidential, however it was encrypted by the hackers, and so the data was hidden to the victims, not to the hackers, and so the confidentiality pillar was not followed as the hackers had access to data that was meant to be private. This meant that the availability pillar was also not followed as the data was not available for the victim to use. Furthermore, this lead to the services being provided by the NHS no longer being available to the public as many of their devices were no longer functioning. The integrity of the data was also compromised as the victim can not be certain the data was not tampered with as they do not have access to it, and the ransomware scrambled the data, making it impossible to access and leading to a risk of permanent damage being done to the data. This means the data can no longer be trusted.\nI would recommend that a victim do some research online to see if there was a cure to the virus available online, however if it was not available, and if it was the only way for life to continue and less money to be wasted, I would recommend paying for the payload so that life can continue as quickly as possible.", "Ok. :(\n"]

#functions
def choose(topic, list):
  print(list[topic])

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
#interaction
while repeat.lower() == 'y':
  try:
    topic = int(input("Which of the possible threats would you like to learn about?\n[Enter the lowercase letter of the following options: (1) Data breaches, (2) Identity Theft, (3) Phishing emails, (4) Social engineering, or (5) none.]\n")) -1 
    choose(topic, threat)
    repeat = input("Would you like to learn about another threat? [Enter y for yes]\n")
  except:
    print("Sorry, I didn't catch that. Choose one of the options listed.\n")
#more information
print("""The NIST framework is used to identify the areas that need to be covered in order to be prepared for cybersecurity threats.\nThese are:
Identify - identifying the threat
Protect - protecting systems against the threat
Detect - detecting the threat when it occurs
Respond - responding quickly to the threat
Recover - recovering from the threat""")
input("[Press enter to continue.]\n")
print("The CIA Triad is the model used to discuss cybersecurity. CIA stands for: Confidentiality, Integrity and Availabiity. (not the central intelligence agency!)\n")
repeat = 'y'
#revealing information they want to hear
while repeat.lower() == 'y':
  try:
    topic = int(input("What would you like to learn more about?\n[Enter the lowercase letter of the following options: (1) confidentiality, (2) integrity, (3) availability, or (4) none.]\n")) -1 
    choose(topic, cia)
    repeat = input("Would you like to learn about another threat? [Enter y for yes]\n")
  except:
    print("Sorry, I didn't catch that. Choose one of the options listed.\n")
#introducing data breach
print("It has also been " + str(year-breachyear) + " years since the NHS WannaCry data breach happened.\n")
repeat = 'y'

#revealing information on breach that they want to hear
while repeat.lower() == 'y':
  try:
    topic = int(input("What would you like to learn about it?\n[Enter the lowercase letter of the following options: (1) breach details, (2) my reflection, or (3) nothing.]\n")) -1 
    choose(topic, threat)
    repeat = input("Would you like to learn about another threat? [Enter y for yes]\n")
  except:
    print("Sorry, I didn't catch that. Choose one of the options listed.\n")

print("Did you know the average time it takes an unauthorized person 166 days to compromise a system? This is because it is a long process with many steps.")
yn = input("Would you like to learn about the Cyberkill chain, a common set of steps hackers have to follow to compromise a system? [Enter 'y' for yes]\n")
if yn.lower() == "y":
  print("""The Cyberkill chain follows the following set of steps:
  1) Reconnaissance - first the hackers harvest email addresses, conference information, etc.
  2) Weaponization - then they couple exploits with backdoors into deliverable payloads.
  3) Delivery - the weaponized bundle is delivered to the victim via email, web, usb, etc.
  4) Exploitation - the vulnerability in the bundle is then exploited to execute code on the victim's system.
  5) Installation - the malware is then installed onto the asset.
  6) Command and Control - the channel is commanded for remote manipulation of the victim.
  7) Actions on objectives - with 'hands on keyboard' access, the intruders can now accompish their original goals.\n""")
  
yn = input("Would you like to hear about how you can protect yourself online? [Enter 'y' for yes]\n")
if yn.lower() == "y":
  print("""The easiest way to protect yourself is to have secure passwords.
  Secrure passwords contain:
  - Lowercase letters
  - Uppercase letters
  - Numbers
  - Special Characters
  - Are different for each account
  In order to remember them all, it is recommended to store them in password managers.
  Password managers are websites that are made especially to store all your passwords safely and easily, allowing you to store all of your passwords in one place with fewer worries about their security.\n""")

#goodbye
print("Thanks for chatting with me, and I hope you learned something new!")