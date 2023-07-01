with open('output.txt') as From_file:
    lines=From_file.readlines()
    for i in range(0,len(lines)):
        # 去除语句的换行符（strip()）
        lines[i]="wavs/"+"%d"%(i)+".wav|"+lines[i].strip()+'\n'
        # print(lines[i])
with open('output2.txt','w') as Out_file:
    Out_file.writelines(lines)
    print("success")