class Person:
    #Method init é usado para inicializar objetos de uma classe. Ele é tambem chamado de constructor. 
    def __init__(self, name, age=None): #O "=" define um valor padrão para o parâmetro, permitindo que ele seja opcional na chamada do construtor
        self.name = name
        self.age = age
        
    def say_hi(self):
        print('Hello, my name is', self.name)

p1 = Person("John", 42)
print(p1.name)
print(p1.age)
print(f"Hi, my name is {p1.name}, and I have {p1.age} years")

p = Person("José")
p.say_hi()


#Constructor são feitos para inicializar (atribuir valores) aos membros de dados da classe quando um objeto da classe é criada. Como methods, um constructor tambme contem uma coleção de statements (instructions) que são executadas no tempo de criação do objeto.  


#Attention to Inheritance