from urllib.parse import *
from urllib.request import *
from tkinter import *
from tkinter import font
from tkinter import ttk
from operator import itemgetter
from xml.dom.minidom import parseString
import spam
g_Tk = Tk()
g_Tk.title("고속도로 주유소 정보 조회")
g_Tk.geometry("530x700")
DataList = []
ClickStr = ""

def InitTopText():
    TempFont = font.Font(g_Tk, size = 18, weight='bold', family='Consolas')
    MainText = Label(g_Tk, font = TempFont, text = "[고속도로 주유소 정보 조회]")
    MainText.place(x=80)

def InitRouteBox():
    global RouteBox,routeIndex,str2


    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.place(x=210, y=120)
    # str2 = StringVar()

    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    RouteBox = Listbox(g_Tk, font=TempFont, activestyle='none', width=15, height=5, borderwidth=7, relief='ridge', \
                       yscrollcommand=ListBoxScrollbar.set)
    RouteBox.insert(1, "88올림픽고속도로")
    RouteBox.insert(2, "경부고속도로")
    RouteBox.insert(3, "고창담양고속도로")
    RouteBox.insert(4, "남해고속도로")
    RouteBox.insert(5, "당진대전고속도로")
    RouteBox.insert(6, "대구부산고속도로")
    RouteBox.insert(7, "대구포항고속도로")
    RouteBox.insert(8, "동해고속도로")
    RouteBox.insert(9, "무안광주고속도로")
    RouteBox.insert(10, "부산울산고속도로")
    RouteBox.insert(11, "서울양양고속도로")
    RouteBox.insert(12, "서해안고속도로")
    RouteBox.insert(13, "순천완주고속도로")
    RouteBox.insert(14, "영동고속도로")
    RouteBox.insert(15, "울산고속도로")
    RouteBox.insert(16, "익산장수고속도로")
    RouteBox.insert(17, "중부고속도로(하남-통영)")
    RouteBox.insert(18, "중부내륙고속도로")
    RouteBox.insert(19, "중앙고속도로")
    RouteBox.insert(20, "천안논산고속도로")
    RouteBox.insert(21, "청원상주고속도로")
    RouteBox.insert(22, "평택시흥고속도로")
    RouteBox.insert(23, "평택제천고속도로")
    RouteBox.insert(24, "평택화성고속도로")
    RouteBox.insert(25, "호남고속도로")
    RouteBox.insert(26, "경인선")
    RouteBox.insert(27, "남해제1지선")
    RouteBox.insert(28, "남해제2지선")
    RouteBox.insert(29, "대전남부순환선")
    RouteBox.insert(30, "봉담동탄선")
    RouteBox.insert(31, "서울외곽순환선")
    RouteBox.insert(32, "서천공주선")
    RouteBox.insert(33, "용인서울선")
    RouteBox.insert(34, "인천국제공항선")
    RouteBox.insert(35, "인천대교선")
    RouteBox.insert(36, "제2경인선")
    RouteBox.insert(37, "제3경인선")
    RouteBox.insert(38, "중부내륙지선")
    RouteBox.insert(39, "호남선지선")

    RouteBox.pack()
    RouteBox.place(x=25, y=80)
    ListBoxScrollbar.config(command=RouteBox.yview)

    b = Button(text="->", command=Button_Click)
    b.place(x=220,y=50)

def Button_Click():
    global r, str
    r = RouteBox.curselection()
    InitDirec()

