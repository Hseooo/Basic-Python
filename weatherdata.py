# 라이브러리 및 그래프 설정
import requests # 크롤링
from bs4 import BeautifulSoup # 크롤링
import matplotlib # 그래프
import matplotlib.pyplot as plt # 그래프


matplotlib.rcParams['font.family'] = 'Malgun Gothic' # 그래프 한글 폰트 설정
matplotlib.rcParams['axes.unicode_minus'] = False # 그래프 "-" 표시 설정

#-----------------------------------------------------------------------------
# 크롤링 설정
while True:
    
    try:
    
        location = input("지역을 검색하세요 | 종료 [Enter]\n>>> ") # 지역 입력 받음
        
        if location == "": # 아무 입력 없을 시 프로그램 종료
            break
        
        Finallocation = location + '날씨' # 검색한 지역
        url = "https://search.naver.com/search.naver?query=" + Finallocation # 웹 페이지 주소 정의
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.151 Whale/3.14.134.62 Safari/537.36'}
        html = requests.get(url, headers=headers) # 웹 페이지의 HTML 코드 받기
        soup = BeautifulSoup(html.text, 'html.parser') # 문자열로 받은 값을 실제 HTML 코드로 변환

#-----------------------------------------------------------------------------
# 기본 날씨 정보 크롤링
        Detailed_Location = soup.find('h2', {'class':'title'}).text # 세부 위치
        
        NowTemp = soup.find('div', {'class':'temperature_text'}) # 현재 온도 박스
        NowTemp_text = NowTemp.find('span', {'class':'blind'}).text # "현재 온도" 텍스트
        
        Weather_Condition = soup.find('span', {'class':'weather before_slash'}) # 기상 상황
        
            
        summary_list = soup.find('dl', {'class':'summary_list'})
        
        summary_list_data1 = summary_list.findAll('dt') # 텍스트 저장
        summary_list_data2 = summary_list.findAll('dd') # 값 저장
        
        summary = soup.find('p', {'class':'summary'}).text # 어제와 비교
        
        SensoryTemp_text = summary_list_data1[0].text # 체감 온도
        SensoryTemp = summary_list_data2[0].text
        
        Humidity_text = summary_list_data1[1].text # 습도
        Humidity = summary_list_data2[1].text
        
        Wind_text = summary_list_data1[2].text # 바람
        Wind = summary_list_data2[2].text
    
#-----------------------------------------------------------------------------
# 추가 날씨 정보 크롤링
        today_chart_list = soup.find('ul', {'class':'today_chart_list'})
        
        today_chart_list_data1 = today_chart_list.findAll('strong') # 텍스트 저장
        today_chart_list_data2 = today_chart_list.findAll('span') # 값 저장
        
        fine_dust_text = today_chart_list_data1[0].text # 미세먼지
        fine_dust = today_chart_list_data2[0].text
        
        ultrafine_dust_text = today_chart_list_data1[1].text # 초미세먼지
        ultrafine_dust = today_chart_list_data2[1].text
        
        UV_rays_text = today_chart_list_data1[2].text # 자외선
        UV_rays = today_chart_list_data2[2].text
    
        Sunset_text = today_chart_list_data1[3].text # 일몰
        Sunset = today_chart_list_data2[3].text
    
