import StackOverflow.constants as const
from selenium import webdriver
import pandas as pd

class StackOverflow(webdriver.Chrome):

    def __init__(self, driver_path=r"C:\SeleniumDrivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        super(StackOverflow, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def open_link(self, page):
        self.get('https://stackoverflow.com/questions/tagged/python?tab=votes&page={}&pagesize=15'.format(page))


    def href1(self):
        lnks = self.find_elements_by_css_selector('a[href^="/questions/"][class="s-link"]')
        hrefs = [a.get_attribute("href") for a in lnks]
        # for lnk in [a.get_attribute("href") for a in lnks]:
        #     # get_attribute() to get all href
        #     print(lnk)
        print(hrefs)
        return hrefs
    def clean_empty_hrefs(self, hrefs):
       # remove all empty lists
        list_hrefs=[]
        for i in hrefs:
            if i!=[]:
                list_hrefs.append(i)
        # merge all elemenets in one list
        herfs_list=[]
        for i in list_hrefs:
            for j in i:
                herfs_list.append(j)
        print(herfs_list)
        return herfs_list


    def open_link2(self,link):
        self.get(link)

    def pull_title(self):
        title=self.find_element_by_class_name(
            'question-hyperlink'
        ).get_attribute('innerHTML').strip()
        return title
    def pull_question_answer(self):
        # p=self.find_element_by_css_selector(
        #     '[itemprop=text]'
        # ).get_attribute('innerHTML').strip()
        # print(p)

        # snippet=self.find_elements_by_xpath('//*[@id="question"]/div[2]/div[2]/div[1]/p')
        # code = self.find_elements_by_css_selector('[class="hljs-keyword"]')
        # for c in code:
        #     c=c.get_attribute('innerHTML').strip()
        #     print(c)

        # for i in snippet:
        #     i=i.get_attribute('innerHTML').strip()
        #     print(i)
        # for c in code:
        #     c=c.get_attribute('innerHTML').strip()
        #     print(c)
        # //*[@id="question"]/div[2]/div[2]/div[1]
        # //*[@id="question"]/div[2]/div[2]/div[1]/pre[2]/code/span[1]
        question_element = self.find_element_by_css_selector('[itemprop="text"]')
        question = question_element.text

        code_elements = question_element.find_elements_by_tag_name("code")
        code = [code_element.text for code_element in code_elements]

        answer_elements = self.find_elements_by_css_selector("[itemprop='text']")
        answer = [answer_element.text for answer_element in answer_elements][1]

        code_elements_answer = answer_elements[1].find_elements_by_tag_name("code")
        code_answer = [code_elements_answer.text for code_elements_answer in code_elements_answer]

        # print(question)
        # print(code)
        # # print(answer)
        # print(code_answer)
        return question,code,answer,code_answer
        # def pull_answer_text(self):
        #     answer_element = self.find_element_by_css_selector('[itemprop="text"]')
        #     text = question_element.text
        #
        #     code_elements = question_element.find_elements_by_tag_name("code")
        #     code = [code_element.text for code_element in code_elements]
        #
        #     print(text)
        #     print(code)

    def create_df(self):
        df = pd.DataFrame({'Question': pd.Series(dtype='str'),
                           'Question_Code': pd.Series(dtype='str'),
                           'Answer': pd.Series(dtype='str'),
                           'Answer_code': pd.Series(dtype='str')})
        return df
