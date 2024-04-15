import PyPDF2

path = []
count = 0

print("Enter the paths for as many pdfs you would like me to merge: ")
path.append(input(f"\nEnter path for pdf{count+1} here :"))
path.append(input(f"\nEnter path for pdf{count+2} here :"))
count += 2
while count>=2:
        
        oneMore = input("\nAny other Pdf you would like me to merge...if so enter yes / if not enter no: ")
        
        if oneMore == "yes" or oneMore == "no":
           
            if oneMore == "yes":
                count+=1
                path.append(input(f"\nEnter path for pdf{count} here :"))
                
            else:
                break

        else:
            print("\nPlease comply by the procedure provided ")    


docFiles = []
for doc in path:
    avoidEscape_ch = "r{doc}"
    docFiles.append(doc)

merger = PyPDF2.PdfMerger()

for filename in docFiles:
    fp = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(fp)
    merger.append(pdfReader)

fp.close()

docName = input("How would you like to save your merged document: ")
any_otherExtentn = input("Would you like any other format for your merged document other than pdf...if so enter yes / if not enter no: ")

if any_otherExtentn == "yes" or any_otherExtentn == "no":
        
        if any_otherExtentn == "yes":
            
            extention = input("Please enter the format for your merged document : ")
            merger.write(f"{docName}.{extention}")
            merger.write(f"{docName}.pdf")

        else:
            merger.write(f"{docName}.pdf")
else:
            print("You should have complied by the procedure provided...by default settings my master programmed in me...I am giving you merged Document in PDF format ")    
            merger.write(f"{docName}.pdf")
            