def InitDirec():
    global RouteBox,str,r,ClickStr
    str = StringVar()
    ClickStr=""

    routeIndex = RouteBox.curselection()
    direction = ttk.Combobox(textvariable=str, width=20)
    if 0 in routeIndex:
        direction['value'] = ('광주','대구')
    elif 1 in routeIndex:
        direction['value'] = ('부산', '서울')
        ClickStr = "경부선"
    elif 2 in routeIndex:
        direction['value'] = ('고창', '담양')
    elif 3 in routeIndex:
        direction['value'] = ('순천', '부산')
        ClickStr = "남해선"
    elif 4 in routeIndex:
        direction['value'] = ('당진', '유성')
    elif 5 in routeIndex :
        direction['value'] = ('부산', '대구')
    elif 6 in routeIndex :
        direction['value'] = ('대구', '포항')
    elif 7 in routeIndex :
        direction['value'] = ('동해', '속초')
        ClickStr = "동해ㆍ울산포항선"
    elif 8 in routeIndex :
        direction['value'] = ('무안', '광주')
        ClickStr = "무안광주ㆍ광주대구선"
    elif 9 in routeIndex :
        direction['value'] = ('부산', '울산')
    elif 10 in routeIndex :
        direction['value'] = ('서울','양양')
        ClickStr = "서울양양선"
    elif 11 in routeIndex :
        direction['value'] = ('목포', '서울')
        ClickStr="서해안선"
    elif 12 in routeIndex :
        direction['value'] = ('광양', '전주')
        ClickStr="순천완주선"
    elif 13 in routeIndex :
        direction['value'] = ('인천', '강릉')
        ClickStr="영동선"
    elif 14 in routeIndex :
        direction['value'] = ('언양', '울산')
    elif 15 in routeIndex :
        direction['value'] = ('익산', '장수')
    elif 16 in routeIndex:
        direction['value'] = ('통영', '하남')
        ClickStr="통영대전ㆍ중부선"
    elif 17 in routeIndex :
        direction['value'] = ('마산','양평')
        ClickStr="중부내륙선"
    elif 18 in routeIndex :
        direction['value'] = ('부산', '춘천')
        ClickStr="중앙선"
    elif 19 in routeIndex :
        direction['value'] = ('논산', '천안')
    elif 20 in routeIndex :
        direction['value'] = ('청원', '상주')
        ClickStr="당진영덕선"
    elif 21 in routeIndex :
        direction['value'] = ('서평택', '군자')
    elif 22 in routeIndex :
        direction['value'] = ('평택', '제천')
        ClickStr="평택제천선"
    elif 23 in routeIndex :
        direction['value'] = ('오성', '안녕')
    elif 24 in routeIndex :
        direction['value'] = ('순천', '논산')
        ClickStr="호남선"
    elif 25 in routeIndex :
        direction['value'] = ('인천', '서울')

    elif 26 in routeIndex :
        direction['value'] = ('산인', '창원')
    elif 27 in routeIndex :
        direction['value'] = ('냉정', '부산')
        ClickStr="남해제2지선"
    elif 28 in routeIndex :
        direction['value'] = ('서대전', '비룡')
    elif 29 in routeIndex :
        direction['value'] = ('동탄', '봉담')
    elif 30 in routeIndex :
        direction['value'] = ('판교-일산', '판교-구리')
    elif 31 in routeIndex :
        direction['value'] = ('서천', '공주')
        ClickStr="서천공주선"
    elif 32 in routeIndex :
        direction['value'] = ('흥덕', '헌릉')
    elif 33 in routeIndex :
        direction['value'] = ('공항', '북로')
    elif 34 in routeIndex :
        direction['value'] = ('공항', '학익')
    elif 35 in routeIndex :
        direction['value'] = ('인천', '안양')
    elif 36 in routeIndex :
        direction['value'] = ('인천', '시흥')
    elif 37 in routeIndex :
        direction['value'] = ('현풍', '대구')
        ClickStr="중부내륙선의지선"
    elif 38 in routeIndex :
        direction['value'] = ('논산', '회덕')
        ClickStr="호남선의지선"
    direction.current()

    direction.place(x=255,y=80)

def InitInputLabel():
    global routeEn
    global direcEn
    TempFont = font.Font(g_Tk, size=20, weight='bold', family='Consolas')
    MenuFont = font.Font(g_Tk, size = 15, weight='bold', family='Consolas')

    route = Label(g_Tk, font=MenuFont, text = "도로명", fg="green")
    direc = Label(g_Tk, font=MenuFont, text = "방향", fg="green")
    # routeEn = Entry(g_Tk, font=TempFont, width = 20, borderwidth = 7, relief = 'ridge')
    # direcEn = Entry(g_Tk, font=TempFont, width=13, borderwidth=7, relief='ridge')

    route.pack()
    direc.pack()
    # routeEn.pack()
    # direcEn.pack()

    route.place(x=80, y=50)
    direc.place(x=300, y=50)
    # routeEn.place(x=80, y=180)
    # direcEn.place(x=80, y=120)

def OrderButton():
    global order, orderAscend, orderDescend, diesel, gasoline, lpg, oil

    oil = IntVar()
    MenuFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')

    order = Label(g_Tk, font=MenuFont, text="가격순 정렬", fg="green")
    order.place(x=275, y=115)

    diesel = Radiobutton(g_Tk, text="디젤", variable=oil, value=1)
    gasoline = Radiobutton(g_Tk, text="가솔린", variable=oil, value=2)
    lpg = Radiobutton(g_Tk, text="LPG", variable=oil, value=3)
    diesel.place(x=250, y=145)
    gasoline.place(x=310, y=145)
    lpg.place(x=375, y=145)

    orderAscend = Button(g_Tk, width=10, height=2, text="오름차순",command = UpSort)
    orderDescend = Button(g_Tk, width=10, height=2, text="내림차순",command=DownSort)
    orderAscend.place(x=250, y=175)
    orderDescend.place(x=340, y=175)

