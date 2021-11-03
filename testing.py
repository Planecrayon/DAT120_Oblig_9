

class Question:

    def __init__(self, question: str, correct: int, alt: list,): # Klassen tar inn tre argument, og alle har definert verditype :str, :int, :list
        self.question = question
        self.alt = alt
        self.correct = correct

    def sjekk_svar(self, answer):
        if answer -1 == self.correct:
            return True
        elif answer -1 != self.correct:
            return  False
        #return answer - 1 == self.correct # kontollerar om brukeres svar == correct, (-1 fordi python byrjar å telle på 0)
    def korrekt_svar_tekst(self):
        return str(f'Rett svar er: {self.alt[self.correct]} \n') # returnerar rett svar

    def __str__(self):
        questions_str = '' # sett questions_str = lik ei blank str for at python veit kva verdi type det skal vær og for at det skal være ein verdi i variabelen
        for i in range(0, len(self.alt)): # ein for loop som går frå 0 og til og med lengda av alternativ i lista alt.
            questions_str += f'{i + 1}. {self.alt[i]} \n'

        return f'{self.question} \n{questions_str}'


def les_fil():
    with open('sporsmaalsfil.txt') as sporsmaal:
        liste_retur = []
        for linje in sporsmaal:
            sporsmaal_liste = ''

            sporsmaal_split = linje.split(':')
            sporsmaal_liste = sporsmaal_split
            sporsmaal_liste[2] = sporsmaal_liste[2].strip()[1:-1].split(', ')
            liste_retur.append(Question(sporsmaal_liste[0],sporsmaal_liste[1],sporsmaal_liste[2]))
        return  liste_retur




if __name__ == "__main__":

    poeng_1 = 0
    poeng_2 = 0

    for i in les_fil():

        print(i) # printar spørsmål og alternativ, synar __str__
        inn_1 = input('Svar frå spiller 1: ') # tek inn svar frå spiller 1
        inn_2 = input('Svar frå spiller 2: ') # tek inn svar frå spiller 2


        correct_1 = i.sjekk_svar(int(inn_1)) # sendar svar frå spiller 1 til def sjekk_svar
        correct_2 = i.sjekk_svar(int(inn_2)) # sendar svar frå spiller 2 til def sjekk_svar

        print('Spiller 1: '+ ('Riktig svar!' if correct_1 else 'Feil svar')) #printar ut om svaret var rett eller feil, dersom correct_1 er True blir if utførst og 'Riktig svar' printa
        if correct_1 == True:
            poeng_1 += 1
        print('Spiller 2: '+ ('Riktig svar!' if correct_2 else 'Feil svar'))
        if correct_2 == True:
            poeng_2 += 1
        i.korrekt_svar_tekst # hentar korrekt_svar_tekst, tek ikkje argument fordi den finn dei via self.
        


