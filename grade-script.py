import csv
import tkinter
from tkinter import filedialog
from operator import itemgetter


# window = tkinter.Tk()
# window.title('Google to Skyward quiz converter')
#
# tkinter.Label(window, text = "Google CSV").grid(row = 0)
# tkinter.Entry(window).grid(row = 0, column = 1)
#
# tkinter.Label(window, text = "Skyward CSV").grid(row = 1)
# tkinter.Entry(window).grid(row = 1, column = 1)
#
# tkinter.Button(window, text = "Convert").grid(row = 2, column = 1)
# tkinter.filename =  filedialog.askopenfilename(title = "Select google classroom CSV",filetypes = (("csv files","*.csv"),("all files","*.*")))
# tkinter.filename =  filedialog.askopenfilename(title = "Select Skyward CSV",filetypes = (("csv files","*.csv"),("all files","*.*")))
# window.mainloop()

def google_read():
    file = str(input('google file: '))
    with open(file,'r') as f:
        read = csv.reader(f)
        google = list(read)
    return google


def skyward_read():
    file = str(input('skyward file: '))
    with open(file,'r') as f:
        read = csv.reader(f)
        skyward = list(read)
    return skyward


def write_to_csv(skyward):
    myFile = open('import_to_skyward.csv', 'w')
        with myFile:
        writer = csv.writer(myFile)
        writer.writerows(skyward)


def convert_grade(google, skyward):
    pretext = ['Last Name', 'First Name', 'Email Address', 'Grade', 'Assignment State', 'Comments']
    count = 0

    google_sorted = sorted(google, key=itemgetter(0))
    google_sorted.remove(pretext)

    for student in google_sorted:
        count += 1
        if student[3] == '':
            skyward[5+count][4] = 'IP'
        elif float(student[3]) > 2.0:
            skyward[5+count][4] = 'M'
        elif float(student[3]) == 2.0:
            skyward[5+count][4] = 'P'
        elif float(student[3]) < 2.0:
            skyward[5+count][4] = 'SC'

    return skyward

####
# QUIZ TRANSLATION
def done():
    with open('google.csv','r') as f:
        read = csv.reader(f)
        google = list(read)

    with open('skyward.csv','r') as f:
        read = csv.reader(f)
        skyward = list(read)

    pretext = ['Last Name', 'First Name', 'Email Address', 'Grade', 'Assignment State', 'Comments']
    count = 0

    google_sorted = sorted(google, key=itemgetter(0))
    google_sorted.remove(pretext)

    for student in google_sorted:
        count += 1
        if student[3] == '':
            skyward[5+count][4] = 'IP'
        elif float(student[3]) > 2.0:
            skyward[5+count][4] = 'M'
        elif float(student[3]) == 2.0:
            skyward[5+count][4] = 'P'
        elif float(student[3]) < 2.0:
            skyward[5+count][4] = 'SC'

    myFile = open('import_to_skyward.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(skyward)

##############
# TWO ASSIGNMENT AVERAGING
def done():
    with open('google1.csv','r') as f:
        read = csv.reader(f)
        google1 = list(read)

    with open('google2.csv','r') as f:
        read = csv.reader(f)
        google2 = list(read)

    with open('skyward.csv','r') as f:
        read = csv.reader(f)
        skyward = list(read)

    pretext = ['Last Name', 'First Name', 'Email Address', 'Grade', 'Assignment State', 'Comments']
    count = 0

    google1_sorted = sorted(google1, key=itemgetter(0))
    google1_sorted.remove(pretext)

    google2_sorted = sorted(google2, key=itemgetter(0))
    google2_sorted.remove(pretext)

    for st1, st2 in zip(google1_sorted, google2_sorted):
        count += 1
        if st1[3] == '' or st2[3] == '':
            if st1[3] == '' and st2[3] == '':
                skyward[5+count][4] = 'IP'
            elif st1[3] == '':
                if float(st2[3]) == 4.0:
                    skyward[5+count][4] = 'P'
                elif float(st2[3]) == 3.0 or float(st2[3]) == 2.0:
                    skyward[5+count][4] = 'SC'
                elif float(st2[3]) < 2.0:
                    skyward[5+count][4] = 'IP'

            elif st2[3] == '':
                if float(st1[3]) == 4.0:
                    skyward[5+count][4] = 'P'
                elif float(st1[3]) == 3.0 or float(st1[3]) == 2.0:
                    skyward[5+count][4] = 'SC'
                elif float(st1[3]) < 2.0:
                    skyward[5+count][4] = 'IP'
        else:
            s1 = float(st1[3])
            s2 = float(st2[3])

            if s1 + s2 > 6.0:
                skyward[5+count][4] = 'M'
            elif s1 + s2 == 6.0 or s1 + s2 == 5.0:
                skyward[5+count][4] = 'P'
            elif s1 + s2 == 4.0 or s1 + s2 == 3.0:
                skyward[5+count][4] = 'SC'
            elif s1 + s2 < 3.0:
                skyward[5+count][4] = 'IP'

    myFile = open('import_to_skyward.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(skyward)

#################
# 6TH PERIOD SPLIT CLASS HELL
def done():
    with open('google1.csv','r') as f:
        read = csv.reader(f)
        google1 = list(read)

    with open('google2.csv','r') as f:
        read = csv.reader(f)
        google2 = list(read)

    with open('skyward.csv','r') as f:
        read = csv.reader(f)
        skyward = list(read)

    pretext = ['Last Name', 'First Name', 'Email Address', 'Grade', 'Assignment State', 'Comments']
    count = 0

    #google1_sorted = sorted(google1, key=itemgetter(0))
    #google1_sorted.remove(pretext)

    #google2_sorted = sorted(google2, key=itemgetter(0))
    #google2_sorted.remove(pretext)
    google1_sorted = google1
    google1_sorted.remove(pretext)
    google2_sorted = google2
    google2_sorted.remove(pretext)

    for st1, st2 in zip(google1_sorted, google2_sorted):
        count += 1
        if st1[3] == '' or st2[3] == '':
            if st1[3] == '' and st2[3] == '':
                skyward[5+count][4] = 'IP'
            elif st1[3] == '':
                if float(st2[3]) == 4.0:
                    skyward[5+count][4] = 'P'
                elif float(st2[3]) == 3.0 or float(st2[3]) == 2.0:
                    skyward[5+count][4] = 'SC'
                elif float(st2[3]) < 2.0:
                    skyward[5+count][4] = 'IP'

            elif st2[3] == '':
                if float(st1[3]) == 4.0:
                    skyward[5+count][4] = 'P'
                elif float(st1[3]) == 3.0 or float(st1[3]) == 2.0:
                    skyward[5+count][4] = 'SC'
                elif float(st1[3]) < 2.0:
                    skyward[5+count][4] = 'IP'
        else:
            s1 = float(st1[3])
            s2 = float(st2[3])

            if s1 + s2 > 6.0:
                skyward[5+count][4] = 'M'
            elif s1 + s2 == 6.0 or s1 + s2 == 5.0:
                skyward[5+count][4] = 'P'
            elif s1 + s2 == 4.0 or s1 + s2 == 3.0:
                skyward[5+count][4] = 'SC'
            elif s1 + s2 < 3.0:
                skyward[5+count][4] = 'IP'

    myFile = open('import_to_skyward.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(skyward)
