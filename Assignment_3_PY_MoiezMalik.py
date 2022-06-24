from colorama import init
init()

def main():
    CodesFile = 'A3_Codes.txt'
    FG_GREEN = '\033[32m'
    FG_RED = '\033[31m'
    BOLD = '\033[1m'
    WARNING = '\033[93m'
    print('Reading file', CodesFile, '...\n')
    print(
        BOLD +
        "Valid Code (e.g. ABC2475A5R-14): Minimum 10 Character Long with Country Code (4th to 7th character) must be Digit and Security Code (10th Character) must be Uppercase  \n\nInvalid Restricted code: Security code 'R' can't be in Country code above 2000 \n"
    )

    # Open File
    products_Code_File = open(CodesFile, 'r')

    # Read each files in file
    product_Code_Lines = products_Code_File.readlines()

    # Loop though each line and check for Char count
    for code in product_Code_Lines:
        try:
            # Pull char 4-7 and convert into digit
            codeNum = code[3:7]
            convertCode = int(codeNum)

            # Pull 10th Char and convert into String
            securityChar = code[9:10]
            CovertSCode = str(securityChar)

            # Code must be 10 or more char and have 4-7 char digit and 10th char Uppercase Word
            if len(code) >= 10 and type(
                    convertCode) == int and CovertSCode.isupper():

                # R Security Code is restricted in Country code above 2000
                if convertCode > 2000 and CovertSCode == 'R':
                    print(WARNING + 'Invalid Restricted Code:', code)
                else:
                    print(FG_GREEN + 'Valid  code:', code)
            else:
                print(FG_RED + 'Invalid code:', code)
        except:
            print(FG_RED + 'Invalid code:', code)

    # Close File
    products_Code_File.close()


main()
