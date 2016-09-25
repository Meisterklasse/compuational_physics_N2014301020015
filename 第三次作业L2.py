   #1.1版本减少了电脑的运算量   
   #用line_N[X]语句，全部直接输出字符串的一部分  
   #省去了上一版本横向移动的循环中不断修改line_N的操作   

line_0 = ".......／￣￣￣Y￣￣＼       "  
line_1 = "　 　l　　　　　　　　　l     "
line_2 = "     \,,,,,／￣￣￣￣、ﾉ     "  
line_3 = "　　　|:::::　　　　　　l    "  
line_4 = "　　　|:::　　＿_　　　|     "  
line_5 = "　　（6　　　＼●>　<● 人     "  
line_6 = "　　　!　　　　)・・(　l     "      
line_7 = "　　　c　　　　　(三)　ﾉ     "  
line_8 = "　　　／＼　　　　二　ノ     "  
line_9 = "　   　/⌒c.‘`—一*＼        "  
   
xmax=70                       #改变xmax和ymax可改变横竖移动范围
ymax=30  
decelerationY=3                #改变decelerationY可调节y方向上移动的速度   
  
line_0 = xmax*" "+str(line_0)    #直接设定总line_N,以后直接输出其某部分
line_1 = xmax*" "+str(line_1)    #从左边延长字符串
line_2 = xmax*" "+str(line_2)  
line_3 = xmax*" "+str(line_3)  
line_4 = xmax*" "+str(line_4)  
line_5 = xmax*" "+str(line_5)  
line_6 = xmax*" "+str(line_6)  
line_7 = xmax*" "+str(line_7)  
line_8 = xmax*" "+str(line_8)  
line_9 = xmax*" "+str(line_9)
  
for x in range(xmax,-1,-1):    #右平移   
    import os  
    i = os.system('cls')       #省去了循环中不断修改line_N的操作
    print line_0[x:]  
    print line_1[x:]  
    print line_2[x:]  
    print line_3[x:]  
    print line_4[x:]  
    print line_5[x:]  
    print line_6[x:]  
    print line_7[x:]  
    print line_8[x:]  
    print line_9[x:]  
    import time
    time.sleep(0.005)
    
line_00 = ".......／￣￣￣Y￣￣＼       "  
line_01 = "　 　l　　　　　　　　　l     "
line_02 = "     \,,,,,／￣￣￣￣、ﾉ     "  
line_03 = "　　　|:::::　　　　　　l    "  
line_04 = "　　　|:::　　\　　/　|     "  
line_05 = "　　（6　　　＼●>　<● 人     "  
line_06 = "　　　!　　　　)・・(　l     "      
line_07 = "　　　c　　　　　(四)　ﾉ     "  
line_08 = "　　　／＼　　　　二　ノ     "  
line_09 = "　   　/⌒c.‘`—一*＼        "  

line_00 = xmax*" "+str(line_00)    #直接设定总line_N,以后直接输出其某部分
line_01 = xmax*" "+str(line_01)    #从左边延长字符串
line_02 = xmax*" "+str(line_02)  
line_03 = xmax*" "+str(line_03)  
line_04 = xmax*" "+str(line_04)  
line_05 = xmax*" "+str(line_05)  
line_06 = xmax*" "+str(line_06)  
line_07 = xmax*" "+str(line_07)  
line_08 = xmax*" "+str(line_08)  
line_09 = xmax*" "+str(line_09)
      
for y in range(ymax*decelerationY):       #下平移
    import os                             #不明提示???shadowed by loop variable
    i = os.system('cls')   
    y_deceleration = int(y/decelerationY)  
    for j in range(y_deceleration):  
        print " "  
    print line_00  
    print line_01  
    print line_02  
    print line_03  
    print line_04  
    print line_05  
    print line_06  
    print line_07  
    print line_08  
    print line_09
    import time
    time.sleep(0.005)
    
line_10 = "  ／￣￣Y￣￣￣＼.......       "  
line_11 = " l　　　　　　　　l     "
line_12 = " \ /￣￣￣￣\,,,,/    "  
line_13 = "  l　      　:::::|　　　　　　"  
line_14 = " |　　  _＿　  :::|　    "  
line_15 = "  人 ●>　<● /　　 3|　   "  
line_16 = "|    )・・(　     | "      
line_17 = " \  　(三)　c　    ﾉ     "  
line_18 = "　 \  　二       ／＼　　　   "  
line_19 = "　  /⌒c.‘`—一*＼        "  

line_10 = xmax*" "+str(line_10)    #直接设定总line_N,以后直接输出其某部分
line_11 = xmax*" "+str(line_11)    #从左边延长字符串
line_12 = xmax*" "+str(line_12)  
line_13 = xmax*" "+str(line_13)  
line_14 = xmax*" "+str(line_14)  
line_15 = xmax*" "+str(line_15)  
line_16 = xmax*" "+str(line_16)  
line_17 = xmax*" "+str(line_17)  
line_18 = xmax*" "+str(line_18)  
line_19 = xmax*" "+str(line_19)

for m in range(xmax):                   #左平移
    import os  
    i = os.system('cls')  
    for j in range(y_deceleration):  
        print " "  
    print line_10[m:]                  #省去了循环中不断修改line_N的操作
    print line_11[m:]  
    print line_12[m:]  
    print line_13[m:]  
    print line_14[m:]  
    print line_15[m:]  
    print line_16[m:]  
    print line_17[m:]  
    print line_18[m:]  
    print line_19[m:]  
    import time
    time.sleep(0.005)
    
line_20 = "  ／￣￣Y￣￣￣＼.......       "  
line_21 = " l　　　　　　　　l     "
line_22 = " \ /￣￣￣￣\,,,,/    "  
line_23 = "  l　      　:::::|　　　　　　"  
line_24 = " |　 \　  /    :::|　    "  
line_25 = "  人 ●>　<● /　　 3|　   "  
line_26 = "|    )・・(　     | "      
line_27 = " \  　(四)　c　    ﾉ     "  
line_28 = "　 \  　二       ／＼　　　   "  
line_29 = "　  /⌒c.‘`—一*＼        "  

line_20 = xmax*" "+str(line_20)    #直接设定总line_N,以后直接输出其某部分
line_21 = xmax*" "+str(line_21)    #从左边延长字符串
line_22 = xmax*" "+str(line_22)  
line_23 = xmax*" "+str(line_23)  
line_24 = xmax*" "+str(line_24)  
line_25 = xmax*" "+str(line_25)  
line_26 = xmax*" "+str(line_26)  
line_27 = xmax*" "+str(line_27)  
line_28 = xmax*" "+str(line_28)  
line_29 = xmax*" "+str(line_29)
  
for y in range(ymax*decelerationY,0,-1):    #上平移
    import os  
    i = os.system('cls')  
    y_deceleration = int(y/decelerationY)  
    for j in range(y_deceleration):  
        print " "  
    print line_20[xmax:]  
    print line_21[xmax:]  
    print line_22[xmax:]  
    print line_23[xmax:]  
    print line_24[xmax:]  
    print line_25[xmax:]  
    print line_26[xmax:]  
    print line_27[xmax:]  
    print line_28[xmax:]  
    print line_29[xmax:]  
    import time
    time.sleep(0.005)