decode_key = unquote(spam.id())
def Search():
    global str,DataList,RenderText,ClickList

    DataList.clear()
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    direction = str.get()
    # direction = '인천'
    url = spam.url()
    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : decode_key, quote_plus('serviceKey') : '', quote_plus('type') : 'xml', quote_plus('routeName') : '', quote_plus('direction') : direction, quote_plus('numOfRows') : '30', quote_plus('pageNo') : '1' })
    request = Request(url + queryParams)

    response = urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        Data = response_body.decode('utf-8')
        parseData = parseString(Data)
        data = parseData.childNodes
        list = data[0].childNodes
        for item in list:
            if item.nodeName == "list":
                subitems = item.childNodes
                #1,2,3 - 디젤,가솔린,lpg 가격 ,
                DataList.append((subitems[1].firstChild.nodeValue,subitems[2].firstChild.nodeValue,subitems[3].firstChild.nodeValue, subitems[9].firstChild.nodeValue,subitems[7].firstChild.nodeValue))
        if ClickStr=="":
            RenderText.insert(INSERT,"주유소 없음")
        else:
            for i in range(len(DataList)):
                if DataList[i][4]==ClickStr:
                    RenderText.insert(INSERT, "[")
                    RenderText.insert(INSERT, i + 1)
                    RenderText.insert(INSERT, "] ")
                    RenderText.insert(INSERT, DataList[i][3])
                    RenderText.insert(INSERT, "주유소(휴게소)")
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "디젤 가격: ")
                    RenderText.insert(INSERT, DataList[i][0])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "가솔린 가격: ")
                    RenderText.insert(INSERT, DataList[i][1])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "LPG 가격: ")
                    RenderText.insert(INSERT, DataList[i][2])
                    RenderText.insert(INSERT, "\n")
                    RenderText.insert(INSERT, "\n\n")
    RenderText.configure(state='disabled')

def UpSort():
    global DataList,oil
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    if oil.get() == 1:
        tuple(DataList)
        DataList.sort(key=itemgetter(0))
        for i in range(len(DataList)):
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "] ")
            RenderText.insert(INSERT, DataList[i][3])
            RenderText.insert(INSERT, "주유소(휴게소)")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "디젤 가격: ")
            RenderText.insert(INSERT, DataList[i][0])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n\n")
    elif oil.get()==2:
        tuple(DataList)
        DataList.sort(key=itemgetter(1))
        for i in range(len(DataList)):
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "] ")
            RenderText.insert(INSERT, DataList[i][3])
            RenderText.insert(INSERT, "주유소(휴게소)")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "가솔린 가격: ")
            RenderText.insert(INSERT, DataList[i][1])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n\n")
    elif oil.get()==3:
        tuple(DataList)
        DataList.sort(key=itemgetter(2))
        for i in range(len(DataList)):
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "] ")
            RenderText.insert(INSERT, DataList[i][3])
            RenderText.insert(INSERT, "주유소(휴게소)")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "LPG 가격: ")
            RenderText.insert(INSERT, DataList[i][2])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n\n")
    RenderText.configure(state='disabled')

def DownSort():
    global DataList,oil
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    if oil.get() == 1:
        tuple(DataList)
        DataList.sort(reverse=True,key=itemgetter(0))
        for i in range(len(DataList)):
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "] ")
            RenderText.insert(INSERT, DataList[i][3])
            RenderText.insert(INSERT, "주유소(휴게소)")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "디젤 가격: ")
            RenderText.insert(INSERT, DataList[i][0])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n\n")
    elif oil.get()==2:
        tuple(DataList)
        DataList.sort(reverse=True,key=itemgetter(1))
        for i in range(len(DataList)):
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "] ")
            RenderText.insert(INSERT, DataList[i][3])
            RenderText.insert(INSERT, "주유소(휴게소)")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "가솔린 가격: ")
            RenderText.insert(INSERT, DataList[i][1])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n\n")
    elif oil.get()==3:
        tuple(DataList)
        DataList.sort(reverse=True,key=itemgetter(2))
        for i in range(len(DataList)):
            RenderText.insert(INSERT, "[")
            RenderText.insert(INSERT, i + 1)
            RenderText.insert(INSERT, "] ")
            RenderText.insert(INSERT, DataList[i][3])
            RenderText.insert(INSERT, "주유소(휴게소)")
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "LPG 가격: ")
            RenderText.insert(INSERT, DataList[i][2])
            RenderText.insert(INSERT, "\n")
            RenderText.insert(INSERT, "\n\n")
    RenderText.configure(state='disabled')

def InitRenderText():
    global RenderText
    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)
    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=34, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=25, y=220)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)
    RenderText.configure(state='disabled')


def InitButton():
    TempFont = font.Font(g_Tk, size = 12, weight="bold", family='Consolas')
    search = Button(g_Tk, font = TempFont, width = 6, height = 5, text="검색",command = Search)
    search.pack()
    search.place(x=435, y=95); search["bg"] = "blue"; search["fg"] = "white"


InitRouteBox()
InitDirec()
InitTopText()
InitInputLabel()
InitButton()
InitRenderText()
OrderButton()
g_Tk.mainloop()