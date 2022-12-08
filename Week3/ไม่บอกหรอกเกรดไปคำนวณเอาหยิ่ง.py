"""ไม่บอกหรอกเกรดไปคำนวณเอาหยิ่ง"""
def main():
    """ไม่บอกหรอกเกรดไปคำนวณเอาหยิ่ง"""
    score = int(input())
    print("0.0"*(score <= 49) or "1.0"*(score <= 54) or "1.5"*(score <= 59)\
    or "2.0"*(score <= 64) or "2.5"*(score <= 69)\
    or "3.0"*(score <= 74) or "3.5"*(score <= 79) or "4.0"*(score <= 100))
main()
