def replace_domain(address,new_domain,prev_domain="kaaj.com"):
  name,domain=address.split("@")

  if domain==prev_domain:
    address=name+"@"+new_domain
    print("Changed:"+address)
  else:
    print("Unchanged:"+address)
replace_domain("bob@sheba.xyz","sheba.xyz")
