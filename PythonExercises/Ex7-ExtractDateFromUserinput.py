

#Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
#exam_st_date = (11, 12, 2014)
#Sample Output : The examination will start from : 11 / 12 / 2014

examStartDate: str = input("Enter the exam start date: ")
examStartDate = examStartDate.replace("(","")
examStartDate = examStartDate.replace(")","")
examStartDate = examStartDate.split(",")

examMonth   = examStartDate[0]
examDate    = examStartDate[1]
examyear    = examStartDate[2]

print("The exam date is: " + examMonth + "/" + examDate + "/" + examyear)



## Comment: I am sure there is a better and more optimized way of solving this.