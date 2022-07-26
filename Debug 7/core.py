"""
Function that converts a decimal IP address to a binary IP address
"""
def Decimal_to_Binary_IP(number:str):
    IP_Addr = number.split('.')
    Binary_IP = []
    for ip in IP_Addr:
        Binary_Octet = bin(int(ip))[2:]
        Binary_Octet = format(int(Binary_Octet), "08b")
        Binary_IP.append(Binary_Octet)
    return ".".join(Binary_IP)
    
if __name__ == '__main__':
    print(Decimal_to_Binary_IP("172.16.1.200"))