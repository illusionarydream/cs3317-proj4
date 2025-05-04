threshold=41

python main.py --mdp blackjack --algorithm value_iteration --card-values 1 2 3 4 5 6 7 8 9 10 --multiplicity 4 --threshold $threshold --peek-cost 1
python main.py --mdp blackjack --algorithm policy_iteration --card-values 1 2 3 4 5 6 7 8 9 10 --multiplicity 4 --threshold $threshold --peek-cost 1