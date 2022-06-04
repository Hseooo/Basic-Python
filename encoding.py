userInput = input("한글입력 : ")

encodedUserInput = userInput.encode("utf-8")

print("사용자 입력 : ", userInput)
print("UTF-8변환", encodedUserInput)
