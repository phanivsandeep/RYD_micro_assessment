import PyPDF2
import re
import json
num="1234567890"
contentInPage=[]
questions=[]
option1,option2,option3,option4=[],[],[],[]
answers=[]
jsonData=[]
class exam:
    def pdfToText(self):
        pdfObject=open('The_Living_World.pdf','rb')
        reader=PyPDF2.PdfFileReader(pdfObject)
        numOfPages=reader.numPages
        for i in range(numOfPages):
            contentInPage.append(list((reader.getPage(i).extractText()).split("\n")))
        pdfObject.close()
    def clearGarbageAndSolution(self):
        for i in contentInPage:
            gv=i.index("10005 Ph.011-47623456")
            i=i[gv+1:]
            for j in i:
                if "Sol.Answer" in j:#Extracting answers here
                    for k in range(len(j)):
                        if j[k]=="(":
                            answers.append(j[k+1])
                            break
                if "[" in j:#Removing the text like aieee, aipmt etc
                    start=j.index("[")
                    end=j.index("]")+1
                    temp=j[start:end]
                    j=j.replace(temp,"")
                if "(1)" or "(2)" or "(3)" or "(4)" in j:#Extraction of options
                    if "(1)" in j and "Sol.Answer" not in j:
                        start=j.index("1")
                        end=0
                        if "(2)" in j:
                            end=j.index("2")-1
                        else:
                            end=len(j)
                        opt1=j[start:end]
                        if len(opt1)>2 and j[start+1]==")":
                            option1.append(opt1)
                    if "(2)" in j and "Sol.Answer" not in j:
                        start=j.index("2")
                        end=0
                        if "(3)" in j:
                            end=j.index("3")-1
                        else:
                            end=len(j)
                        opt2=j[start:end]
                        if len(opt2)>2 and j[start+1]==")":
                            option2.append(opt2)
                    if "(3)" in j and "Sol.Answer" not in j:
                        start=j.index("3")
                        end=0
                        if "(4)" in j:
                            end=j.index("4")-1
                        else:
                            end=len(j)
                        opt3=j[start:end]
                        if len(opt3)>2 and j[start+1]==")":
                            option3.append(opt3)
                    if "(4)" in j:
                        start=j.index("4")
                        end=0
                        if "Sol.Answer" in j:
                            end=j.index(".")-3
                        else:
                            end=len(j)
                        opt4=j[start:end]
                        if len(opt3)>2 and j[start+1]==")":
                            option4.append(opt4)
                if len(j)>1:
                    temp=re.findall("[123456789]",j)
                    for y in temp:
                        try:
                            if j[j.index(y)+1]=="." or j[j.index(y)+2]==".":
                                questions.append(j[j.index(y):])
                                break
                        except:
                            pass       
        print(len(answers),len(option1),len(option2),len(option3),len(option4),len(questions))
    def convertToJSON(self):
        numberOfQuestions=len(questions)
        for i in range(numberOfQuestions):
            temp="Question "+str(i+1)
            try:
                opt1=option1[i]
            except:
                opt1="NA"
            try:
                opt2=option2[i]
            except:
                opt2="NA"
            try:
                opt3=option3[i]
            except:
                opt3="NA"
            try:
                opt4=option4[i]
            except:
                opt4="NA"

            jsonData.append({temp:questions[i],"Option 1":opt1,"Option 2":opt2,"Option 3":opt3,"Option 4":opt4,"Answer":answers[i]})
        with open('finalData.json','w') as jsonFile:
            json.dump(jsonData,jsonFile,indent=4,ensure_ascii=False)  
      

            
    
if __name__=="__main__":
    st1=exam()
    st1.pdfToText()
    st1.clearGarbageAndSolution()
    st1.convertToJSON()
    '''file1=open("questions.txt","a")
    file1.write("\n".join(questions))
    file1.close()
    file1=open("answers.txt","a")
    file1.write("\n".join(answers))
    file1.close()
    file1=open("multiChoice.txt","a")
    file1.write("All option (1)")
    file1.write("\n".join(option1))
    file1.write("All option (2)")
    file1.write("\n".join(option2))
    file1.write("All option (3)")
    file1.write("\n".join(option3))
    file1.write("All option (4)")
    file1.write("\n".join(option4))
    file1.close()'''
    