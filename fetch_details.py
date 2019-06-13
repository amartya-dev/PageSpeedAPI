
import requests 
import xlwt 
from xlwt import Workbook 
import xlrd

api_key = input("Enter the obtained api key : ")
def generate_excel(url, mode, clnt) :
    response = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url='+url+'&strategy='+mode+'&key='+api_key)
    js = response.json()

    print ("Score: ",js['lighthouseResult']['categories']['performance']['score']*100)

    k = []

    for m in js['lighthouseResult'] :

        try :
            for i in js['lighthouseResult'][m] :
                k.append([js['lighthouseResult'][m][i]['details'],js['lighthouseResult'][m][i]['title']])
        except :
            pass

    final_opportunities = []

    print (len(k))
    for i in k :
        if 'overallSavingsMs' in list(i[0].keys()) :
            
            print (i[1],i[0]['overallSavingsMs'])
            final_opportunities.append([i[1] , i[0]['overallSavingsMs']])


    
    try :
        wb = Workbook() 
        
        sheet1 = wb.add_sheet('Sheet 1')

        sheet1.write(0, 0, 'Score') 
        sheet1.write(0, 1, js['lighthouseResult']['categories']['performance']['score']*100) 


        sheet1.write(1, 0, 'Opportuninty') 
        sheet1.write(1, 1, 'Speed')
        for i in range (len(final_opportunities)) :
            for j in range (2) :
                sheet1.write(i+2,j,final_opportunities[i][j])
                
        wb.save(clnt+'details'+mode+'.xls') 
    except :
        wb = Workbook() 
        
        sheet1 = wb.add_sheet('Sheet 1')

        sheet1.write(0, 0, 'Score') 
        sheet1.write(0, 1, js['lighthouseResult']['categories']['performance']['score']*100)
        wb.save(clnt+'details'+mode+'.xls') 

workbook = xlrd.open_workbook('urls.xls')

sheet = workbook.sheet_by_index(0)

for row in range(sheet.nrows):
    url = sheet.cell(row,0).value
    mode = sheet.cell(row,1).value
    clnt = sheet.cell(row,2).value

    generate_excel(url, mode, clnt)
        
