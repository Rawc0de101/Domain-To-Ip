# -*- coding: utf-8 -*-
import socket 
import os
import time

def restart():
    domain()

#colors 
purp = '\033[35m'
whit = '\033[97m'
gree = '\033[92m'
yell = '\033[93m'
red  = '\033[31m'
cyan = '\033[96m'

def domain():
    os.system('clear')
    print(yell+"      𝓓𝓸𝓶𝓪𝓲𝓷   𝓽𝓸   𝓘𝓟   𝓥2")
    print("")
    print(yell+"    Enter Number of domains")
    print(purp+"            1 - 10")
    print("")
    numdom = int(raw_input(purp+"╔─────>"+yell+" "))

    if numdom == 1:      #Domain   1
       os.system('clear')
       print(yell+"                    ┌──────────────────────────────────┐")
       print("                    │    𝓦𝓮𝓵𝓬𝓸𝓶𝓮    𝓣𝓸    𝓓𝓸𝓶𝓪𝓲𝓷 "+yell+"Ꮙ 2   │")
       print("                    └────────┬────────────────┬────────┘")
       print("                             │"  +red+"  Enter Domain" +yell+"  │"        )
       print("                             └───┬───────┬────┘")
       print("                                 │"   +red+"   1" +yell+"   │")
       print("                                 └───────┘")
       print("")
       domain = raw_input(purp+"╔─────>"+yell+" ") 
       resolve = socket.gethostbyname(domain) 
       os.system('clear')
       print("")
       print(purp +"╔─────> "+whit+domain)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve)
       print("")
       print(red+"command:"+yell+" b"+red+" - this command will take you back to menu")
       print("")
       print(red+"command:" +yell+" exit"+red+" - this command will exit the script")
       print("")

    elif numdom ==2:        #  Domain 2
       os.system('clear')
       print(yell+"                    ┌──────────────────────────────────┐")
       print("                    │    𝓦𝓮𝓵𝓬𝓸𝓶𝓮    𝓣𝓸    𝓓𝓸𝓶𝓪𝓲𝓷 "+yell+"Ꮙ 2   │")
       print("                    └────────┬────────────────┬────────┘")
       print("                             │"  +red+"  Enter Domain" +yell+"  │"        )
       print("                             └───┬───────┬────┘")
       print("                                 │"   +red+"   2" +yell+"   │")
       print("                                 └───────┘")
       print("")
       domain1 = raw_input(purp+"╔─────>"+yell+" ")
       domain2 = raw_input(purp+"╔─────>"+yell+" ") 
       resolve1 = socket.gethostbyname(domain1)
       resolve2 = socket.gethostbyname(domain2)
       os.system('clear')
       print("")
       print(purp +"╔─────> "+whit+domain1)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve1)
       print("")
       print(purp +"╔─────> "+whit+domain2)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve2)
       print("")
       print(red+"command:"+yell+" b"+red+" - this command will take you back to menu")
       print("")
       print(red+"command:" +yell+" exit"+red+" - this command will exit the script")
       print("")

    elif numdom ==3:    #Domain 3
       os.system('clear')
       print(yell+"                    ┌──────────────────────────────────┐")
       print("                    │    𝓦𝓮𝓵𝓬𝓸𝓶𝓮    𝓣𝓸    𝓓𝓸𝓶𝓪𝓲𝓷 "+yell+"Ꮙ 2   │")
       print("                    └────────┬────────────────┬────────┘")
       print("                             │"  +red+"  Enter Domain" +yell+"  │"        )
       print("                             └───┬───────┬────┘")
       print("                                 │"   +red+"   3" +yell+"   │")
       print("                                 └───────┘")
       print("")
       domain1 = raw_input(purp+"╔─────>"+yell+" ")
       domain2 = raw_input(purp+"╔─────>"+yell+" ") 
       domain3 = raw_input(purp+"╔─────>"+yell+" ")
       resolve1 = socket.gethostbyname(domain1)
       resolve2 = socket.gethostbyname(domain2)
       resolve3 = socket.gethostbyname(domain3)
       os.system('clear')
       print("")
       print(purp +"╔─────> "+whit+domain1)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve1)
       print("")
       print(purp +"╔─────> "+whit+domain2)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve2)
       print("")
       print(purp +"╔─────> "+whit+domain3)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve3)
       print("")
       print(red+"command:"+yell+" b"+red+" - this command will take you back to menu")
       print("")
       print(red+"command:" +yell+" exit"+red+" - this command will exit the script")
       print("")

    elif numdom==4:   #domain 4
       os.system('clear')
       print(yell+"                    ┌──────────────────────────────────┐")
       print("                    │    𝓦𝓮𝓵𝓬𝓸𝓶𝓮    𝓣𝓸    𝓓𝓸𝓶𝓪𝓲𝓷 "+yell+"Ꮙ 2   │")
       print("                    └────────┬────────────────┬────────┘")
       print("                             │"  +red+"  Enter Domain" +yell+"  │"        )
       print("                             └───┬───────┬────┘")
       print("                                 │"   +red+"   4" +yell+"   │")
       print("                                 └───────┘")
       print("")
       domain1 = raw_input(purp+"╔─────>"+yell+" ")
       domain2 = raw_input(purp+"╔─────>"+yell+" ") 
       domain3 = raw_input(purp+"╔─────>"+yell+" ")
       domain4 = raw_input(purp+"╔─────>"+yell+" ")
       resolve1 = socket.gethostbyname(domain1)
       resolve2 = socket.gethostbyname(domain2)
       resolve3 = socket.gethostbyname(domain3)
       resolve4 = socket.gethostbyname(domain4)
       os.system('clear')
       print("")
       print(purp +"╔─────> "+whit+domain1)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve1)
       print("")
       print(purp +"╔─────> "+whit+domain2)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve2)
       print("")
       print(purp +"╔─────> "+whit+domain3)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve3)
       print("")
       print(purp +"╔─────> "+whit+domain4)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve4)
       print("")
       print(red+"command:"+yell+" b"+red+" - this command will take you back to menu")
       print("")
       print(red+"command:" +yell+" exit"+red+" - this command will exit the script")
       print("")

    elif numdom==5:    #Domain 5
       os.system('clear')
       print(yell+"                    ┌──────────────────────────────────┐")
       print("                    │    𝓦𝓮𝓵𝓬𝓸𝓶𝓮    𝓣𝓸    𝓓𝓸𝓶𝓪𝓲𝓷 "+yell+"Ꮙ 2   │")
       print("                    └────────┬────────────────┬────────┘")
       print("                             │"  +red+"  Enter Domain" +yell+"  │"        )
       print("                             └───┬───────┬────┘")
       print("                                 │"   +red+"   5" +yell+"   │")
       print("                                 └───────┘")
       print("")
       domain1 = raw_input(purp+"╔─────>"+yell+" ")
       domain2 = raw_input(purp+"╔─────>"+yell+" ") 
       domain3 = raw_input(purp+"╔─────>"+yell+" ")
       domain4 = raw_input(purp+"╔─────>"+yell+" ")
       domain5 = raw_input(purp+"╔─────>"+yell+" ")
       resolve1 = socket.gethostbyname(domain1)
       resolve2 = socket.gethostbyname(domain2)
       resolve3 = socket.gethostbyname(domain3)
       resolve4 = socket.gethostbyname(domain4)
       resolve5 = socket.gethostbyname(domain5)
       os.system('clear')
       print("")
       print(purp +"╔─────> "+whit+domain1)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve1)
       print("")
       print(purp +"╔─────> "+whit+domain2)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve2)
       print("")
       print(purp +"╔─────> "+whit+domain3)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve3)
       print("")
       print(purp +"╔─────> "+whit+domain4)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve4)
       print("")
       print(purp +"╔─────> "+whit+domain5)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve5)
       print("")
       print(red+"command:"+yell+" b"+red+" - this command will take you back to menu")
       print("")
       print(red+"command:" +yell+" exit"+red+" - this command will exit the script")
       print("")
     
    elif numdom==6:    #Domain 6
       os.system('clear')
       print(yell+"                    ┌──────────────────────────────────┐")
       print("                    │    𝓦𝓮𝓵𝓬𝓸𝓶𝓮    𝓣𝓸    𝓓𝓸𝓶𝓪𝓲𝓷 "+yell+"Ꮙ 2   │")
       print("                    └────────┬────────────────┬────────┘")
       print("                             │"  +red+"  Enter Domain" +yell+"  │"        )
       print("                             └───┬───────┬────┘")
       print("                                 │"   +red+"   6" +yell+"   │")
       print("                                 └───────┘")
       print("")
       domain1 = raw_input(purp+"╔─────>"+yell+" ")
       domain2 = raw_input(purp+"╔─────>"+yell+" ") 
       domain3 = raw_input(purp+"╔─────>"+yell+" ")
       domain4 = raw_input(purp+"╔─────>"+yell+" ")
       domain5 = raw_input(purp+"╔─────>"+yell+" ")
       domain6 = raw_input(purp+"╔─────>"+yell+" ")
       resolve1 = socket.gethostbyname(domain1)
       resolve2 = socket.gethostbyname(domain2)
       resolve3 = socket.gethostbyname(domain3)
       resolve4 = socket.gethostbyname(domain4)
       resolve5 = socket.gethostbyname(domain5)
       resolve6 = socket.gethostbyname(domain6)
       os.system('clear')
       print("")
       print(purp +"╔─────> "+whit+domain1)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve1)
       print("")
       print(purp +"╔─────> "+whit+domain2)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve2)
       print("")
       print(purp +"╔─────> "+whit+domain3)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve3)
       print("")
       print(purp +"╔─────> "+whit+domain4)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve4)
       print("")
       print(purp +"╔─────> "+whit+domain5)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve5)
       print("")
       print(purp +"╔─────> "+whit+domain6)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve6)
       print("")
       print(red+"command:"+yell+" b"+red+" - this command will take you back to menu")
       print("")
       print(red+"command:" +yell+" exit"+red+" - this command will exit the script")
       print("")

    elif numdom==7:    #Domain 7
       os.system('clear')
       print(yell+"                    ┌──────────────────────────────────┐")
       print("                    │    𝓦𝓮𝓵𝓬𝓸𝓶𝓮    𝓣𝓸    𝓓𝓸𝓶𝓪𝓲𝓷 "+yell+"Ꮙ 2   │")
       print("                    └────────┬────────────────┬────────┘")
       print("                             │"  +red+"  Enter Domain" +yell+"  │"        )
       print("                             └───┬───────┬────┘")
       print("                                 │"   +red+"   7" +yell+"   │")
       print("                                 └───────┘")
       print("")
       domain1 = raw_input(purp+"╔─────>"+yell+" ")
       domain2 = raw_input(purp+"╔─────>"+yell+" ") 
       domain3 = raw_input(purp+"╔─────>"+yell+" ")
       domain4 = raw_input(purp+"╔─────>"+yell+" ")
       domain5 = raw_input(purp+"╔─────>"+yell+" ")
       domain6 = raw_input(purp+"╔─────>"+yell+" ")
       domain7 = raw_input(purp+"╔─────>"+yell+" ")
       resolve1 = socket.gethostbyname(domain1)
       resolve2 = socket.gethostbyname(domain2)
       resolve3 = socket.gethostbyname(domain3)
       resolve4 = socket.gethostbyname(domain4)
       resolve5 = socket.gethostbyname(domain5)
       resolve6 = socket.gethostbyname(domain6)
       resolve7 = socket.gethostbyname(domain7)
       os.system('clear')
       print("")
       print(purp +"╔─────> "+whit+domain1)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve1)
       print("")
       print(purp +"╔─────> "+whit+domain2)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve2)
       print("")
       print(purp +"╔─────> "+whit+domain3)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve3)
       print("")
       print(purp +"╔─────> "+whit+domain4)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve4)
       print("")
       print(purp +"╔─────> "+whit+domain5)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve5)
       print("")
       print(purp +"╔─────> "+whit+domain6)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve6)
       print("")
       print(purp +"╔─────> "+whit+domain7)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve7)
       print("")
       print(red+"command:"+yell+" b"+red+" - this command will take you back to menu")
       print("")
       print(red+"command:" +yell+" exit"+red+" - this command will exit the script")
       print("")

    elif numdom==8:    #Domain 8
       os.system('clear')
       print(yell+"                    ┌──────────────────────────────────┐")
       print("                    │    𝓦𝓮𝓵𝓬𝓸𝓶𝓮    𝓣𝓸    𝓓𝓸𝓶𝓪𝓲𝓷 "+yell+"Ꮙ 2   │")
       print("                    └────────┬────────────────┬────────┘")
       print("                             │"  +red+"  Enter Domain" +yell+"  │"        )
       print("                             └───┬───────┬────┘")
       print("                                 │"   +red+"   8" +yell+"   │")
       print("                                 └───────┘")
       print("")
       domain1 = raw_input(purp+"╔─────>"+yell+" ")
       domain2 = raw_input(purp+"╔─────>"+yell+" ") 
       domain3 = raw_input(purp+"╔─────>"+yell+" ")
       domain4 = raw_input(purp+"╔─────>"+yell+" ")
       domain5 = raw_input(purp+"╔─────>"+yell+" ")
       domain6 = raw_input(purp+"╔─────>"+yell+" ")
       domain7 = raw_input(purp+"╔─────>"+yell+" ")
       domain8 = raw_input(purp+"╔─────>"+yell+" ")
       resolve1 = socket.gethostbyname(domain1)
       resolve2 = socket.gethostbyname(domain2)
       resolve3 = socket.gethostbyname(domain3)
       resolve4 = socket.gethostbyname(domain4)
       resolve5 = socket.gethostbyname(domain5)
       resolve6 = socket.gethostbyname(domain6)
       resolve7 = socket.gethostbyname(domain7)
       resolve8 = socket.gethostbyname(domain8)
       os.system('clear')
       print("")
       print(purp +"╔─────> "+whit+domain1)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve1)
       print("")
       print(purp +"╔─────> "+whit+domain2)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve2)
       print("")
       print(purp +"╔─────> "+whit+domain3)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve3)
       print("")
       print(purp +"╔─────> "+whit+domain4)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve4)
       print("")
       print(purp +"╔─────> "+whit+domain5)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve5)
       print("")
       print(purp +"╔─────> "+whit+domain6)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve6)
       print("")
       print(purp +"╔─────> "+whit+domain7)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve7)
       print("")
       print(purp +"╔─────> "+whit+domain8)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve8)
       print("")
       print(red+"command:"+yell+" b"+red+" - this command will take you back to menu")
       print("")
       print(red+"command:" +yell+" exit"+red+" - this command will exit the script")
       print("")

    elif numdom==9:    #Domain 9
       os.system('clear')
       print(yell+"                    ┌──────────────────────────────────┐")
       print("                    │    𝓦𝓮𝓵𝓬𝓸𝓶𝓮    𝓣𝓸    𝓓𝓸𝓶𝓪𝓲𝓷 "+yell+"Ꮙ 2   │")
       print("                    └────────┬────────────────┬────────┘")
       print("                             │"  +red+"  Enter Domain" +yell+"  │"        )
       print("                             └───┬───────┬────┘")
       print("                                 │"   +red+"   9" +yell+"   │")
       print("                                 └───────┘")
       print("")
       domain1 = raw_input(purp+"╔─────>"+yell+" ")
       domain2 = raw_input(purp+"╔─────>"+yell+" ") 
       domain3 = raw_input(purp+"╔─────>"+yell+" ")
       domain4 = raw_input(purp+"╔─────>"+yell+" ")
       domain5 = raw_input(purp+"╔─────>"+yell+" ")
       domain6 = raw_input(purp+"╔─────>"+yell+" ")
       domain7 = raw_input(purp+"╔─────>"+yell+" ")
       domain8 = raw_input(purp+"╔─────>"+yell+" ")
       domain9 = raw_input(purp+"╔─────>"+yell+" ")
       resolve1 = socket.gethostbyname(domain1)
       resolve2 = socket.gethostbyname(domain2)
       resolve3 = socket.gethostbyname(domain3)
       resolve4 = socket.gethostbyname(domain4)
       resolve5 = socket.gethostbyname(domain5)
       resolve6 = socket.gethostbyname(domain6)
       resolve7 = socket.gethostbyname(domain7)
       resolve8 = socket.gethostbyname(domain8)
       resolve9 = socket.gethostbyname(domain9)
       os.system('clear')
       print("")
       print(purp +"╔─────> "+whit+domain1)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve1)
       print("")
       print(purp +"╔─────> "+whit+domain2)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve2)
       print("")
       print(purp +"╔─────> "+whit+domain3)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve3)
       print("")
       print(purp +"╔─────> "+whit+domain4)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve4)
       print("")
       print(purp +"╔─────> "+whit+domain5)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve5)
       print("")
       print(purp +"╔─────> "+whit+domain6)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve6)
       print("")
       print(purp +"╔─────> "+whit+domain7)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve7)
       print("")
       print(purp +"╔─────> "+whit+domain8)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve8)
       print("")
       print(purp +"╔─────> "+whit+domain9)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve9)
       print("")
       print(red+"command:"+yell+" b"+red+" - this command will take you back to menu")
       print("")
       print(red+"command:" +yell+" exit"+red+" - this command will exit the script")
       print("")

    elif numdom==10:    #Domain 10
       os.system('clear')
       print(yell+"                    ┌──────────────────────────────────┐")
       print("                    │    𝓦𝓮𝓵𝓬𝓸𝓶𝓮    𝓣𝓸    𝓓𝓸𝓶𝓪𝓲𝓷 "+yell+"Ꮙ 2   │")
       print("                    └────────┬────────────────┬────────┘")
       print("                             │"  +red+"  Enter Domain" +yell+"  │"        )
       print("                             └───┬───────┬────┘")
       print("                                 │"   +red+"   10" +yell+"  │")
       print("                                 └───────┘")
       print("")
       domain1 = raw_input(purp+"╔─────>"+yell+" ")
       domain2 = raw_input(purp+"╔─────>"+yell+" ") 
       domain3 = raw_input(purp+"╔─────>"+yell+" ")
       domain4 = raw_input(purp+"╔─────>"+yell+" ")
       domain5 = raw_input(purp+"╔─────>"+yell+" ")
       domain6 = raw_input(purp+"╔─────>"+yell+" ")
       domain7 = raw_input(purp+"╔─────>"+yell+" ")
       domain8 = raw_input(purp+"╔─────>"+yell+" ")
       domain9 = raw_input(purp+"╔─────>"+yell+" ")
       domain10 = raw_input(purp+"╔─────>"+yell+" ")
       resolve1 = socket.gethostbyname(domain1)
       resolve2 = socket.gethostbyname(domain2)
       resolve3 = socket.gethostbyname(domain3)
       resolve4 = socket.gethostbyname(domain4)
       resolve5 = socket.gethostbyname(domain5)
       resolve6 = socket.gethostbyname(domain6)
       resolve7 = socket.gethostbyname(domain7)
       resolve8 = socket.gethostbyname(domain8)
       resolve9 = socket.gethostbyname(domain9)
       resolve10 = socket.gethostbyname(domain10)
       os.system('clear')
       print("")
       print(purp +"╔─────> "+whit+domain1)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve1)
       print("")
       print(purp +"╔─────> "+whit+domain2)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve2)
       print("")
       print(purp +"╔─────> "+whit+domain3)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve3)
       print("")
       print(purp +"╔─────> "+whit+domain4)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve4)
       print("")
       print(purp +"╔─────> "+whit+domain5)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve5)
       print("")
       print(purp +"╔─────> "+whit+domain6)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve6)
       print("")
       print(purp +"╔─────> "+whit+domain7)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve7)
       print("")
       print(purp +"╔─────> "+whit+domain8)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve8)
       print("")
       print(purp +"╔─────> "+whit+domain9)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve9)
       print("")
       print(purp +"╔─────> "+whit+domain10)
       print(purp +"║"   + yell +  "   𝓓𝓸𝓶𝓪𝓲𝓷     𝓣𝓸       𝓘𝓹")
       print(purp +"╚─────> "+gree+resolve10)
       print("")
       print(red+"command:"+yell+" b"+red+" - this command will take you back to menu")
       print("")
       print(red+"command:" +yell+" exit"+red+" - this command will exit the script")
       print("")

    else:
       print("")
       print(red +"Error try again")
       time.sleep(2)
       restart()

    end = raw_input(yell+"───>"+red+" :" ) # closes script
    if end =='b':
       restart()
    elif end =='exit':
         os.system('clear')
         print(yell+"𝓒𝓵𝓸𝓼𝓲𝓷𝓰")
         time.sleep(3)
         os.system('clear')
         exit()

domain() # Start domain funaction

