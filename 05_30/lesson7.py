try:
	with open("student.txt", "r", encoding="utf-8") as file:
			data = file.read()
			print(data)
except Exception as e:
	print("發生錯誤:", e)
	
#----------------------------------------

#open("student.txt")引數值的呼叫,必須按照順序
try:
    with open("student.txt") as file:
        data = file.read()
        print(data)
except Exception as e:
    print("發生錯誤：", e)

#----------------------------------------

