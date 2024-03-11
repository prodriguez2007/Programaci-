# RO_P083_monedes

dolars_1 = int(input(" Quantitat de dólars="))

[bitllets_100, dolars] = divmod(dolars_1,100)
[bitllets_50, dolars] = divmod(dolars, 50)
[bitllets_20, dolars] = divmod(dolars,20)
[bitllets_10, dolars] = divmod(dolars, 10)
[bitllets_5, dolars] = divmod(dolars,5)
[bitllets_1, dolars] = divmod(dolars, 1)

print(f"{dolars_1} dòlars equivalen a {bitllets_100} bitllets de 100, {bitllets_50} de 50, {bitllets_20} de 20, {bitllets_10} de 10, {bitllets_5} de 5 i {bitllets_1} de 1")