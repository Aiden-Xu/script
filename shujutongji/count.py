#关键词
key =  ["AVML","BBML","BLML","CHML","DBML","FPML","GFML","HNML","KSML","LCML","LFML","LSML","MOML","NLML","RVML","SFML","VGML","VJML","VLML","VOML","SPML"]
wenben=""
#源文件
for line in open('C:/Users/XMH/Desktop/1.txt','r', encoding='UTF-8') :
    wenben+=line

final = ""
count =0

#遍历关键词
for word in key:
    wenben2=wenben[:]
    count = 0
    while word in wenben2:
        if wenben2.find(word)!=-1:
            temp = wenben2[(wenben2.find(word) - 2)] + wenben2[wenben2.find(word) - 1]
            count += int(temp)
            wenben2=wenben2[(wenben2.find(word)+4):]
    final += word+":"+str(count)+"\n"
print(final)
#输出到桌面TXT
filename = 'C:/Users/XMH/Desktop/处理后.txt'
with open(filename,'w') as file_object:
    file_object.write(final)