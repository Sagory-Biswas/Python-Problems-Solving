'''6. Create 3 variables to store street, city and country, now create address variable to
      store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
      Now Print the address in such a way that the street, city and country prints in a separate line'''

street = "Dhanmondi 27"
city = "Dhaka"
country = "Bangladesh"

address = street +"\n"+city+"\n"+country   #using + operator
Address = f"{street}\n{city}\n{country}"   #using f-sting

print(address)
print(Address)
print("Street:",street+"\n"+"City:",city+"\n"+"Country:",country)