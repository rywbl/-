import os
import os.path
import re
def test(allStr):
	LenallStr = len(allStr) -1
	for i in range(LenallStr):
		find = allStr[i].find("@")
		if find != -1 :
			return allStr.split(",")[i]

def work(path):
	resPath = r"D:\python-project\result"
	#打开文件
	f = open(path,"r",encoding = "UTF-8-sig")
	#处理每一行数据
	lineNo = 0
	while lineNo < 2000:
		lineInfo = f.readline()
		#曹阳,32010619720506042x,F,19720506,-,210005,13770848687,025-842019149,-,cy_qing@163.com,0
		lineword = lineInfo.split(",")
		name_pattern = r"(\w+),"
		nameStr = re.findall(name_pattern,lineInfo)
		if len(nameStr) == 0 :
			break
		print(nameStr[0])
		#nameStr = lineInfo.split(",")[0]
		#获取邮箱的字符串 cy_qing@163.com
		#
		email_pattern = r".*,(.*@.*),"
		mailStr = re.findall(email_pattern,lineInfo)
		if len(mailStr) == 0:
			continue
		print(mailStr[0])
		print(type(mailStr[0]))
		
		dirStrTemp1 = mailStr[0].split("@")
		dirStrTemp = dirStrTemp1[1].split(".")[0]

		#获取邮箱类型 126/qq/other   163
		dirStr = os.path.join(resPath,dirStrTemp)
		#获取邮箱类型对应的字符串  D:\python-project\result\163
		
		#代码无问题 调试BUG 
		if not os.path.exists(dirStr):
			#不存在 创建新目录
			os.mkdir(dirStr)
			
		
		#创建文件
		fileType = dirStrTemp
		filePath = os.path.join(dirStr,fileType + ".txt")
		with open(filePath,"a") as fw:
			lineno = str(lineNo)
			fw.write(lineno + "  " + mailStr[0] + "\n",)
			
		print(lineNo)
		lineNo += 1

		
def getAllDirRE(path, sp = ""):
    #得到当前目录下所有的文件
    filesList = os.listdir(path)
    #处理每一个文件
    sp += "   "
    for fileName in filesList:
        #判断是否是路径（用绝对路径）
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath):
            #print(sp + "目录：", fileName)
            #递归调用
            getAllDirRE(fileAbsPath, sp)
        else:work(fileAbsPath)
            #print(sp + "普通文件：", fileName)
			#处理普通文件
			

getAllDirRE(r"D:\python-project\newdir")
