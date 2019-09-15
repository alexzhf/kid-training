import easygui

user_response = easygui.msgbox("hello 你好")

print(user_response)

flavor = easygui.buttonbox("你最喜欢的冰淇淋口味是？",
                           choices=['香草', '巧克力', '草莓'])
easygui.msgbox("你最爱的冰淇淋口味是" + flavor+"!")

flavor = easygui.choicebox("你最喜欢的冰淇淋口味是？",
                           choices=['香草', '巧克力', '草莓'])
easygui.msgbox("你最爱的冰淇淋口味是" + flavor+"!")

flavor = easygui.enterbox("请输入你喜欢的冰淇淋口味？")
easygui.msgbox("你最爱的冰淇淋口味是" + flavor+"!")

flavor = easygui.enterbox("请输入你喜欢的冰淇淋口味？", default="抹茶")
easygui.msgbox("你最爱的冰淇淋口味是" + flavor+"!")

