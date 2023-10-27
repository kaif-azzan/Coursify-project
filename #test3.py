#f=open('data2.txt','r')
#a=f.read().split(",")
#f.close
#
#print(a[3])
#print(a[4])
import csv

#a=['hello','world','what','is','your']
#
#with open('demo.csv','w') as new_file:
#    csv_writer=csv.writer(new_file, delimiter=' ')
#    csv_writer.writerow(a)



#rows = []
#with open("demo.csv", 'r') as file:
#    csvreader = csv.reader(file)
#    for row in csvreader:
#        rows.append(row)
#
#print(rows)

#list_1 = rows[0][0].split()
#

#counter=0
#col[0]=str(col[0])
#if list_1[0] in col[0]:
#    counter+=1
#if list_1[1] in col[0]:
#    counter+=1
#if list_1[2] in col[0]:
#    counter+=1
#if list_1[3] in col[0]:
#    counter+=1
#
#percent=(counter/len(list_1))*100
#print(str(percent)+'%')



with open("demo.csv",'r') as file:
    csvreader=csv.reader(file)
    for i in csvreader:
        temp_value_for_skills=i

converted_skills_to_list=temp_value_for_skills[0].split()


col=[]
with open("sum.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        col.append(row)

final=[]

for j in range(0,len(col)):
    converted_summary_to_str=str(col[j])

    counter=0

    for i in range(0,len(converted_skills_to_list)):
        if converted_skills_to_list[i] in converted_summary_to_str:
            counter+=1
    final.append(counter)
