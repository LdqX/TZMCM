import pandas as pd
data=pd.read_excel(r"C:/Users/Administrator/Desktop/Data/new.xlsx")
aloneRate_data=pd.read_csv(r"C:/Users/Administrator/Desktop/Data/alone/aloneRate.csv")
keepRate_data=pd.read_csv(r"C:/Users/Administrator/Desktop/Data/alone/dependRate.csv")

test_data=pd.read_excel(r"C:/Users/Administrator/Desktop/Data/test.xlsx")

str1=r"保单号	起保日期	终止日期	渠道	品牌	车系	保单性质	续保年	投保类别	是否本省车牌	使用性质	车辆种类	车辆用途	新车购置价	车龄	险种	NCD	风险类别（A最低，E最高）	客户类别	被保险人性别	被保险人年龄	是否投保车损	是否投保盗抢	是否投保车上人员	三者险保额	签单保费	立案件数	已决赔款	是否续保"
str2=r"C:/Users/Administrator/Desktop/Data/depend/"
a=str1.split("\t")
dependRateY_data=[] # a list of dataframe, which including the name and rate
dependRateN_data=[]
for i in range(27):
    #i :0~26
    strTemp=a[(i+1)%28]
    strEndN=str2+strTemp+r"N.csv"
    strEndY=str2+strTemp+r"Y.csv"
    #no column named 订单号
    #len : 0~26
    dependRateY_data.append(pd.read_csv(strEndY,encoding='UTF-8',engine='python',names=["续保"+strTemp+"概率"]))
    dependRateN_data.append(pd.read_csv(strEndN,encoding='UTF-8',engine='python',names=["不续保"+strTemp+"概率"]))
    
    #delete!!!!!!!!!!!
    #if i>3: break
