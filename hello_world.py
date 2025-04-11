print("Hello World");
fruit = ["apple", "orange", "banana", "mango", "strawbery", "peaches"];
x = "This apple is tasty";
print(fruit[2:4]);
print(x[2:8]);

score = {
    "John": 95,
    "Rita": 90,
    "Sam": 85,  
}
print("John's score is", score["John"]);

car = ["toyota", "ford", "tesla", "truck", "mercedes"];
for x in car:
    if x == "tesla":
        print("I wish to own tesla one day");
    elif x == "truck":
        print("But trucks are the best for work");
        
    else:
        print("I like", x, "too");

print("LESSON 2.6")        
username = "John123"
def validate_username(uname) :
    if uname == "John123":
        print("Hello John")
    else:
        print("Wrong username")
        
validate_username(username)

