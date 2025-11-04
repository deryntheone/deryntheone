def croissant():
    print("A croissant is a French Viennoiserie in a crescent shape made from a laminated yeast dough that sits between a bread and a puff pastry.")

def macaron():
    print("A macaron or French macaroon is a sweet meringue-based confection made with egg white, icing sugar, granulated sugar, almond meal, and often food colouring.")

def baklava():
    print("Baklava is a layered pastry dessert made of filo pastry, filled with chopped nuts, and sweetened with either syrup or honey.")

def puff_pastry():
    print("Puff pastry, also known as pâte feuilletée, is a light, flaky pastry, its base dough (détrempe) composed of wheat flour and water. Butter or other solid fat (beurrage) is then layered into the dough. The dough is repeatedly rolled and folded, rested, re-rolled and folded, encasing solid butter between each resulting layer.")

def danish_pastry():
    print("A Danish pastry is a multilayered, laminated sweet Viennoiserie. Like other Viennoiserie, such as croissants, it is neither a bread nor a pastry, as it uses yeast-leavened dough, that is laminated like puff pastry to create a layered texture.")

def cannoli():
    print("Cannoli are Sicilian pastries consisting of a tube-shaped shell of fried pastry dough, filled with a sweet and creamy filling containing ricotta cheese. Their size ranges from 9 to 20 centimetres (3+1⁄2 to 8 in). In mainland Italy, the food is commonly known as cannolo siciliano.")

def eclair():
    print("An éclair is a pastry made with choux dough filled with a cream and topped with a flavored icing. The dough, which is the same as that used for profiteroles, is typically piped into an oblong shape with a pastry bag and baked until it is crisp and hollow inside.")

def tiramisu():
    print("Tiramisu is an Italian dessert made of ladyfinger pastries (savoiardi) dipped in coffee, layered with a whipped mixture of egg yolks, sugar, and mascarpone, and topped with cocoa powder. The recipe has been adapted into many varieties of cakes and other desserts. Its origin is disputed between the Italian regions of Veneto and Friuli-Venezia Giulia. The name comes from the Italian tirami su (lit. 'pick me up' or 'cheer me up').")

def strudel():
    print("Strudel is a type of layered pastry with a filling that is usually sweet, but savoury fillings are also common. It became popular in the 18th century throughout the Habsburg Empire. Strudel is part of Austrian cuisine and German cuisine but is also common in other Central European cuisines. In Italy it is recognized as a prodotto agroalimentare tradizionale (PAT) of South Tyrol.")

def mille_feuille():
    print("A mille-feuille, also known by the names Napoleon in North America, Post-Soviet countries, vanilla slice in the United Kingdom, and custard slice, is a French dessert made of puff pastry layered with pastry cream. Its modern form was influenced by improvements made by Marie-Antoine Carême.")

print("WELCOME TO THE PASTRY DICTIONARY!\n \n1. Croissant\n2. Macaron\n3. Baklava\n4. Puff Pastry\n5. Danish Pastry\n6. Cannoli\n7. Eclair\n8. Tiramisu\n9. Strudel\n10. Mille-feuille")

choice = input("\nPlease enter the corresponding number of your desired pastry: ")

if choice == '1':
    croissant()
elif choice == '2':
    macaron()
elif choice == '3':
    baklava()
elif choice == '4':
    puff_pastry()
elif choice == '5':
    danish_pastry()
elif choice == '6':
    cannoli()
elif choice == '7':
    eclair()
elif choice == '8':
    tiramisu()
elif choice == '9':
    strudel()
elif choice == '10':
    mille_feuille()
else:
    print("Sorry, but we do not have that pastry in our dictionary yet. Please feel free to contact the developer to submit a pastry definition request!")

