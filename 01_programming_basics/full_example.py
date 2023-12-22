print("--- [ Keliamųjų metų radimo programa ] ---")
metai = input("Įveskite metus: ")
if metai.isnumeric():
    metai = int(metai)
    keliamieji = metai % 4 == 0 and metai % 100 != 0 or metai % 400 == 0
    if keliamieji:
        print(f"{metai} yra keliamieji")
    else:
        print(f"{metai} yra nekeliamieji")
else:
    print("metai turi būti skaičius")
print('bye!')
