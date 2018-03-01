
import os
import urllib.request, urllib.error, urllib.parse
import re
import operator

#def checkfile():
#    filecheck = os.path.isfile('./http_access_log.txt')
#    return filecheck 


def main():
    # Open connection to URL
    print("Attempting to make connection with https://s3.amazonaws.com/tcmg476/http_access_log...")
    webUrl = urllib.request.urlopen("https://s3.amazonaws.com/tcmg476/http_access_log")
    
    # Get the result code and print it
    print("Result Code: " + str(webUrl.getcode()), "Successful Connection. \n")    
    
    # Read the data from the URL and Print it
    global data
    data = webUrl.read()
    return data

def openwrite(lines): 
    # Open a file for writing and create it if it doesn't exist
    f = open("http_access_log.txt","w+")
    
    # Write the data from the website to the file
    f.write(lines.decode("UTF-8"))
    
    # Close the file when done
    f.close()
    
def openread():
    global count
    count = 0
    f = open("http_access_log.txt","r")
    if f.mode == 'r':
        fl = f.readlines()
        for x in fl:
            count = count + 1
        print("Total requests within log:", count, "\n")
        monthlyaverage = count/12
        print("Average number of requests per month:", str(round(monthlyaverage,2)), "\n")
    return fl

def regexsearch(lines):
    statuscount400 = 0
     
    statuscount300 = 0
     
    # Open files of months to write data to
    a = open("October1994.txt","w+")
    b = open("November.txt","w+")
    c = open("December.txt","w+")
    d = open("January.txt","w+")
    e = open("February.txt","w+")
    f = open("March.txt","w+")
    g = open("April.txt","w+")
    h = open("May.txt","w+")
    i = open("June.txt","w+")
    j = open("July.txt","w+")
    k = open("August.txt","w+")
    l = open("September.txt","w+")
    m = open("October1995.txt","w+")
    NEWFILES = []
    MULTFILES = []
    ERRORS = []
    regex = re.compile(".*\[([^:]*):(.*) \-[0-9]{4}\] \"([A-Z]+) (.+?)( HTTP.*\"|\") ([2-5]0[0-9]) .*")
    
    # Splitting lines for finding least and most requested files
    FILES = {}
    for x in lines:
        parts = regex.split(x)
        if (len(parts) >= 7):
            if parts[4] not in NEWFILES and parts[4] not in FILES:
                NEWFILES.append(parts[4])
            elif parts[4] in NEWFILES and parts[4] not in FILES:
                FILES[parts[4]] = 2
                NEWFILES.remove(parts[4])
            elif parts[4] not in NEWFILES and parts [4] in FILES:
                FILES[parts[4]] += 1
    maximum = max(iter(FILES.items()), key=operator.itemgetter(1))[0]
    print("Number of files that were only requested once:", len(NEWFILES), "A few examples include:", NEWFILES[12], ",", NEWFILES[534], ", and", NEWFILES[696])
    print("Number of files that were requested on multiple occassions:", len(list(FILES.keys())), ". The most requested file is:", maximum, ". It has been requested", FILES[maximum], "times. \n")


    # Splitting lines and counting 4xx/3xx status codes
    for x in lines:
        parts = regex.split(x)
        if (len(parts) >= 7):    
            if ('400' in parts[6] or '401' in parts[6] or '402' in parts[6] or '403' in parts[6] or '404' in parts[6] or '405' in parts[6] or '406' in parts[6] or '407' in parts[6] or '408' in parts[6] or '409' in parts[6] or '410' in parts[6]
                 or '411' in parts[6] or '412' in parts[6] or '413' in parts[6] or '413' in parts[6] or '414' in parts[6] or '415' in parts[6] or '416' in parts[6] or '417' in parts[6] or '418' in parts[6] or '421' in parts[6] or '422' in parts[6]
                 or '423' in parts[6] or '424' in parts[6] or '426' in parts[6] or '428' in parts[6] or'429' in parts[6] or '431' in parts[6] or '451' in parts[6] ):
                statuscount400 += 1
            if ('300' in parts[6] or '301' in parts[6] or '302' in parts[6] or '303' in parts[6] or '304' in parts[6] or '305' in parts[6] or '306' in parts[6] or '307' in parts[6] or '308' in parts[6]):
                statuscount300 += 1 
    percentage400 = (statuscount400 / count)
    percentage300 = (statuscount300 / count)
    print("There are a total of", statuscount400, "4XX status codes, and", statuscount300, "3XX status codes.")
    print("Percentage of 4XX status codes: " + str(round(percentage400,2)) + "%")
    print("Percentage of 3XX status codes: " + str(round(percentage300,2)) + "%")
    print("Standby for summary of requests...\n")
 
         
    # Splitting lines and adding to month files

    for x in lines:
        parts = regex.split(x)
        if (len(parts) >= 7):
            if ('Oct' in parts[1] and '1994' in parts[1]):
                a.write(x)
                #print "Line added to October 1994 File"
            if ('Nov' in parts[1] and '1994' in parts[1]):
                b.write(x)
                #print "Line added to November File"            
            if ('Dec' in parts[1] and '1994' in parts[1]):
                c.write(x)
                #print "Line added to December File"  
            if ('Jan' in parts[1] and '1995' in parts[1]):
                d.write(x)
                #print "Line added to January File"
            if ('Feb' in parts[1] and '1995' in parts[1]):
                e.write(x)
                #print "Line added to February File"
            if ('Mar' in parts[1] and '1995' in parts[1]):
                f.write(x)
                #print "Line added to March File"
            if ('Apr' in parts[1] and '1995' in parts[1]):
                g.write(x)
                #print "Line added to April File"
            if ('May' in parts[1] and '1995' in parts[1]):
                h.write(x)
                #print "Line added to May File"
            if ('Jun' in parts[1] and '1995' in parts[1]):
                i.write(x)
                #print "Line added to June File"
            if ('Jul' in parts[1] and '1995' in parts[1]):
                j.write(x)
                #print "Line added to July File"
            if ('Aug' in parts[1] and '1995' in parts[1]):
                k.write(x)
                #print "Line added to August File"
            if ('Sep' in parts[1] and '1995' in parts[1]):
                l.write(x)
                #print "Line added to September File"
            if ('Oct' in parts[1] and '1995' in parts[1]):
                m.write(x)
                #print "Line added to October 1995 File"                          
        # Error Check 
        if not parts or len(parts) < 7:
            #print "Error parsing line! Log entry added to ERRORS[] list..."
            ERRORS.append(x)
    
    a.close()
    b.close()
    c.close()
    d.close()
    e.close()
    f.close()
    g.close()
    h.close()
    i.close()
    j.close()
    k.close()
    l.close()
    m.close()          
    
    
    # Opening files to read
    a = open("October1994.txt","r")
    b = open("November.txt","r")
    c = open("December.txt","r")
    d = open("January.txt","r")
    e = open("February.txt","r")
    f = open("March.txt","r")
    g = open("April.txt","r")
    h = open("May.txt","r")
    i = open("June.txt","r")
    j = open("July.txt","r")
    k = open("August.txt","r")
    l = open("September.txt","r")
    m = open("October1995.txt","r")    
            
    # Naming variables that will be used in counting and averaging lines
    oct94fcount = 0 
    novfcount = 0 
    decfcount = 0 
    janfcount = 0 
    febfcount = 0 
    marfcount = 0 
    aprfcount = 0 
    mayfcount = 0 
    junfcount = 0 
    julfcount = 0  
    augfcount = 0 
    sepfcount = 0 
    oct95fcount = 0 
  
    
    if a.mode == 'r':
        oct94r = a.readlines()
        for x in oct94r:
            oct94fcount += 1
    oct94davg = oct94fcount/8
    oct94wavg = oct94fcount/1.14
    print("October 1994 results:")       
    print("During the month of October 1994, there was a total number of", oct94fcount, "beginning on the 24th.")
    print("That is an average of", oct94davg, "requests per day, and an average of", str(round(oct94wavg,2)), "requests per week.")
    
    if b.mode == 'r':
        novr = b.readlines()
        for x in novr:
            novfcount += 1
    novdavg = novfcount/30
    novwavg = novfcount/4.29
    print("\nNovember 1994 results:")       
    print("During the month of November 1994, there was a total number of " + str(novfcount) + ".")
    print("That is an average of", str(round(novdavg,2)), "requests per day, and an average of", str(round(novwavg,2)), "requests per week.")    

    if c.mode == 'r':
        decr = c.readlines()
        for x in decr:
            decfcount += 1
    decdavg = decfcount/31
    decwavg = decfcount/4.43
    print("\nDecember 1994 results:")       
    print("During the month of December 1994, there was a total number of " + str(decfcount) + ".")
    print("That is an average of", str(round(decdavg,2)), "requests per day, and an average of", str(round(decwavg,2)), "requests per week.")    
    
    if d.mode == 'r':
        janr = d.readlines()
        for x in janr:
            janfcount += 1
    jandavg = janfcount/31
    janwavg = janfcount/4.43
    print("\nJanuary 1995 results:")       
    print("During the month of January 1995, there was a total number of " + str(janfcount) + ".")
    print("That is an average of", str(round(jandavg,2)), "requests per day, and an average of", str(round(janwavg,2)), "requests per week.")
    
    if e.mode == 'r':
        febr = e.readlines()
        for x in febr:
            febfcount += 1
    febdavg = febfcount/28
    febwavg = febfcount/4
    print("\nFebruary 1995 results:")       
    print("During the month of February 1995, there was a total number of " + str(febfcount) + ".")
    print("That is an average of", str(round(febdavg,2)), "requests per day, and an average of", str(round(febwavg,2)), "requests per week.")    
    
    if f.mode == 'r':
        marr = f.readlines()
        for x in marr:
            marfcount += 1
    mardavg = marfcount/31
    marwavg = marfcount/4.43
    print("\nMarch 1995 results:")       
    print("During the month of March 1995, there was a total number of " + str(marfcount) + ".")
    print("That is an average of", str(round(mardavg,2)), "requests per day, and an average of", str(round(marwavg,2)), "requests per week.") 
    
    if g.mode == 'r':
        aprr = g.readlines()
        for x in aprr:
            aprfcount += 1
    aprdavg = aprfcount/30
    aprwavg = aprfcount/4.29
    print("\nApril 1995 results:")       
    print("During the month of April 1995, there was a total number of " + str(aprfcount) + ".")
    print("That is an average of", str(round(aprdavg,2)), "requests per day, and an average of", str(round(aprwavg,2)), "requests per week.") 
    
    if h.mode == 'r':
        mayr = h.readlines()
        for x in mayr:
            mayfcount += 1
    maydavg = mayfcount/31
    maywavg = mayfcount/4.43
    print("\nMay 1995 results:")       
    print("During the month of May 1995, there was a total number of " + str(mayfcount) + ".")
    print("That is an average of", str(round(maydavg,2)), "requests per day, and an average of", str(round(maywavg,2)), "requests per week.")    

    if i.mode == 'r':
        junr = i.readlines()
        for x in junr:
            junfcount += 1
    jundavg = junfcount/30
    junwavg = junfcount/4.29
    print("\nJune 1995 results:")       
    print("During the month of June 1995, there was a total number of " + str(junfcount) + ".")
    print("That is an average of", str(round(jundavg,2)), "requests per day, and an average of", str(round(junwavg,2)), "requests per week.") 
    
    if j.mode == 'r':
        julr = j.readlines()
        for x in julr:
            julfcount += 1
    juldavg = julfcount/31
    julwavg = julfcount/4.43
    print("\nJuly 1995 results:")       
    print("During the month of July 1995, there was a total number of " + str(julfcount) + ".")
    print("That is an average of", str(round(juldavg,2)), "requests per day, and an average of", str(round(julwavg,2)), "requests per week.")
    
    if k.mode == 'r':
        augr = k.readlines()
        for x in augr:
            augfcount += 1
    augdavg = augfcount/31
    augwavg = augfcount/4.43
    print("\nAugust 1995 results:")       
    print("During the month of August 1995, there was a total number of " + str(augfcount) + ".")
    print("That is an average of", str(round(augdavg,2)), "requests per day, and an average of", str(round(augwavg,2)), "requests per week.")   
    
    if l.mode == 'r':
        sepr = l.readlines()
        for x in sepr:
            sepfcount += 1
    sepdavg = sepfcount/30
    sepwavg = sepfcount/4.29
    print("\nSeptember 1995 results:")       
    print("During the month of September 1995, there was a total number of " + str(sepfcount) + ".")
    print("That is an average of", str(round(sepdavg,2)), "requests per day, and an average of", str(round(sepwavg,2)), "requests per week.")    

    if m.mode == 'r':
        oct95r = m.readlines()
        for x in oct95r:
            oct95fcount += 1
    oct95davg = oct95fcount/11
    oct95wavg = oct95fcount/1.57
    print("\nOctober 1995 results:")        
    print("During the month of October 1995, there was a total number of", oct95fcount, "ending on the 11th.")
    print("That is an average of", str(round(oct95davg,2)), "requests per day, and an average of", str(round(oct95wavg,2)), "requests per week.")    
            
    a.close()
    b.close()
    c.close()
    d.close()
    e.close()
    f.close()
    g.close()
    h.close()
    i.close()
    j.close()
    k.close()
    l.close()
    m.close()            

    
if __name__ == "__main__":
#    print checkfile()
    main()
    openwrite(data)
    fl = openread()
    regexsearch(fl)