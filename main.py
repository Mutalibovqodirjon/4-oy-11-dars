# 1 misol
import asyncio
async def  paroldeleter(a:str):
    i=0
    new_passsworsd =""
    while len(a)>i:
        if not a[i].isdigit():
            new_passsworsd += a[i]
        i+=1
    print(f"Yangilangan parol{new_passsworsd}")
f="parol123"
async def main():
    await asyncio.gather(paroldeleter(f))

asyncio.run(main())

#2 misol
async def parol(a:str):
    b=""
    i=0
    if len(a) > 10:
        while 10 > i:
            b+=a[i]
            i += 1
    print(b)
f="Hello world "
async def main():
    await asyncio.gather(parol(f))

asyncio.run(main())


# 3 misol
async def raqam_del(a:str):
    i=0
    yangi_ism =""
    while len(a)>i:
        if not a[i].isdigit():
            yangi_ism += a[i]
        i+=1
    print(yangi_ism)
f="Qodirjon124"
async def main():
    await asyncio.gather(raqam_del(f))

asyncio.run(main())
#

# 4 misol
async  def text(a:str):
    i = 0
    y = " "
    while len(a)>i:
        if a[i] != " ":
            y+=a[i].lower()
        i+=1
    print(y)
f = "Heell o W orld"
async def main():
    await asyncio.gather(text(f))

asyncio.run(main())


# 5 misol
async def text(a: str):
    y = ""
    i = 0
    b = "aeiouAEIOU"
    while i < len(a):
        if a[i] in b:
            y += a[i]
        i += 1
    print(y)

f = "Salom dunyo"
async def main():
    await asyncio.gather(text(f))
asyncio.run(main())


#6 misol
async def text(a:str):
    y = ""
    i = 0
    while i < len(a):
        if i < len(a) - 1 and a[i] == 'a' and a[i + 1] == 'b':
            y += "#"
            i += 2
        else:
            y += a[i]
        i +=1
    print(y)


f = "abdfds ab sdfjs"
async def main():
    await asyncio.gather(text(f))
asyncio.run(main())


# 7 misol
async def  text(a:str):
    i=0
    y =""
    while len(a)>i:
        if a[i].isdigit():
            y += a[i]
        i+=1
    print(y[::-1])
f="123456789"
async def main():
    await asyncio.gather(text(f))

asyncio.run(main())


#  8 misol
async def text(a: str):
    i = 0
    y = ""
    v = len(a) // 2
    while i < len(a):
        if i != v:
            y += a[i]
        i += 1
    print(y)
f = "salodunyo"
async def main():
    await asyncio.gather(text(f))

asyncio.run(main())


#  9 misol
async def  text(a:str):
    i=0
    y =""
    while len(a)>i:
        y += a[i]
        i+=1
    if  y.endswith("a"):
        y=y.lower()
    print(y)


f="Alina"
async def main():
    await asyncio.gather(text(f))
asyncio.run(main())
#
# 10 misol
async def text(a):
    i = 0
    y = ""
    l = []
    while i < len(a):
        if a[i] not in l:
            y += a[i]
            l.append(a[i])
        i += 1
    print(l)

f = "Hello World"
async def main():
    await asyncio.gather(text(f))
asyncio.run(main())

#  11 misol
async def text(a):
    u = "aeiouAEIOU"

    if all(i in u for i in a):
        print(a.upper())
    else:
        print("So'z faqat unli harflardan iborat emas.")
f = input("So'zni kiriting: ")
async def main():
    await asyncio.gather(text(f))
asyncio.run(main())

# 12 misol
import aiohttp
async def current_weather(city_name):
    parameters = {
        "q": city_name,
        "appid": 'd774a8d22a0680891844b5289eda4be6',
        "units": 'metric'
    }
    url = 'https://api.openweathermap.org/data/2.5/weather'

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=parameters) as response:
            if response.status == 200:
                data = await response.json()
                temp = data['main']['temp']
                description = data['weather'][0]['description']
                wind = data['wind']['speed']
                info = (
                    f"{city_name.title()} da havo harorati {round(temp)}°C.\n"
                    f"Shamol {wind} m/s. Havo: {description}."
                )
                print(info)
            else:
                print("Xatolik: Shahar nomi noto'g'ri yoki API xizmatida muammo bor.")

city = input("Shahar nomini kiriting: ")
async def main():
    await current_weather(city)
asyncio.run(main())

