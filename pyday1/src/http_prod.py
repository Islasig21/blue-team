ip_string = "192.168.1.1"
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
if failed_attemps:
    alert_level = "HIGH"
    print()