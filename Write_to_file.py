rom bs4 import BeautifulSoup
import csv
import re

html_file = "file_name.html"
#file name of the target html


fop = {}
#Final output dictionary

# { 'ROUTER_NAME' : {
#                         'show cdp neigh':'failed',
#                         'show running-config':'success',
#                         'show version':'success',
# },'':{}


#  }


# Function to parse "Command" and exception handling incase of it's unavailability
def command_parser(cmd):
        r_cmd = re.findall(r"\(([^0-9]+)\)",cmd)
        if r_cmd:
                return(r_cmd[0])
        cmd_op = re.findall(r"\Failure",cmd)
        if cmd_op:
                return("Unable to connect")
        return("None")

# Function to parse "Device  Name"
def deviceName(dname):
        spt = dname.split(":")
        return(re.sub(r"\s+","",spt[1]))



#SCRIPT START

#Creating headers for CSV file 
csv_headers=['Device Name','sh run','show cdp neigh','show ip access-list','show running-config','show startup-config','show version']
with open('rConfigDevice.csv','a') as csvf:
        writer = csv.writer(csvf)
        writer.writerows([csv_headers])
csvf.close()


#Beautiful soup parsing
with open(html_file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')



table = soup.find_all('table',attrs={'id':'hor-zebra'})



for i in range(len(table)):
        cols = []
        table_heading = table[i].find('thead')
        table_body = table[i].find('tbody')

        device_name = deviceName(table_heading.text.strip().encode("utf-8"))
        # print device_name
        if device_name not in fop:
                fop[device_name] = {}
        rows = table_body.find_all('tr')
        status = ""
        notice = ""
        for row in rows:
                columns = row.find_all('td')
                if columns[0].text.strip().encode("utf-8") == 'Status:':
                        status = columns[1].text.strip().encode("utf-8")
                        print status
                if columns[0].text.strip().encode("utf-8") == 'Notice:':
                        notice = command_parser(columns[1].text.strip().encode("utf-8"))
                        print notice

            
        fop[device_name].update({notice:status}) 
        #Dictionary appending with all the new data


#ADDING THE VALUES TO THE CSV

for i in fop:
        test = []
        if "Unable to connect" in fop[i]:
                test.append([i,'Unable to connect','Unable to connect','Unable to connect','Unable to connect','Unable to connect','Unable to connect'])
        else:
                test.append([
                        i,
                        fop[i]['sh run'] if 'sh run' in fop[i] else '-',
                        fop[i]['show cdp neigh'] if 'show cdp neigh' in fop[i] else '-',
                        fop[i]['show ip access-list'] if 'show ip access-list' in fop[i] else '-',
                        fop[i]['show running-config'] if 'show running-config' in fop[i] else '-',
                        fop[i]['show startup-config'] if 'show startup-config' in fop[i] else '-',
                        fop[i]['show version'] if 'show version' in fop[i] else '-'
        ])

        with open('rConfigDevice.csv','a') as csvf:
                writer = csv.writer(csvf)
                writer.writerows(test)
        csvf.close()
