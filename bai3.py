x = input("Nhap day du ho ten cua ban cua ban: ");
print(x);
def TN(n):
    str1 = str(n);
    str2 = str1[::-1];
    if (str1 == str2):
        return True;
    else:
        return False;
 
n = int(input("Nhập số nguyên dương n = "));
print("Tổng các chữ số của", n , "là", TN(n));
