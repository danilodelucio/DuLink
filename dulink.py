import pyperclip

error_msg = "[ERRO!] Link inválido!"
sucess_msg = "[FEITO!] Link gerado e copiado para a área de transferência!"

print("Desenvolvido por: Danilo de Lucio")
print("www.danilodelucio.com")
print("20/04/2022")

while True:
    print("")
    link_ref = input("Insira o link de referência: ")

    index_start = "src="
    index_end = " width="

    if index_start in link_ref and index_end in link_ref:
        link_final = link_ref[link_ref.find(index_start)+5:link_ref.find(index_end)-1]

        link_final = link_final.replace("embed", "download")
        print("-"*len(link_final))
        print(sucess_msg)
        print(link_final)
        print("-" * len(link_final))

        pyperclip.copy(link_final)
    else:
        print("-"*len(error_msg))
        print(error_msg)
        print("-" *len(error_msg))