#!/usr/bin/env python


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance. P = V² / R
	return (voltage**2)/resistance

def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	if v1[0]*v2[0] + v1[1]*v2[1]==0:
		return True
	return False


def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	nb_positifs = 0
	somme = 0
	for v in values:  # cannot use sum() pcq cette fonction est réservée aux iterables comme les listes, tuples, strings
		if v >= 0:
			nb_positifs += 1
			somme += v
	return somme / nb_positifs

'''ALTERNATIVE

possible avec sum(v) ? : would need sum(values)/len(values) et des ".remove" pour les <0 et -= pour len(values)

'''

def bills(value):
	pass
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties = tens = fives = ones = 0
	while value != 0:
		if value >= 20:
			twenties +=1
			value -= 20
			continue
		elif value >= 10:
			tens +=1
			value -= 10
			continue
		elif value >= 5:
			fives +=1
			value -= 5
			continue
		elif value >= 1:
			ones += 1
			value -=1
			continue

	return (twenties, tens, fives, ones);

if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
