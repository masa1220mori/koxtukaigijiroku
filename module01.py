import urllib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import datetime

class parliament:

    def get_xml(self,file):
        start='1'
        keyword=str(input("what's keyword:"))
        speaker=str(input("who's speaker※なしなら空白:"))
        nameoffile = str(file)
        xml_file = nameoffile + '.xml'

        while start!=None:

            startdate = '1999-01-01'
            enddate = str(datetime.date.today())
            meeting = ''

            #urllib.parse.quoteが日本語をコーディングしてくれる
            url = 'http://kokkai.ndl.go.jp/api/1.0/speech?' \
                                                + urllib.parse.quote('startRecord='
                                                + start
                                                + '&maximumRecords=100&any=' + keyword
                                                +'&speaker=' + speaker
                                                + '&nameOfMeeting=' + meeting
                                                + '&from=' + startdate
                                                + '&until=' + enddate)
         # Get信号のリクエストの検索結果（XML）

            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as response:
                 XmlData = response.read()
                 root = ET.fromstring(XmlData)
                 tree = ET.ElementTree(element= root)
                 tree.write(xml_file,encoding='utf-8',xml_declaration= True)

            s=int(start)
            print(s*100,'件読み込み')
            tree = ET.parse(xml_file)
            root = tree.getroot()
            NoR = root.find('numberOfRecords')
            NoR2 = root.find('numberOfReturn')
            Inor=int(NoR.text)
            if s*100<=Inor:
                s=s+1
                start=str(s)
            else:
                print('xml file is made')
                break


    def make_text(self,file):

        nameoffile = str(file)
        xml_file = nameoffile + '.xml'
        txt_file = nameoffile + '.txt'
        tree = ET.parse(xml_file)
        root = tree.getroot()
        NoR = root.find('numberOfRecords')
        NoR2 = root.find('numberOfReturn')
        sR = root.find('startRecord')
        nRP = root.find('nextRecordPosition')
        num=int(NoR2.text)
        name=root.findall('.//speaker')
        date = root.findall('.//date')
        speech = root.findall('.//speech')
        house=root.findall('.//nameOfHouse')
        meeting=root.findall('.//nameOfMeeting')
        t =0

        for t in range(num):
            if name[t].text== None:
                continue
            else:
                f = open(txt_file, 'a', encoding='utf-8')
                print(date[t].text, file=f)
                print(house[t].text,file=f)
                print(meeting[t].text, file=f)
                print(name[t].text,file=f)
                print(speech[t].text, file=f)
                f.close()
        return "txt file is made "

    def make_parliament_text(self, file):
        start = '1'
        keyword = str(input("what's keyword:"))
        speaker = str(input("who's speaker※なしなら空白:"))
        nameoffile = str(file)
        xml_file = nameoffile + '.xml'
        txt_file = nameoffile + '.txt'
        year = str(input("what's start year※半角英数字:"))
        month = str(input("what's start month:"))
        day = str(input("what's start day:"))
        startdate=year+'-'+month  +'-'+day

        while start != None:

            #startdate = '1999-01-01'
            enddate = str(datetime.date.today())
            meeting = ''

            # urllib.parse.quoteが日本語をコーディングしてくれる
            url = 'http://kokkai.ndl.go.jp/api/1.0/speech?' + urllib.parse.quote('startRecord='
                                                                                 + start
                                                                                 + '&maximumRecords=100&any=' + keyword
                                                                                 + '&speaker=' + speaker
                                                                                 + '&nameOfMeeting=' + meeting
                                                                                 + '&from=' + startdate
                                                                                 + '&until=' + enddate)
            # Get信号のリクエストの検索結果（XML）

            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as response:
                XmlData = response.read()
                root = ET.fromstring(XmlData)
                tree = ET.ElementTree(element=root)
                tree.write(xml_file, encoding='utf-8', xml_declaration=True)

            tree = ET.parse(xml_file)
            root = tree.getroot()
            NoR = root.find('numberOfRecords')
            NoR2 = root.find('numberOfReturn')
            NSP = root.find('nextRecordPosition')
            num = int(NoR2.text)
            s = int(start)
            print(s + 99, '件読み込み')
            name = root.findall('.//speaker')
            date = root.findall('.//date')
            speech = root.findall('.//speech')
            house = root.findall('.//nameOfHouse')
            meeting = root.findall('.//nameOfMeeting')
            Inor = int(NoR.text)
            if s + 99 <= Inor:
                t = 0

                for t in range(num):
                    if name[t].text == None:
                        continue
                    else:
                        f = open(txt_file, 'a', encoding='utf-8')
                        print(date[t].text, file=f)
                        print(house[t].text, file=f)
                        print(meeting[t].text, file=f)
                        print(name[t].text, file=f)
                        print(speech[t].text, file=f)
                        f.close()

                start = NSP.text
            else:
                print(NoR.text+"件処理完了")
                break


parliament01=parliament()
parliament01.make_parliament_text("keyword")#検索するキーワードを指定する