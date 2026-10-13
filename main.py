from pyscript import display, document

Members = ["Kim Namjoon", "Kim Seokjin", "Min Yoongi", "Jung Hoseok", "Park Jimin", "Kim Taehyung", "Jeon Jungkook", "Anissa Manaloto"]

def check_membership(e):
    document.getElementById("output1").innerHTML = ""

    fname = document.getElementById("first_name").value
    lname = document.getElementById("last_name").value

    applicant_name = str(fname + " " + lname)

    check = applicant_name.title() in Members

    verified = "Congratulations" + " " + applicant_name + "!" + " " + "Welcome to the OBMC Theater Club!"
    not_verified = "Sorry" + " " + applicant_name + ", " + "your name is not on the list."

    display({
        True: verified,
        False: not_verified
    }[check], target="output1")