#-----------------------------------------------------------------------------
# 그래프 정보 크롤링
        weather_graph_box = soup.find('div', {'class':'weather_graph_box'}) # 날씨 그래프 정보
        
        weather_graph_time = weather_graph_box.findAll('dt') # 시간 저장
        weather_graph_temp = weather_graph_box.findAll('span') # 온도 저장
        
        
        pre_graph_box = soup.find('div', {'class':'precipitation_graph_box'}) # 강수 그래프 정보
        
        pre_graph_box_time = pre_graph_box.find('div', {'class':'time_wrap'}) # 시간 정보
        pre_graph_box_mm = pre_graph_box.find('div', {'class':'graph_wrap'}) # 강수량 정보
        pre_graph_box_prob = pre_graph_box.find('div', {'class':'icon_wrap'}) # 확률 정보
        
        pre_graph_time = pre_graph_box_time.findAll('li') # 시간 저장
        pre_graph_mm = pre_graph_box_mm.findAll('li') # 강수량 저장
        pre_graph_prob = pre_graph_box_prob.findAll('em') # 확률 저장
        
        
        wind_graph_box = soup.find('div', {'class':'wind_graph_box'}) # 바람 그래프 정보
        
        wind_graph_box_time = wind_graph_box.find('div', {'class':'time_wrap'}) # 시간 정보
        wind_graph_box_speed = wind_graph_box.find('div', {'class':'graph_wrap'}) # 풍속 정보
        wind_graph_box_direction = wind_graph_box.find('div', {'class':'icon_wrap'}) # 풍향 정보
        
        wind_graph_time = wind_graph_box_time.findAll('span') # 시간 저장
        wind_graph_speed = wind_graph_box_speed.findAll('span') # 풍속 저장
        wind_graph_direction = wind_graph_box_direction.findAll('em') # 풍향 저장
        
        
        humidity_graph_box = soup.find('div', {'class':'humidity_graph_box'}) # 습도 그래프 정보
        
        humidity_graph_box_time = humidity_graph_box.find('div', {'class':'time_wrap'}) # 시간 정보
        humidity_graph_box_per = humidity_graph_box.find('div', {'class':'graph_wrap'}) # 습도 정보
        
        humidity_graph_time = humidity_graph_box_time.findAll('span') # 시간 저장
        humidity_graph_per = humidity_graph_box_per.findAll('span') # 습도 저장
    
#-----------------------------------------------------------------------------
# 날씨 정보 출력
        def weather_information():
    
            print("========================================")
            print("[",location,"]", Detailed_Location, "현재 날씨") # 지역 정보 출력
            print("========================================")
            NowTemp_C1 = NowTemp.text.strip() 
            NowTemp_C2 = NowTemp_C1[5:] # 현재 온도 값
            print(NowTemp_text, ":", NowTemp_C2) # 현재 온도 출력
            print("----------------------------------------")
            print(summary[:-5]) # 어제와 온도 비교 출력
            print(Weather_Condition.text.strip()) # 기상 상황 출력
            print(SensoryTemp_text, ":", SensoryTemp) # 체감 온도 출력
            print(Humidity_text, ":", Humidity) # 습도 출력
            print(Wind_text, ":", Wind) # 바람 출력
            print("----------------------------------------")
            print(fine_dust_text, ":", fine_dust) # 미세먼지 출력
            print(ultrafine_dust_text, ":", ultrafine_dust) # 초미세먼지 출력
            print(UV_rays_text, ":", UV_rays) # 자외선 출력
            print(Sunset_text, ":", Sunset) # 일몰 출력
            print("----------------------------------------")

