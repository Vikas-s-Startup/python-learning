S1 = "one+two-one-one+two+one"
S2 = "two-two-one-two"
S3 = "two"

def solution(S):
    S = S.replace("one", "1").replace("two", "2")
    print(S)
    result = 0
    i = 0
    while i < len(S):
        if S[i] == "+":
            i+=1
            if S[i] == 1:
                result+=1
            elif S[i] == 2:
                result +=2
        elif S[i] == "-":
            i+=1
            if S[i] == 1:
                result -= 1
            elif S[i] == 2:
                result -= 2
        else:
            if S[i] == '1':
                result += 1
            elif S[i] == '2':
                result += 2
        i += 1
    return result


print(solution(S3))