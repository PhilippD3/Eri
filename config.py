import math

TOKEN = "7649297537:AAFZmshUPp8ReACZVGmguR9ig8xKZIfi0mI"

def rk2 (text):
        x =list(map(float, text.split()))
        s= sum(x)
        sr = s/len(x)
        so = 0
        N= len(x)

        for i in range(len(x)):
                so = so + (abs(sr-x[i]))**2
        sigma = math.sqrt( (so/(len(x)-1) )  ) 

        o = [0,0,0,0]


        for i in range(len(x)):
                if x[i]<(sr-sigma):
                        o[0]=o[0]+1
                if x[i]>=(sr-sigma) and x[i]<(sr):
                        o[1]=o[1]+1
                if x[i]>=(sr)and x[i]<(sr+sigma):
                        o[2]=o[2]+1
                if  x[i]>=(sr+sigma):
                        o[3] = o[3]+1

        E = [N*0.16,N*0.34,N*0.34,N*0.16]

        Xi = 0
        for i in range(4):
                Xi= Xi+ (((o[i]-E[i])**2)/E[i])
        a = [f"X_sr = {sr}",f"sigma = {sigma}", f"O1 ={o[0]},O2 ={o[1]}, O3 ={o[2]}, O4 ={o[3]},",f"Xi ={Xi}", f"Xi=<n ==>> {Xi<=4}"]
        return a

def three_sigma(text):
    a = []
    nums = list(map(float, text.split()))
    while True:
        
        x_avg = sum(nums) / len(nums)
        

        # Находим выброс
        maxi = 0
        hui = abs(nums[0] - x_avg)
        for i in range(len(nums)):
            if abs(nums[i] - x_avg) > hui:
                maxi = i
                hui = abs(nums[i] - x_avg)
        a.append(f"X_avg до: {x_avg}")
        # Пересчитываем среднее без выброса
        
        x_avg = 0
        for i in range(len(nums)):
            if i == maxi:
                continue
            x_avg = x_avg + nums[i]
    
        x_avg = x_avg/ (len(nums)-1)
        a.append(f"X_avg без {nums[maxi]}: {x_avg}")

        sumi = 0
        for i in range(len(nums)):
            if i == maxi:
                continue
            sumi = sumi + ((nums[i] - x_avg) * (nums[i] - x_avg))
        # Вычисляем стандартное отклонение

        sigma = math.sqrt((sumi) / (len(nums) - 2))
        a.append(f"sigma = {sigma}")
        a.append(f"{x_avg} +- {3 * sigma}")

        # Проверка на выброс
        if abs(nums[maxi] - x_avg) > 3 * sigma:
            a.append(f"{nums[maxi]}   Выброс\n\n")
            nums.pop(maxi) # Удаляем выброс из списка
            continue
        else:
            a.append(f"{nums[maxi]} Не выброс\n\n")
            x_avg = sum(nums) / len(nums)
            a.append(f"X_avg конечная = {x_avg}")
            sumi = sum([abs(num - x_avg)*2 for num in nums])
            sigma = math.sqrt(sumi / (len(nums) - 1))
            a.append(f"sigma конечная = {sigma}")
            a.append(f"Ответ для первого: {x_avg} +- {3 * sigma}")
            break
        print("hui")
    return a

        
