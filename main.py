import gkeepapi

import time

import random

from aiogram import Bot, Dispatcher, executor, types

def GetWords():

    keep = gkeepapi.Keep()
    keep.login(login, password)

    gnote1 = keep.get('15JIVCictYkSnqWq8bIm9XgjdJSNxNZZy4st66hRKft2rh2-Eq_hkp-sA9AHe9bc')
    gnote1 = gnote1.text

    gnote2 = keep.get('1wWZ3_nGmZAiPOscMVG9C3hFrRTOjMKuLEAjxRXN0mdga03P7bpQq2ofW5ozArHg')
    gnote2 = gnote2.text

    start_time = time.time()

    result = []

    file2 = open('getRandom50IELTSWords.txt', 'w')
    for line in gnote1.splitlines():
        for r in (("👍🏻", ""), ("👍🏿", ""), ("'", "")):
            line = line.replace(*r)
        if line != '':
            result.append(line)
    for line in gnote2.splitlines():
        for r in (("👍🏻", ""), ("👍🏿", ""), ("'", "")):
            line = line.replace(*r)
        if line != '':
            result.append(line)
    
    overall = []
    s = ''
    for word in random.sample(result, 50):
        overall.append(word)
        file2.write(word + '\n')
    for l in overall:
        s += l + '\n'
    print("--- %s seconds ---" % (time.time() - start_time))
    return s

def GetGREWords():
    
    keep = gkeepapi.Keep()
    keep.login(login, password)

    gnote1 = keep.get('1zGlxXHGFXZV8dYBr5FUyBI75sCvmtGZT-g832uErJuDDX-brqbi0bvBHKw2zu3w')
    gnote1 = gnote1.text

    gnote2 = keep.get('1DcUq1J4KZhhbpJ2Px2-f3qMnhefeWZqLxSb_R5Nt1FFdFkfdc08ZOf842Gaz_38')
    gnote2 = gnote2.text

    gnote3 = keep.get('1c-1nOOOvK5ZUTdaYHy2WqSr9IwuoF0smLsIvEuMCvgtPjJMRv7PdK3t5_BswlQ')
    gnote3 = gnote3.text

    gnote4 = keep.get('1FsgZWCk1-4uLfgH6xUz-NgwnHHF1Htt5kfioFO8QBbWAn68G_1t0j3ZwBwB2KuA')
    gnote4 = gnote4.text

    gnote5 = keep.get('1abce6Vzy_6EYC5tp99-ZOmRyivmZUdHCUgfsUexx2iie92Ky8nuOf1nMLTKfWWg')
    gnote5 = gnote5.text

    start_time = time.time()

    result = []

    file2 = open('getRandom50GREWords.txt', 'w')
    for line in gnote1.splitlines():
        line = line.replace('	', ' - ')
        line = line.capitalize()
        if line != '':
            result.append(line)
    for line in gnote2.splitlines():
        line = line.replace('	', ' - ')
        line = line.capitalize()
        if line != '':
            result.append(line)
    for line in gnote3.splitlines():
        line = line.replace('	', ' - ')
        line = line.capitalize()
        if line != '':
            result.append(line)
    for line in gnote4.splitlines():
        line = line.replace('	', ' - ')
        line = line.capitalize()
        if line != '':
            result.append(line)
    for line in gnote5.splitlines():
        line = line.replace('	', ' - ')
        line = line.capitalize()
        if line != '':
            result.append(line)
    
    overall = []
    s = ''
    for word in random.sample(result, 50):
        overall.append(word)
        file2.write(word + '\n')
    for l in overall:
        s += l + '\n'
    print("--- %s seconds ---" % (time.time() - start_time))
    return s

bot = Bot(token='telegram token')
dp = Dispatcher(bot)

# Method that returns random words through telegram bot
@dp.message_handler(commands=['getwords'])
async def ieltswords(message: types.Message):
    await message.answer(text=GetWords())

# Method that returns random words through telegram bot
@dp.message_handler(commands=['getgrewords'])
async def ieltswords(message: types.Message):
    await message.answer(text=GetGREWords())

# Starting long polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