#print(dependRateN_data[i+1:][:i+1][0]['概率'][value])
count=0
for row,index in test_data.iterrows():
    # for every row
    # it doesn't matter for multiply million
    YRate=1000000000
    NRate=1000000000
    
    sResult=" "
    for i in range(27): 
        # i:列数 0~27 ， 比较的因素数目 , 0是起保日期
        curColumn=a[i+1]  #the column in waiting ,1~28
        curSecondColumnY="续保"+curColumn+"概率"
        curSecondColumnN="不续保"+curColumn+"概率"
        #概率表格
        dFY=dependRateY_data[i:][:i+1][0]
        dFN=dependRateN_data[i:][:i+1][0]
        #待查键
        testValue=str(index[curColumn])
        
        #print(curColumn)
        #print(testValue,i)
        #print(i)
        #print(dFY)
        #print(len(dFY))
        print("---")
        #print(dFN)
        #print(len(dFN))
        
        #初始时间
        if i==0:
            testValue=testValue[0:4]
            if testValue=='2018' :
                YRate=YRate*float(dFY[curSecondColumnY][1])
                NRate=NRate*float(dFN[curSecondColumnN][1])
            elif testValue=='2017' :
                YRate=YRate*float(dFY[curSecondColumnY][2])
                NRate=NRate*float(dFN[curSecondColumnN][2])
            else :
                YRate=YRate*float(dFY[curSecondColumnY][3])
                NRate=NRate*float(dFN[curSecondColumnN][3])
        elif i==1:continue
               
        #新车购置价
        elif i==12:
            tempValue=int(testValue)
            if tempValue>300000:
                YRate=YRate*float(dFY[curSecondColumnY][1])
                NRate=NRate*float(dFN[curSecondColumnN][1])
            elif tempValue<50000 :
                YRate=YRate*float(dFY[curSecondColumnY][2])
                NRate=NRate*float(dFN[curSecondColumnN][2])
            elif tempValue>= 50000 and tempValue<70000:
                YRate=YRate*float(dFY[curSecondColumnY][4])
                NRate=NRate*float(dFN[curSecondColumnN][4])
            elif tempValue>= 70000 and tempValue<100000:
                YRate=YRate*float(dFY[curSecondColumnY][3])
                NRate=NRate*float(dFN[curSecondColumnN][3])
            elif tempValue>= 100000 and tempValue<150000:
                YRate=YRate*float(dFY[curSecondColumnY][7])
                NRate=NRate*float(dFN[curSecondColumnN][7])
            elif tempValue>= 150000 and tempValue<200000:
                YRate=YRate*float(dFY[curSecondColumnY][6])
                NRate=NRate*float(dFN[curSecondColumnN][6])
            elif tempValue>= 200000 and tempValue<300000:
                YRate=YRate*float(dFY[curSecondColumnY][5])
                NRate=NRate*float(dFN[curSecondColumnN][5])
            else :
                print("新车购置价为空")
                
         #被保险人年龄
        elif i==19:
            tempValue=float(testValue)
            if tempValue>50:
                YRate=YRate*float(dFY[curSecondColumnY][7])
                NRate=NRate*float(dFN[curSecondColumnN][7])
            elif tempValue<25:
                YRate=YRate*float(dFY[curSecondColumnY][1])
                NRate=NRate*float(dFN[curSecondColumnN][1])
            elif tempValue>= 25 and tempValue<30:
                YRate=YRate*float(dFY[curSecondColumnY][2])
                NRate=NRate*float(dFN[curSecondColumnN][2])
            elif tempValue>= 30 and tempValue<35:
                YRate=YRate*float(dFY[curSecondColumnY][3])
                NRate=NRate*float(dFN[curSecondColumnN][3])
            elif tempValue>= 35 and tempValue<40:
                YRate=YRate*float(dFY[curSecondColumnY][4])
                NRate=NRate*float(dFN[curSecondColumnN][4])
            elif tempValue>= 40 and tempValue<45:
                YRate=YRate*float(dFY[curSecondColumnY][5])
                NRate=NRate*float(dFN[curSecondColumnN][5])
            elif tempValue>= 45 and tempValue<50:
                YRate=YRate*float(dFY[curSecondColumnY][6])
                NRate=NRate*float(dFN[curSecondColumnN][6])
            else :
                print("被保险人年龄为空")
                
        #三者险保额
        elif i==23:
            tempValue=float(testValue)
            if tempValue>800000:
                YRate=YRate*float(dFY[curSecondColumnY][2])
                NRate=NRate*float(dFN[curSecondColumnN][2])
            elif tempValue<200000:
                YRate=YRate*float(dFY[curSecondColumnY][1])
                NRate=NRate*float(dFN[curSecondColumnN][1])
            elif tempValue>= 200000 and tempValue<400000:
                YRate=YRate*float(dFY[curSecondColumnY][4])
                NRate=NRate*float(dFN[curSecondColumnN][4])
            elif tempValue>= 400000 and tempValue<600000:
                YRate=YRate*float(dFY[curSecondColumnY][3])
                NRate=NRate*float(dFN[curSecondColumnN][3])
            elif tempValue>= 600000 and tempValue<800000:
                YRate=YRate*float(dFY[curSecondColumnY][5])
                NRate=NRate*float(dFN[curSecondColumnN][5])
            else :
                print("三者险保额为空") 
                
        #签单保费或已决赔款
        elif i==24 or i==26:
            tempValue=float(testValue)
            if tempValue>4000:
                YRate=YRate*float(dFY[curSecondColumnY][2])
                NRate=NRate*float(dFN[curSecondColumnN][2])
            elif tempValue<600:
                YRate=YRate*float(dFY[curSecondColumnY][1])
                NRate=NRate*float(dFN[curSecondColumnN][1])
            elif tempValue>= 600 and tempValue<700:
                YRate=YRate*float(dFY[curSecondColumnY][7])
                NRate=NRate*float(dFN[curSecondColumnN][7])
            elif tempValue>= 700 and tempValue<800:
                YRate=YRate*float(dFY[curSecondColumnY][6])
                NRate=NRate*float(dFN[curSecondColumnN][6])
            elif tempValue>= 800 and tempValue<850:
                YRate=YRate*float(dFY[curSecondColumnY][5])
                NRate=NRate*float(dFN[curSecondColumnN][5])
            elif tempValue>= 850 and tempValue<900:
                YRate=YRate*float(dFY[curSecondColumnY][4])
                NRate=NRate*float(dFN[curSecondColumnN][4])
            elif tempValue>= 900 and tempValue<1000:
                YRate=YRate*float(dFY[curSecondColumnY][3])
                NRate=NRate*float(dFN[curSecondColumnN][3])
            elif tempValue>= 1000 and tempValue<2000:
                YRate=YRate*float(dFY[curSecondColumnY][10])
                NRate=NRate*float(dFN[curSecondColumnN][10])
            elif tempValue>= 2000 and tempValue<3000:
                YRate=YRate*float(dFY[curSecondColumnY][9])
                NRate=NRate*float(dFN[curSecondColumnN][9])
            elif tempValue>= 3000 and tempValue<4000:
                YRate=YRate*float(dFY[curSecondColumnY][8])
                NRate=NRate*float(dFN[curSecondColumnN][8])
            else :
                print(curColumn+"为空") 
                if curColumn=="已决赔款":
                    YRate=YRate*float(dFY[curSecondColumnY][11])
                    NRate=NRate*float(dFN[curSecondColumnN][11])
        else:
            try:
                YRate=YRate*float(dFY[curSecondColumnY][testValue])
                NRate=NRate*float(dFN[curSecondColumnN][testValue])
                
            except KeyError:
                try:
                    YRate=YRate*float(dFY[curSecondColumnY]['空'])
                    NRate=NRate*float(dFN[curSecondColumnN]["空"])
                except KeyError:
                    continue
            else :continue
                
                
        print("YRate=",YRate,"\tNRate=",NRate,"\n")
    if YRate>NRate:sResult='是'
    else :sResult='否' 
    if sResult==index[a[28]]: count=count+1
    #Delete!!!!!!!!!!!
    
    
    print(row)
    print("\n") 


print("成功次数:",count,"\n验证成功率：\n",count/65535.0,end=" ")
print("%")        
