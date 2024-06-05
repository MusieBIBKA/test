import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time


def get_text(el) -> str:
    if not el:
        return "Отсутствует"

    return el.get_text(strip=True)
def fetch_news(url):
    time.sleep(150)  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
     
    
    news_items = soup.find_all('article', class_='uho rubric_lenta__item js-article')
    
    for item in news_items:
    
        timestr = item.find('p', class_='uho__tag rubric_lenta__item_tag hide_desktop').text.strip()
        times = datetime.strptime(timestr, '%d.%m.%Y, %H:%M')
        if times > datetime.now()-timedelta(minutes=3)+timedelta(hours=3):
            if 'Украин' in item.text or 'США' in item.text:
                heading = item.find('span', class_='vam').text.strip()
                argument = get_text(item.find(
                    'h3',
                    class_='uho__subtitle rubric_lenta__item_subtitle'))
                source = item.find('ul', class_='crumbs tag_list').text.strip()
                
                print(f'Новость: {heading}')
                print(f'Анотация: {argument}')
                print(f'Тэг: {source}')
                print("-" * 50)
            else: 
                    print("-" )
                    print("-" )
                    print("-" )
                
        
def run_script(duration_hours):
    end_time = datetime.now() + timedelta(hours=duration_hours)
    print(
        f'Время работы программы {duration_hours} часа.'
    )

    while datetime.now() < end_time:
        
        url = 'https://www.kommersant.ru/lenta?ysclid=lwxx2s7elm606723236'
        fetch_news(url)


run_script(4)