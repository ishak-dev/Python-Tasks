opposites = {"up": "down", "right": "wrong", "true": "false"}
alias = opposites
print(alias is opposites)
acopy = opposites.copy()
acopy["right"] = "left"
print(opposites["right"])
