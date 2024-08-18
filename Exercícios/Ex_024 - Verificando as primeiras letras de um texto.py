print("Vamos verificar se você nasceu em uma cidade que começa com a palavra Santo")
cid = input("Qual cidade você nasceu? ").strip ()
cid = cid.lower()
cid_list = cid.split()
res = cid_list [0] == "santo" 
print(res)