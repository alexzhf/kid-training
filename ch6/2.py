import easygui

age_xm_str = easygui.enterbox("请输入小明的年龄：")

age_father = 30.5 + float(age_xm_str)
easygui.msgbox("因为爸爸比小明大30.5岁，所以爸爸的年龄是：" + str(age_father))

age_grandfather = 30.5 + age_father
easygui.msgbox("因为爷爷比爸爸大30.5岁，所以爷爷的年龄是：" + str(age_grandfather))
