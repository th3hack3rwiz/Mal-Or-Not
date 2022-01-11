<p align="center">
  <img src="https://th3hack3rwiz.github.io/images/Mal-OR-Not/title.png">
</p>

# Mal-OR-Not
Mal-OR-Not: (Malicious Entity Detector)

Nowadays, cyber crimes are at an all-time high, especially after the recent global pandemic situation that's going on, due to which everything had to be shifted to online mode. Cybercriminals have made a fortune in cyberspace. 

These cyber crimes may be of countless types and forms but the way they originate will remain constant. Phishing attacks (that is to trick the user into performing malicious actions) are one of the biggest gateways to the occurrence of a cybercrime. 

These actions could be - **clicking on a malicious URL, opening an infected file, visiting a malicious domain, reacting to spam emails and SMS's, etc.** 

What I'm trying to highlight here is that the origin of these cyber crimes is generally - *an IP address, a URL, a domain, a mobile number, or a malicious file.*

We as cybersecurity students who're about to break into the industry decided to take upon this challenge of developing an all-in-one solution to this problem. After a lot of brainstorming and accumulation of thoughts and ideas, we have come up with 'Mal-OR-Not'. We have developed it in a way that any normal user can use it to safeguard himself from cybercrimes and catch any malicious intent in its early phases. 

## Installation Instructions

### Get the required API keys:

- #### Steps to get API key for ip2location

  1) Make an account on : https://www.ip2location.com/register
  2) Activate your account.
  3) Go to: https://www.ip2location.com/web-service/ip2location
  4) Click on "SIGN UP FOR A TRIAL KEY"
  5) Check your inbox for API key.


- #### Steps to get API key for ipqualityscore

  1) Make an account on - https://www.ipqualityscore.com/create-account
  1) Activate your account.
  1) Go to - https://www.ipqualityscore.com/user/settings
  1) Scroll down to get your API key


- #### Steps to get API key for virustotal

  1) Create an account on Virus Total - https://www.virustotal.com/gui/join-us
  1) Activate your account
  1) Go to: https://www.virustotal.com/gui/user/<your username>/apikey
  1) Get your virustotal API key.


- #### Steps to get API key for numverify

  1) Make an account on - https://numverify.com/signup
  1) Activate your account.
  1) Go to https://numverify.com/dashboard to get API key.


### Clone this repository and install all requirements:

```bash
git clone https://github.com/th3hack3rwiz/Mal-Or-Not.git
cd Mal-Or-Not
chmod +x setup.sh
./setup.sh
```
  
### Usage

python3 Mal-Or-Not.py
  
<p align="left">
  <img src="https://th3hack3rwiz.github.io/images/Mal-OR-Not/intro%20screen.png">
</p>
  
### Implementation
  
User is prompted to enter his name and location for report generation purposes.
 
  <p align="left">
  <img src="https://th3hack3rwiz.github.io/images/Mal-OR-Not/Enter%20Username%20and%20City.png">
</p>
  
Main user interface is displayed to the user, from which he can select what kind of entity he wants to test. 
  
  <p align="left">
  <img src="https://th3hack3rwiz.github.io/images/Mal-OR-Not/intro%20screen2.png">
</p>
  
For eg: If a user wants to find out if a certain file is malicious or not. He will do the following: 
(To test the authenticity of the tool, let's create a real malware using msfvenom)

<p align="left">
  <img src="https://th3hack3rwiz.github.io/images/Mal-OR-Not/creating%20a%20malware.png">
</p>
  
Now, let's test the malware against Mal-OR-Not
  
  <p align="left">
  <img src="https://th3hack3rwiz.github.io/images/Mal-OR-Not/File-take%20input1.png">
</p>
 
  <p align="left">
  <img src="https://th3hack3rwiz.github.io/images/Mal-OR-Not/File%20take%20input2.png">
</p>
  
We obtain the following result:
  
  <p align="left">
  <img src="https://th3hack3rwiz.github.io/images/Mal-OR-Not/File%20Result%20-%20malicious.png">
</p>
  
The following report is generated in the 'report/file' directory:
  
  <p align="left">
  <img src="https://th3hack3rwiz.github.io/images/Mal-OR-Not/file-report.png">
</p>
