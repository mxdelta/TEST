col_ticket=int(input("Сколько билетов хотите приобрести?: "))
sum_cost=0
for _ in range(col_ticket):
    age=int(input(f"Введите возраст {_ + 1}-го участника "))
    if age<18:
        t_cost=0
       
    if age>=18 and age <= 25:
        t_cost=990
    if age>25:
        t_cost=1390
              
    sum_cost=sum_cost+t_cost
    
if col_ticket>=3: 
    sum_cost=sum_cost-sum_cost*.1
    print("Общая стоимость со скидкой: ", sum_cost)
else:
    print("Общая стоимость (скидка не распространяется): ", sum_cost)
  
---------------------------------------------------------------------------------------
''' ИЛИ тАК
def calculate_price(age):
    if age < 18:
        return 0
    elif 18 <= age <= 25:
        return 990
    else:
        return 1390

def main():
    n = int(input("Сколько билетов хотите приобрести? "))
    total_cost = 0
    for _ in range(n):
        age = int(input(f"Введите возраст {_ + 1}-го участника "))
        cost = calculate_price(age)
        total_cost += cost if n > 3 else cost * 0.9
    print("Общая стоимость:", total_cost)

if __name__ == "__main__":
    main()
'''
