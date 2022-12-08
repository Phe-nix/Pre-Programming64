"""[quiz] โรงเรียนเวทย์มนต์เปิดรับสมัครแล้ว"""
def main():
    """[quiz] โรงเรียนเวทย์มนต์เปิดรับสมัครแล้ว"""
    name = input()
    age = int(input())
    sex = input().capitalize()
    height = float(input())
    result = ""
    sex2 = ""
    if 13 <= age <= 15:
        if sex == "Male" and height >= 160:
            result += ("You can study in junior high school.")
            sex2 += ("Mr.")
        elif sex == "Female" and height >= 155:
            result += ("You can study in junior high school.")
            sex2 += ("Miss")
        else:
            result += ("You can not join this school.")
            if sex == "Male":
                sex2 += ("Mr.")
            elif sex == "Female":
                sex2 += ("Miss")
    elif 16 <= age <= 18:
        if sex == "Male" and height >= 170:
            result += ("You can study in senior high school.")
            sex2 += ("Mr.")
        elif sex == "Female" and height >= 165:
            result += ("You can study in senior high school.")
            sex2 += ("Miss")
        else:
            result += ("You can not join this school.")
            if sex == "Male":
                sex2 += ("Mr.")
            elif sex == "Female":
                sex2 += ("Miss")
    else:
        if sex == "Male":
            sex2 += ("Mr.")
            result += ("You can not join this school.")
        elif sex == "Female":
            sex2 += ("Miss")
            result += ("You can not join this school.")
    print("%s %s Age:%3d Height:%7.2f"%(sex2, name, age, height))
    print(result)
main()