#-----------------------------------------------------------------------------
# 그래프 설정
        def weather_graph(): # 날씨 그래프
        
            plt.title('날씨') # 그래프 제목
            
            x = [weather_graph_time[0].text, # X축 값 설정
                 weather_graph_time[1].text, 
                 weather_graph_time[2].text, 
                 weather_graph_time[3].text, 
                 weather_graph_time[4].text, 
                 weather_graph_time[5].text, 
                 weather_graph_time[6].text, 
                 weather_graph_time[7].text, 
                 weather_graph_time[8].text, 
                 weather_graph_time[9].text,
                 weather_graph_time[10].text,
                 weather_graph_time[11].text]
            y = [int(weather_graph_temp[1].text[:-1]), # Y축 값 설정
                 int(weather_graph_temp[4].text[:-1]), 
                 int(weather_graph_temp[7].text[:-1]), 
                 int(weather_graph_temp[10].text[:-1]), 
                 int(weather_graph_temp[13].text[:-1]), 
                 int(weather_graph_temp[16].text[:-1]), 
                 int(weather_graph_temp[19].text[:-1]), 
                 int(weather_graph_temp[22].text[:-1]), 
                 int(weather_graph_temp[25].text[:-1]), 
                 int(weather_graph_temp[28].text[:-1]),
                 int(weather_graph_temp[31].text[:-1]),
                 int(weather_graph_temp[34].text[:-1])]
            
            plt.ylim(min(y)-1, max(y)+1) # 표시 정보 위치 설정
            
            plt.plot(x, y, color = 'gray', # 그래프 설정
                     marker = 'o', markeredgecolor = 'blue', markerfacecolor = 'royalblue', 
                     label = '온도')
            
            for i in range(len(x)): # 그래프 값 표시
                height = y[i]
                plt.text(x[i], height + 0.15, y[i], ha='center')
                
            plt.xlabel('시간', loc = 'right') # X축 레이블 설정
            plt.ylabel('기온', loc = 'top') # Y축 레이블 설정
            
            plt.legend()
            plt.show() # 그래프 출력
    
    
        def pre_graph(): # 강수 그래프
            
            plt.title('강수') # 그래프 제목
            
            label = [pre_graph_time[0].text, # 레이블 설정
                     pre_graph_time[1].text, 
                     pre_graph_time[2].text, 
                     pre_graph_time[3].text, 
                     pre_graph_time[4].text, 
                     pre_graph_time[5].text, 
                     pre_graph_time[6].text, 
                     pre_graph_time[7].text, 
                     pre_graph_time[8].text, 
                     pre_graph_time[9].text, 
                     pre_graph_time[10].text, 
                     pre_graph_time[11].text]
            values = [int(pre_graph_mm[0].text.replace("~","")), # 값 설정
                      int(pre_graph_mm[1].text.replace("~","")), 
                      int(pre_graph_mm[2].text.replace("~","")), 
                      int(pre_graph_mm[3].text.replace("~","")), 
                      int(pre_graph_mm[4].text.replace("~","")), 
                      int(pre_graph_mm[5].text.replace("~","")), 
                      int(pre_graph_mm[6].text.replace("~","")), 
                      int(pre_graph_mm[7].text.replace("~","")), 
                      int(pre_graph_mm[8].text.replace("~","")), 
                      int(pre_graph_mm[9].text.replace("~","")), 
                      int(pre_graph_mm[10].text.replace("~","")), 
                      int(pre_graph_mm[11].text.replace("~",""))]
            info = [pre_graph_prob[0].text, # 표시 정보 설정
                    pre_graph_prob[1].text, 
                    pre_graph_prob[2].text, 
                    pre_graph_prob[3].text, 
                    pre_graph_prob[4].text, 
                    pre_graph_prob[5].text, 
                    pre_graph_prob[6].text, 
                    pre_graph_prob[7].text, 
                    pre_graph_prob[8].text, 
                    pre_graph_prob[9].text, 
                    pre_graph_prob[10].text, 
                    pre_graph_prob[11].text]
            
            plt.ylim(0, max(values)+1) # 표시 정보 위치 설정
                    
            plt.bar(label, values, color = 'teal')
            
            for i in range(len(label)): # 그래프 값 표시
                height = values[i]
                plt.text(label[i], height + 0.15, info[i], ha='center')
                plt.text(label[i], height + 0.05, values[i], ha='center')
        
            plt.xlabel('시간', loc = 'right')
            plt.ylabel('강수량 mm', loc = 'top')
        
            plt.show() # 그래프 출력
            
            
        def wind_graph(): # 바람 그래프
        
            plt.title('바람') # 그래프 제목
        
            label = [wind_graph_time[0].text, # 레이블 설정
                     wind_graph_time[1].text, 
                     wind_graph_time[2].text, 
                     wind_graph_time[3].text, 
                     wind_graph_time[4].text, 
                     wind_graph_time[5].text, 
                     wind_graph_time[6].text, 
                     wind_graph_time[7].text, 
                     wind_graph_time[8].text, 
                     wind_graph_time[9].text, 
                     wind_graph_time[10].text, 
                     wind_graph_time[11].text]
            values = [int(wind_graph_speed[1].text),# 값 설정
                      int(wind_graph_speed[3].text), 
                      int(wind_graph_speed[5].text), 
                      int(wind_graph_speed[7].text), 
                      int(wind_graph_speed[9].text), 
                      int(wind_graph_speed[11].text), 
                      int(wind_graph_speed[13].text), 
                      int(wind_graph_speed[15].text), 
                      int(wind_graph_speed[17].text), 
                      int(wind_graph_speed[19].text), 
                      int(wind_graph_speed[21].text), 
                      int(wind_graph_speed[23].text)]
            info = [wind_graph_direction[0].text, # 표시 정보 설정
                    wind_graph_direction[1].text, 
                    wind_graph_direction[2].text, 
                    wind_graph_direction[3].text, 
                    wind_graph_direction[4].text, 
                    wind_graph_direction[5].text, 
                    wind_graph_direction[6].text, 
                    wind_graph_direction[7].text, 
                    wind_graph_direction[8].text, 
                    wind_graph_direction[9].text, 
                    wind_graph_direction[10].text, 
                    wind_graph_direction[11].text]
            
            plt.ylim(0, max(values)+1) # 표시 정보 위치 설정
        
            plt.bar(label, values, color = 'cornflowerblue')
            
            for i in range(len(label)): # 그래프 값 표시
                height = values[i]
                plt.text(label[i], height + 0.2, info[i], ha='center')
                plt.text(label[i], height + 0.05, values[i], ha='center')
        
            plt.xlabel('시간', loc = 'right')
            plt.ylabel('풍속 m/s', loc = 'top')
        
            plt.show() # 그래프 출력
        
    
        def humidity_graph(): # 습도 그래프
        
            plt.title('습도') # 그래프 제목
        
            label = [humidity_graph_time[0].text, # 레이블 설정
                     humidity_graph_time[1].text, 
                     humidity_graph_time[2].text, 
                     humidity_graph_time[3].text, 
                     humidity_graph_time[4].text, 
                     humidity_graph_time[5].text, 
                     humidity_graph_time[6].text, 
                     humidity_graph_time[7].text, 
                     humidity_graph_time[8].text, 
                     humidity_graph_time[9].text, 
                     humidity_graph_time[10].text, 
                     humidity_graph_time[11].text]
            values = [int(humidity_graph_per[1].text), # 값 설정
                      int(humidity_graph_per[3].text), 
                      int(humidity_graph_per[5].text), 
                      int(humidity_graph_per[7].text), 
                      int(humidity_graph_per[9].text), 
                      int(humidity_graph_per[11].text), 
                      int(humidity_graph_per[13].text), 
                      int(humidity_graph_per[15].text), 
                      int(humidity_graph_per[17].text), 
                      int(humidity_graph_per[19].text), 
                      int(humidity_graph_per[21].text), 
                      int(humidity_graph_per[23].text)]
            
            plt.ylim(0, max(values)+10) # 표시 정보 위치 설정
            
            plt.bar(label, values, color = 'dodgerblue')
            
            for i in range(len(label)): # 그래프 값 표시
                height = values[i]
                plt.text(label[i], height + 1, values[i], ha='center')
        
            plt.xlabel('시간', loc = 'right')
            plt.ylabel('습도 %', loc = 'top')
        
            plt.show() # 그래프 출력
        
#-----------------------------------------------------------------------------
# 출력 값 설정
        weather_information() # 날씨 정보 출력
        
        while True:
            
            graph_order = input("그래프 선택\n| 날씨 | 강수 | 바람 | 습도 | 뒤로 가기 [Enter]\n>>>")
            if "날씨" in graph_order: # "날씨"를 입력 받을 때
                weather_graph() # 날씨 그래프 출력
            elif "강수" in graph_order: # "강수"를 입력 받을 때
                pre_graph() # 강수 그래프 출력
            elif "바람" in graph_order: # "바람"을 입력 받을 때
                wind_graph() # 바람 그래프 출력
            elif "습도" in graph_order: # "습도"를 입력 받을 때
                humidity_graph() # 습도 그래프 출력
            elif graph_order == "": # "Enter"을 입력 받을 때
                break # while 문 탈출
        
    except: # 오류 발생 시
    
        print("====================")
        print("[오류] 잘못된 입력")
        print("====================")
