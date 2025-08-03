import time
import random
def intro():
    print("🕵️ Welcome Agent. Your mission awaits...")
    time.sleep(1.5)
    print("Choose your mission:\n")
    print("1. Scan Target")
    print("2. Crack Password")
    print("3. Trace Signal")
    print("4. Exit")
def scan_target():
    L1=["✅Target found!","❌Scan failed. Try again."]
    print("🔍Scanning...")
    time.sleep(2)
    result=random.choice(L1)
    print(result)
def crack_pw():
    print("🔐 Initiating password crack...")
    time.sleep(2)
    pw=random.int(100,999)
    guess=int(input("Enter your guess(3-digit code):"))
    if guess==pw:
        print("🔐 Cracking password...")
        time.sleep(1.5)
        print("💥 Boom! Access granted.")
    else:
        print("🚫Access denied! The code was",pw,".")
def trace_signal():
    L2=["✅Scanned to location.","❌Tracing failed!"]
    print("📡Tracing signal...")
    op=random.choice(L2)
    print(op)

while True:
       intro()
       ch=int(input("Enter your choice:"))
       if ch==1:
           scan_target()
           break
       elif ch==2:
           crack_pw()
           break
       elif ch==3:
           trace_signal()
           break
       else:
           break