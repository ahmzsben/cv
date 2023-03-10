#!/usr/bin/python
# Author : RA YAN
# @RAYANDIAG
#Account link https://t.me/RAYANDIAG
# version : 1.0



import subprocess
import sys
import os


class SuperScanner:

    def __init__(self):
        self.lines = []
        self.filename = ""

    def printCredits(self):
        print("""
    _____             __     __      _   _ 
   |  __ \     /\     \ \   / //\   | \ | |
   | |__) |   /  \     \ \_/ //  \  |  \| |
   |  _  /   / /\ \     \   // /\ \ | . ` |
   | | \ \  / ____ \     | |/ ____ \| |\  |
   |_|  \_\/_/    \_\    |_/_/    \_\_| \_|
	                                                                              
		""")

        print("   Happy Scanning Script by: RA YAN ")
        print("            @RAYANDIAG              	")   
        print("      https://t.me/RAYANDIAG   	")  

    def getFilename(self):
        self.filename = sys.argv[1]

    def loadIP(self):
        with open(self.filename) as f:
            self.lines = [line.rstrip('\n') for line in f]
        print(f"\n\nThere are {len(self.lines)} in {self.filename} \n\n")

    def executeCommands(self):
        target = ""
        targeted = ""
        if len(sys.argv) >= 4: 
            if sys.argv[3] == "target":
                target = "--target amir5.tk"
                targeted = "target"
            elif sys.argv[3] == "target2":
                target = "--target azure.kenyainnews.com"
                targeted = "target2"
            else:
                pass
        for ip in self.lines:
            print(f"cdn-ssl {ip} {targeted}")
            os.system(f"bugscanner-go scan cdn-ssl -c {ip} {target} -o Rayan_files/scanned_{sys.argv[1]}")
	
    def executeCommands2(self):
        os.system(f"bugscanner-go scan direct -f {sys.argv[1]} -o Rayan_files/scanned_{sys.argv[1]}")

    def executeCommands3(self):
        os.system(f"subfinder -d {sys.argv[2]} -o rayansubdomainlist")
		
    def run(self):
        self.printCredits()
        if sys.argv[2] == "cdn":
            self.getFilename()
            self.loadIP()
            self.executeCommands()
        elif sys.argv[2] == "direct":
            self.getFilename()
            self.loadIP()
            self.executeCommands2()
        elif sys.argv[1] == "subdomain":
            self.executeCommands3()
			
        print("All Commands has been run successfully!")


if __name__ == "__main__":
    scan = SuperScanner()
    scan.run()


    

