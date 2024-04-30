# Script to automatically send a target boxes from USPS

# Description
This script is to show that even decades later, boxes can be spammed to a target address
for the sake of irritation. A max of 500 boxes can be sent, but that is for only ONE order or ONE account.
This can leads to an attacker sending thousands of boxes throughout the day, week, etc. to a given target.

* Key Note
    - This no longer is working since yesterday due to them taking the option to deliver boxes for free down..
    - We will see how they go about mitigating such and go from there in a later time.
    - For now I'm going to leave this code here as a base. (Never tried it with premade accounts 👀)


# Disclaimer
This script is for educational purposes only or if YOU truly need boxes to be sent to your place of stay.
I am not responsible for the usage of this utility, nor do I claim any responsibility for any actions by
others from the use of this utility.

```
       +--------------+
      /|             /| 
     / |            / |
    *--+-----------*  |
    | USPS Shipping|  |
    |  |           |  |
    |  |           |  |
    |  +-----------+--+
    | /            | /
    |/             |/
    *--------------*     [Boxxer]
```

# Prerequisites
```
python3
```

# Install
```
git clone https://github.com/CharlesTheGreat/Boxxer
cd Boxxer
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
playwright install
```

# Usage
```
usage: python3 boxxer.py --help

ship a target a bunch of boxes

options:
  -h, --help            show this help message and exit
  -s STREET, --street STREET
                        specify the street address [1600 Gabaldon Rd]
  -st STATE, --state STATE
                        specify the street address [Nevada]
  -c CITY, --city CITY  specify the city the address resides in [Las Vegas]
  -z ZIP, --zip ZIP     specify the zip code of the address [87112]
```

# 💬 Contact Me 

![Gmail Badge](https://img.shields.io/badge/-doobthegoober@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white)

# 🚦 Stats

<a href="https://github.com/CharlesTheGreat77">
  <img src="https://github-readme-stats.vercel.app/api?username=CharlesTheGreat77&show_icons=true&hide=commits" />
</a>
<a href="https://github.com/CharlesTheGreat77">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=CharlesTheGreat77&layout=compact" />
</a>

<p align="center"> 
  <img src="https://profile-counter.glitch.me/CharlesTheGreat77/count.svg" />
</p>