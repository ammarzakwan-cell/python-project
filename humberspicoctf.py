def main():
    al = []
    for i in range(26):
        al.append(chr(ord("A") + i))

    enc_flag_pre = [16, 9, 3, 15, 3, 20, 6]
    enc_flag_body = [20,8,5,11,5,25,9,19,12,5,1,4,20,8,5,23,1,25] 

    flag = ""
    for i in enc_flag_pre:
        flag+= al[i - 1]
    
    flag += "{"
    for i in enc_flag_body:
        flag += al[i - 1]

    flag+= "}"
    print(flag)

if __name__ == "__main__":
    main()