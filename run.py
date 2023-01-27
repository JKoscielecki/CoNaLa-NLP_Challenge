from StackOverflow.StackOverflow import StackOverflow


with StackOverflow(teardown=True) as bot:
    df=bot.create_df()
    start_page=1
    end_page=2
    hrefs = []
    for page in range(start_page,end_page):
        bot.open_link(page)

        hrefs.append(bot.href1())
        print('Exiting ...')


    for i in bot.clean_empty_hrefs(hrefs):
        bot.open_link2(i)
        # bot.pull_title()
        question,code,answer,code_answer=bot.pull_question_answer()
        df = df.append({'question':str(question),'code':str(code),'answer':str(answer),'code_answer':str(code_answer)}, ignore_index=True)
        print(df.shape)
        print(df.head())
    print(df)