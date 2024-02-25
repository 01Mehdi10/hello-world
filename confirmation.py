def question(annonce, essais = 4, please ='Oui ou non, s.v.p.!'):
  while essais > 0:
    reponse = input(annonce)
    if reponse in ('o', 'oui','O','Oui','OUI'):
      return 1
    if reponse in ('n','non','N','Non','NON'):
      return 0
    print(please)
    essais = essais - 1
    
# appel fonction
rep = question('Avez-vous compris ? ', 2, 'Répondez par oui ou par non !')