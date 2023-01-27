import pandas as pd
from openpyxl.workbook import Workbook
from StackOverflow.StackOverflow import StackOverflow


with StackOverflow(teardown=True) as bot:
    df=pd.DataFrame()
    start_page=25
    end_page=100
    hrefs = []
    for page in range(start_page,end_page):
        bot.open_link(page)
        hrefs.append(bot.href1( ))
        print('Exiting ...')


    for i in bot.clean_empty_hrefs(hrefs):
        bot.open_link2(i)
        title = bot.pull_title()
        question,code,answer,code_answer=bot.pull_question_answer()
        df = df.append({'title':str(title),'question':str(question),'code':str(code),'answer':str(answer),'code_answer':str(code_answer)}, ignore_index=True)
        # print(df.head())
    df.to_excel('extract/dump2.xlsx')
