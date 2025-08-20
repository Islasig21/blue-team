"""ip_string = "192.168.1.1"
port = "443"
int_port = int(port)
is_secure = (int_port == 443)
#print(is_secure)  
log_tokens = "Aug 12 10:06:01 sshd[1234]: Failed password for guest from 192.0.2.15 port 22 ssh2".split()
month,day,time,host,*message_ports=log_tokens
print(log_tokens)
ip=log_tokens[9]
print(f"[PARSED]Data: {month} {day} {time},Host:{host}")
print(f"[MESSAGE]: {' '.join(message_ports)}")
print(f"[PARSED]Data: ip:{ip}")
print(f"[MESSAGE]: {' '.join(ip)}")

failed_attemps=[
    "203.0.113.45"
    "198.51.100.23"
    "192.0.2.15"

]

log_lines = [
    "Aug 12 10:02:11 sshd[1234]: Failed password for root from 203.0.113.45 port 22 ssh2",
    "Aug 12 10:05:43 sshd[1234]: Accepted password for admin from 198.51.100.23 port 22 ssh2",
    "Aug 12 10:06:01 sshd[1234]: Failed password for guest from 192.0.2.15 port 22 ssh2"
]


failed_attempts = [line for line in log_lines if "Failed password" in line]


if failed_attempts:
    alert_level = "HIGH"
    print(f"[ALERT] {len(failed_attempts)} failed login attempts detected! Level: {alert_level}")
else:
    print("[OK] No suspicious login attempts found.")


for line_num, line in enumerate(log_lines, 1):
    if "Failed password" in line:
        print(f"[SECURITY] Line {line_num}: Unauthorized login attempt → {line}")

     def analyze_logs(log_file, threshold=2, **options):
    verbose = options.get('verbose', False)
    failed_count = 0

    with open(log_file, "r") as f:
        for line in f:
            if "Failed password" in line:
                failed_count += 1
                if verbose:
                    print(f"[DEBUG] Failed attempt: {line.strip()}")

    if failed_count >= threshold:
        print(f"[ALERT] {failed_count} failed login attempts detected (threshold={threshold})")
        return True
    else:
        print(f"[INFO] {failed_count} failed attempts — below threshold")
        return False


# Example usage:
# result = analyze_logs("auth.log", threshold=3, verbose=True)
# print("Result:", result)
"""
'''
numodd = [num for num in range (0,21)if num%2!=0]
print (numodd)

Path("evidence.log").write_text(

)
def process_evidence_line(line):
    print(F"[EVIDENCE] Processing: (line)")
   ''' '''
class Person:
    def __init__ (self,name,age,country):
        self.name=name
        self.age=age
        self.country=country

    def ShowInfo(self):
            print(f"Hi,I'm{self.name},{self.age}years old from {self.country}.")
        

person1=Person('Islam',21,'Misurata')
        
person1.ShowInfo()
'''
''''
class BankAccount:
    def __init__(self,name,money):
          self.name=name
          self.balance=money

    def deposit(self,amount):
         self.balance+=amount
         print(f"(Deposit Amount is {amount}.Your Balance {self.balance}")


    def withdraw(self,amount):
         if amount<=self.balance:
              self.balance-=amount
              print(f"(Withdraw Amount is {amount}.Your Balance {self.balance}")



    def PrintBankAcoount(self):
          print(f"HELLO BEST COUSTUMER {self.name}.Your Bank Amount is {self.balance}") 

Costumer1=BankAccount("Islam",5000)
Costumer1.PrintBankAcoount() 
Costumer1.deposit(2000)
Costumer1.PrintBankAcoount()                     
Costumer1.withdraw(1000)
Costumer1.PrintBankAcoount() 
'''
import os
import requests

class SolanaCMCRequests:
    BASE_URL = "https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest"

    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("CMC_KEY")
        if not self.api_key:
            raise ValueError("API key is required")
        self.session = requests.Session()
        self.session.headers.update({
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": self.api_key,
        })

    def get_quote(self, symbol="SOL", convert="USD"):
        params = {"symbol": symbol, "convert": convert}
        resp = self.session.get(self.BASE_URL, params=params)
        resp.raise_for_status()
        data = resp.json()
        return data["data"][symbol]["quote"][convert]  


if __name__ == "__main__":
    sol = SolanaCMCRequests(api_key="YOUR_API_KEY")
    print(sol.get_quote())
