per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму для вложения: "))
deposit = []

# Преобразование словаря в список
for bank in per_cent:
    deposit.append(int(money*(per_cent[bank])))
    
print("Преобразование словаря в список: ",deposit)

# Максимальная сумма, которую вы можете заработать
max_value = max(deposit)
print("Максимальная сумма, которую вы можете заработать: ", max_value)

# Расчет максимальной суммы вариант 2
max_percent = max(per_cent, key=per_cent.get)
print("max процент в банке ", max_percent, " и составляет", per_cent[max_percent], "в итоге сумма за год составит", per_cent[max_percent]*money)  
