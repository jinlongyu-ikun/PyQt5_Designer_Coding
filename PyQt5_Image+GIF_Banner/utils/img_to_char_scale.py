# author jinyunlong
# createtime 2023/3/15 22:55
# 职业 锅炉房保安
import os

from PIL import Image


def img2charTxt(filename, scale, txtname):
    ascii_chars = "MNHQ$CXKAO67+>!:-. "
    img = Image.open(filename)
    img = img.convert("L")
    w, h = img.size
    new_w = int(w * scale)
    new_h = int(h * scale)
    img = img.resize((int(new_w * 1.75), new_h))
    w, h = img.size
    data = img.load()
    result = []
    n = len(ascii_chars)-1
    for y in range(h):
        line = "".join(ascii_chars[data[x, y]*n//255] for x in range(w))
        line += "\n"
        result.append(line)
    with open(txtname, "w") as f:
        f.writelines(result)



# 示例用法
# 获取当前脚本所在文件夹的路径
# current_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(current_dir, '..', 'image', 'cai.jpg')
# img2charTxt(file_path, 0.2, 'cai_image.txt')

# https://zhuanlan.zhihu.com/p/573554229
# https://www.degraeve.com/img2txt.php

'''

666666666777777777777777777777------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
776666666777777777777777777777------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
>>+666777777777777777777777777------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
>>!>77677777777777777777777777------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
>>>!!>777777777777777777777777------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
>>>>!!!>7777777777777777777777------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
>>>>>!!!!>77777777777777777777---------------------------------------------------------------------------------------:+6OO67+>:-----------------------------------------------------------------------------------
>>>>>!!!!!!>+77777777777777777-----------------------------------------------------------------------------------:!+7ACCXXXKKKA6+>:-------------------------------------------------------------------------------
>>>>>>!!>>!!!>7667777777777777----------------------------------------------------------------------------------!7AKX$Q$XXXCCCXXKA6>------------------------------------------------------------------------------
>>>>>>!!!!!!!!>>77777777777777--------------------------------------------------------------------------------->AKXXX$$KKC$$$$CCXXKA+-----------------------------------------------------------------------------
>>>!!!!!!!!!!!!!!+777777777777--------------------------------------------------------------------------------!AKXXXCK7!7$Q$$CCCCXXXK+----------------------------------------------------------------------------
>>>!!!!!!!!!!!!!!!!+7777777777-------------------------------------------------------------------------------!OKXXCCX6+>O$CCCXKAAKXXXX+---------------------------------------------------------------------------
>>>!!!!!!!!!!!!!!!!!!+77777777------------------------------------------------------------------------------!6KXCC$$CAO76AKKKA7!!>AXAA>---------------------------------------------------------------------------
>>>!!!!!!!!!!!!!!!!!!!>+777777-----------------------------------------------------------------------------:+AXC$$$CO6A6>!>>>!!!!!76++!---------------------------------------------------------------------------
>>>!!!!!!!!!!!!!!!!!!!!!!+7777------------------------------------------------------------------------------:OX$$Q$O6O7>>>++>!!>>>>+7+:---------------------------------------------------------------------------
>>>!!!!!!!!!!!!!!!!!!!!!!!!+77------------------------------------------------------------------------------->OC$QQ6>!!!+66+>!>>>>>+76!.--------------------------------------------------------------------------
>>>!!!!!!!!!!!!!!!!!!!!!!!!!>+--------------------------------------------------------------------------------:7XQQA>>>>>6A6OO+>>>++XNC7++!:----------------------------------------------------------------------
>>>!!!!!!!!!!!!!!!!!!!!!!!!!!!!:--------------------------------------------------------------------------------!7KA6++++OA6O7>>>+7OQHHHHHQ$X6++!-----------------------------------------------------------------
>>>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:---------------------------------------------------------------------------------:+67+++77+>!>+6A$HHHHHQHHHHHH$X>--::-----------------------------------------------------------
>>>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:---------------------------------------------------------------------------------:>!+7>>++76OA$HHHHH$$HHHHHHHN7.-KCK7:--------------------------------------------------------
>>>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:----------------------------------------------------------------------------------A$CKAOOOA$HHHHH$CHHHHHHHHH>.-CHHH$CCCX7---------------------------------------------------
>>>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:-------------------------------------------------------------------------------ANNNHQXXCHNNHQ$$QHHHHHHHHNQ!-!QHQQHHHHNQ:.-------------------------------------------------
>>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:-------------------------------------------------------------------------->:>HNHHHNNNNNHQC$HNHHHHHHHHHNQ!->QHHHHHHHHHX+.------------------------------------------------
>>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:---------------------------------------------------------------------->CX!+HNHHHNNH$C$QNNNHHNHHHHHHHNH+:>QHHHHHHHHHHHO!-----------------------------------------------
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:-------------------------------------------------------------------7QNX!>$HCNHQ$$QHNNNNHHHHHHHHHHHHN7:+HHHHHHHHHHHHHQO!---------------------------------------------
-:!!!>>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:---------------------------------------------------------------!XHHN$>!O$QQ$$HNNNNNNNNHHHHHNNNNNNNA!>$NHHHHHHHHHHHHHHX>-------------------------------------------
---:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:------------------------------------------------------------:CNHHNN6!>$$QHNHHNNNNNNNHHHHHNNNNNNN$>>ANNHHHHHHHHHHHHHH$X+-----------------------------------------
-----:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>!!:----------------------------------------------------------6NHHHNMK!!ANNNNNHHHHHHHHHNNNNNNNNNNNNO>+$NNNHHNNNHHHHHHHHHQK7A7-------------------------------------
-------:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:--------------------------------------------------------KNHHHNX!!>7HNNNNHHHHHHHHHNNNNNNNNNNNNQ++ONNNNNNNNNNHHHHHHHHHHHQO!-----------------------------------
---------:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:------------------------------------------------------KNHHHNXAK+>CNHNNHHHHNNNNNNNNNNNNNNNNNNK++XNNNNNNHNNNHHHHHHHHHHHNQO:---------------------------------
-----------:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>!!:---------------------------------------------------.ANHHHHNNN7>ONNHHHHHNNNNNNNNNNNNNNNNNNNH7+6QNNNNH76CQNNNHHHHHHHHHHNX:--------------------------------
-------------:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:------------------------------------------------->$NHHNHHHNX>+$NHHHHHNNNNNNNNNNNNNNNNNNNNX++KNNNNC:.-:+KQHHQNHHHHHHHNX!-------------------------------
---------------:!!>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:-----------------------------------------------XNHHHNNNNNH+>ONNHHHHNNNNNNNNNNNNNNNNNNNNNO+7HNNNA.-----:!:>HNHHHNHHHHC+------------------------------
-----------------:!!>>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!:-------------------------------------------.6HHHHNNNNNNMA!+HNNNHNNNNNNNNNNNNNNNNNNNNNM$77KMNNQ>--------ONNNNNNHHHHHQ7-----------------------------
-------------------:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>!::-----------------------------------------:QHHHHNNNNNNNQ+>KNNNNNNNNNNNNNNNNNNNNNNNNNNNO77HNNN$>------:XMNNNNNNHHHHHQ7----------------------------
---------------------:!!!!!!!!!!!!!!!!!!!!>>>>>!!!!!!!!!!!!!!!!!!!::-------------------------------------:>XNHHHNNNNNNNNHO>+HNNNNNNNNNNNNNNNNNNNNNNNNNNQ7+KNNNNQ!------:O$QHNNNNHHHHHHO---------------------------
-----------------------:!!!!!>!!!!!!!!!!!>>>>>>>!!!!!!!!!!!!!!!!!!!!::-----------------------------------+HNHHHHNNNNNNNN67>>CNHHHNNNNNNNNNNNNNNNNNNNNNNNK76QNNNNC:--------:!CMNNHHHHHHHO:-------------------------
-------------------------:!!>>!!!!!!!!!!>>>>>>>>>>>>>!!!!!!!!!!!!!!>!!::---------------------------------:CNHHNNNNNNNNNC:>+>7NNHHNNNNNNNNNNNNNNNNNNNNNNN$77CMNNNNO----------!CNNHHHHHHHHA:------------------------
---------------------------:!>>!!!!!!>>>>>>>>>>>>>>>>>>>>>!!!!!!!!!!!>!!::------------------------------:7CHHHNNNNNNNNH>:$X>>CNNNNNNNNNNNNNNNNNNNNNNNNNNHAOQNNNNNO-----------:AHNHHHHHHHHA!-----------------------
----------------------------::!!!!!!!>>>>>>>>>>>>>>>>>>>>>!!!!!!!!!!!!!>!!:----------------------------.7HHHHHHNNNNNMMK--:+>>6NNNNNNNNNNNNNNNNNNNNNNNNNNNHCQNNNQA:-------------+CHNNHHHHHHK:----------------------
------------------------------::!!!!!>>>>>>>>>>>>>>>>>>>!!!!!!!!!!!!!!!!!!!!::--------------------------XNHHHHHHNNQA67:-----++XNNNNNNNNNNNNNNNNNNNNNNNNNNHXK$$6-----------------:+A$HHHHHHHK:---------------------
--------------------------------::!>>>>>>>!!!>>>>>>>>>>>!!!!!!!!!!!!!!!!!!!!!!::-----------------------OHHHHHHHHNN+..------.77+$NNNNNNNNNNNNNNNNNNNNNHQQ$CCXXX7.-------------------:7HHHHHHHA!:-------------------
----------------------------------:!!>>>>>>>>>>>>>>>>>>>!!!!!!!!!!!!!!!!!!!>!!!!::--------------------!QHHHHHHHNNNO--------!$X77$HHNNNNNHHHHHHHHHQQ$$CXCCCXXXXK!--------------------!QNHH$XKA+:-------------------
------------------------------------:!!>>>>>>>>>>>>>>>>>!!!!!!!!!!!!!!!!!!!>>>>>>!:------------------:OQHHHHHHNNNN$:------->K$$XXCQHHHHHQQQQ$$$QCCCCXXXXXXXXXKKA:-------------------:KQXO7+>>>!::-:---------------
--------------------------------------:!!>>>>>>>>>>>>>>>>>>>>!!!!!!!!!!!!!!>>>>>>>!!::--------------:6QQHHHHHH$KO7>:------:-OQ$$$$$$QQQQQQQ$$$$$CCCXXXXXXXXKKKAK6-------------------->777++>>>+>:-:-----------::::
----------------------------------------:!>>>>>>>>>>>>>>>>>>>!!!!!!!!!!!!!!>>>>>>>>>>!::-----------:!KCC$QHH$A+:-----------+CCCCCCCCC$$CCCCCCCCCCXXXXXKKKKKKKKKKX!-------------------:!7+!>+++77!-------------::::
------------------------------------------:!!>>>>>>>>>>>>>>>>>>>>>>!!!!!>>>>>>>>>>>>>>>!::--------:!+6OOAXQA>!:::----------6XKKKKKKXXXCCCCCXXXXXXXXXXXXXKKKKKKKKX>---::---------------!6>--+776O>----------:::::::
--------------------------------------------:!>>>>>>>>>>>>>>>>>>>>>!!!!!>>>>>>>>>>>>>>>>>!::-----:!>++776OK>::-::----------.7AAAAAAAAKKXXCC$$XKKKXXXXXCXXXXXXKKKK>---::---------------!7>-->66O6:----------:::::::
:::-------------------------------------------:!!>>>>>>>>!>>>>>>>>>!!!!!>>>>>>>>>>>>>>>>>>>!:::::!!>>>>++76>::-::-----------OAAOOOOOOOAAKKXXC$$XXXKKKKXXXXXKKKKKK!-:-::---------------:::-->OOO!-----:::::::::::::
::::--------------------------------------------:!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>!>>!!!!>>>>>>>>>+>:--:::---------:AAAAOOOOOOOOAKKKXC$$CCXXKKKXXXXXKKKKA:-------------------------6O7:---::::::::::::::::
::::----------------------------------------------:!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>+>>++>>>>>:--:::--------->AAAAOOOOOO6OOAKKKX$CCCXXXXKKKKKKKKKKA!------------------------:>!----:::::::::::::::::
:::::-----------------------------------------------:!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>+++++++>>77>>>>+!--:::--------->KAAOOO666666OOAKKXC$CXXXXXKKKKKKKKKKK+-------------:::-------::::::-::::::::::::::::::
:::::-------------------------------------------------:!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>++++++++7>+67>>!>7!--:::----------!7AKAO6666666OOAKKC$$CXKKKXKKKKKKKKAA6-----:::::::::::::::::::::::::::::::::::::::::::
:::::---------------------------------------------------:!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>++++++++77+767+>>>7>-----------------!AOO666666666OOKAC$CCCXKXXXKKKKKKAAA:----:::::::::::::::::::::::::::::::::::::::::::
:::::::---------------------------------------------------:!>>>>>>>>>>>>>>>>>>>>>>>>>>>++++++++++777667777+7+:-----------------7OO66666666666A7XCCCCCXKKKKKKKKAAAA>---::::::::::::::::::::::::::::::::::::::::::::
:::::::-----------------------------------------------------:!>>>>>>>>>>>>>>>>>>>>>>>>++77777777777666766766+!:----------------:OO66666666666O6A$XCCCCCXKKKKKKKAAA7---::::::::::::::::::::::::::::::::::::::::::::
:::::::-----------------------------------:::-----------------:!>>>>>>>>>>>>>>>>>>>>>+777777777777666676666OO+!-----------------+A666667766666O+ACXXCCCCXKKKKKKKAAO---::::::::::::::::::::::::::::::::::::::::::::
:::::-------------------------------------:::-------------------:!>>>>>>>>>>>>>>>>>>>7766677777766666666666AA6>------------------7O66667777666O6-KXXXXXXXXXKKKKKAAO-------::::::::::::::::::::::::::::::::::::::::
:::::-------------------------------------:::---------------------:!>>>>>>>>>>>>>>>>+76OO666666666666666OOOAAA+:::--:------------:OO6666666666OO-7CXXXXXXXXXKKKKAAA:------::::::::::::::::::::::::::::::::::::::::
::::::---::---------------------------------------------------------:!>>>>>>>>>>>>>>>7OA6666666OOOOOOOOOOOAAKA7!!!::------------:->O666666666OOA!:XXXXXXXXXXXKKKKAA>---:::::::::::::::::::::::::::::::::::::::::::
:::::::-:::::::::-----------------------------------------------------:!>>>>>>>>>>>>>7OAO66OOOOOOOOOOOOOOAKKKO+!>>!!::-----------:+OOOOOOOOOOOAK:.6CXXXXXXXXXXKKKAK7---:::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::------------------------------------------------------::!>>>>>>>>>>>+6OOOOOOAAAAAAAAAAAAKKKA7>>>>>>>!::--------!OAAAAAAAAAAAAXO-.7$XXXXXXXXXXKKKKKO--::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::----------------------::-------:::::::---------------::--:!>>>>>>>>>++66OOOAAAAAAAAAAAKKKAA7+>>>>>>>>>!:-------7AOAAAAAAAAKKK$+--+$XXXXXXXXXKKKKKKA!-::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::--------------:::::::::-----:::::::::--------::::--::::--:!>>>>>>>>++76OAAAAAAAAAAAAAAO67+>>>>>>>>>>>>!::-:--7KOOOAAAAAKKKKA!--:6XXXXXXXXKKKKKKKK>-::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::------::::::::::---::!>>>>>>>++7766OOOOOOOOOO6677+>>>>>>>>>>>>>>>!:---:6AAAAAAKKKKKX!-::--+$XXXXXXKKKKKKKK+-::::::::::::::::::::::::::::::::::::::::::::
::::::-------------------------------------------------------------::::::::::--::!>>>>>>>+++777766666677++>>>>>>>>>>>>>>>>>>!!:--7AAAAKKKKKKKX:-:::--ACXXXXXKKKKKKKKO:-:::::::::::::::::::::::::::::::::::::::::::
!!!!!!!!!!!:::::::::::::::::::::::::::::::::::::::::::::::---------:::::::::------:!!>>>>>+++++7777777++>>>>>>>>>>>>>>>>>>>>>>!::OOAAAKKKKKKXA-------OCXXXKKKKKKKKKKA:-:::::::::::::::::::::::::::::::::::::::::::
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>++++++++++++++++++++++++++++++++++++>>>>+OAAAAKKKKKKK+:!!!!:!OXXXXKKKKKKKKKKO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>+++++++++++++++++++++++++++++++>>>>>>>>>>>>>>+OAAAKKKKKKKK7!>>>>>++OKXXXKKKKKKKKKO>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>+>>>>>>>>>>>+>>>+>++>>>>>>>>>>>>>>>>>>>>>>>>OAAAKKKKKKKK7!>>>+6OOAKKXXXXXKKKKKKA+>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>OAAAKKKKKKKK7!>+6OOAAKKKKXXXXXKKKKKA+>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>!7AAAAKKKKAAAA77OAAAAAKCXKXXXXXXKKKKO>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>!>>!>>!+AAAAKKKKAAAOOOAAKKKKKKXXXXXXXXXXXK6>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>!!!!!!!!>>>>>>>>>>>>>>>!!!!!!!!!!!!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>!!!>>>>>!!!!+AAAAAKKKAAAOOAAKKKKKKKKXXXXXXXXXXO>>>>>>>!>>>!!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>!!!>>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>>>>!!!!!!!!!!!>!!!!!!!!!!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>!!!!!>>>!!!!>OAAAAKKKAAAOOAKKXXXXXXXXKKKKAAO6+>>>>>>>>!!!!!!!>>>!>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!>>!!!>>>>>>>>>>>>>>>>>!!>>>>>>>>>>>>>>>>>>>>>!>>>>>>!!!!!!!!!!!!!!!!!!!!!>OAAKKKKKAAAAAAKXXXXXXA6+>!>>!!!!!!>>!!!!!!!!!!!!!!!!!!>>>>>>>>>>>>>>>>>>>>>>>>>>

'''