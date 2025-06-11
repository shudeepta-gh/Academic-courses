def hospital_fee(**kwargs):
  max_payer=""
  max_amount=-1
  for k,v in kwargs.items():
    if v>max_amount:
      max_amount=v
      max_payer=k
    else:
      if max_amount==v:
         max_payer+= f", {k}"
  return[max_amount,max_payer]

max_amount, max_payer = hospital_fee(Neymar =
1000, Dembele = 600, Reus = 500, Bale = 1000)

max_amount, max_payer = hospital_fee(Mashrafe =
400, Bumrah = 900, Steyn = 1200, Cummins = 900,
Wood = 400, Marsh = 700)

print("Highest fee was",max_amount,"tk which was paid by",max_payer)
