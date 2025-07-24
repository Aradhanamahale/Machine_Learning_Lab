#!/usr/bin/env python
# coding: utf-8

# In[8]:


print("---calculator---")
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Seecond Number: "))

print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
choice =int(input("Enter your choice: "))

while True:
    if choice == 1:
        print("Addition is: ",num1 + num2)
    elif choice == 2:
        print("Substraction is: ",num1 - num2)
    elif choice == 3:
        print("Multiplication is:",num1 * num2)
    elif choice == 4:
        if num2 != 0:
            print("Division is: ",num1 / num2)
        else:
            print("Error")
    else:
        print("Invalid choice")
    
    ch =int(input("Do you Want to Continue? (Yes(1) or No(0)): "))
    if ch != 1:
        print("Stop")
        break
        


# In[7]:


import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [2,4,8,10]

plt.plot(x,y)
plt.show()



# In[11]:


import matplotlib.pyplot as plt
a = [1,2,3,4]
b = [11,23,17,12]
c = [3,4,5,6]
plt.plot(a,b,c)
plt.show()


# In[20]:


import matplotlib.pyplot as plt
x = [11,22,33]
y = [1,2,3]
z = [10,20,30]
q = [2,3,4]

plt.plot(x,y,z,q)
plt.title("My Plotting Graph")
plt.show()


# In[21]:


print("TY B Aradhana Mahale")


# In[22]:


import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C', 'Category D']
values = [23, 45, 56, 78]
plt.bar(categories, values, color='skyblue')

plt.title('Sample Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()


# In[ ]:


import matplotlib.pyplot

