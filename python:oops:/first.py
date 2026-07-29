# classes practice

# class factorymumbai:
#     a = "hello"
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"your name is {self.name}")

# class factorydelhi(factorymumbai):
#     super. __init__(self,name):


# obj = factorydelhi("inderjeet")
# obj.show()

#--------------------------------------------------------------------------------------------
# inheritance 

# class animal:
#     a = "hello python user"
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"your name is {self.name} and your age is {self.age}")
# class human(animal):
#     def __init__(self,name,age):    
#         super().__init__(name)
#         self.age=age

# person1=human("inderjeet",19)
# person1.show()
# print(person1.a)

#------------------------------------------------------------------------------------------
# table 

# n = int(input("enter:"))

# for i in range(1,11):
#     print(f"{n} * {i} = {n * i}")

#--------------------------------------------------------------------------------------------
# recursive table

# def table(n,i = 1):
#     if i >= 10:
#         return
#     print(f"{n} * {i} = {n*i}")
#     table(n,i+1)
# n = int(input("enter:")) 
# res = table(n) 
# print(res)  

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

 
# multilevel inheritance

class delhi:
    def __init__(self,name,gdp,population):
        self.gdp=gdp
        self.population=population
        self.name=name
    def show(self):
        print(f"your city name {self.name} and its gdp size is {self.gdp} and its population is {self.population} with infra{self.infra} and its gdp per capita as {self.gdp_per_capita}")

class punjab(delhi):
    def __init__(self,name,gdp,population,infra):
        super().__init(name,gdp,population)
        self.infra=infra
class chennai(punjab):
    def __init__(self,name,gdp,population,infra,gdp_per_capita):
        super().__init__(name,gdp,population,infra)
        self.gdp_per_capita=gdp_per_capita

chennai1=chennai("chennai",240000000,17000000,34,30000)
chennai1.show()


