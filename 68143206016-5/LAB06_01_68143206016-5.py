import random
random_number = random.randint(1,100)
while True:
    answer = int(input("กรุณากรอกเลขที่ต้องการทาย : "))
    if answer >= 0 and answer <=100:
        
        if answer > random_number:
            number = print("มากเกินไป (Too high!)")
            continue
        elif answer < random_number:
            number = print("น้อยเกินไป (Too Low!)")
            continue
        else:
            answer = random_number
            print(f"ยินดีด้วย! คุณทายเลขถูกต้อง คือ : {answer}")
        break
    else:
        print(f"Error'{answer}' กรุณากรอกตัวเลขให้อยู่ในช่วง 1-100 ")