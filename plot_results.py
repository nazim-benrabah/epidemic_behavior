
import numpy as np
from subprocess import run
import pandas as pd
from pandas import *
from numpy import *
from matplotlib import pyplot


nb_noeuds=60
nb_snapshots=100
nb_simulations=100
period_snapshot=10
width=500
height=500

nb_infected=[2,8,16,40]	#varier le parametre de nombre d'infectés initialement
duree_infection=[60,70,90,120]  #varier le parametre de la durée d'infection
travel_distances=[210,240,270,280]  #varier le parametre du rayon de mobilité
contagion_periods=[210,240,270,280] #Varier la durée de contamination
immune_periods=[310,320,380,470] #varier la periode d'immunité
number_of_nodes=[60,70,90,120] # varier la densité de population en faisant varier le nombre de noeuds
PopDensities=[n/(height*width) for n in number_of_nodes]


data = pd.read_csv('duree_epidemie_en_fonction_densité_population.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:

	df[0].plot(label='Densité= '+str(PopDensities[0]))
	df[1].plot(label='Densité= '+str(PopDensities[1]))
	df[2].plot(label='Densité= '+str(PopDensities[2]))
	df[3].plot(label='Densité= '+str(PopDensities[3]))
	
	mean = df.mean(1)
	error = df.std(1) / sqrt(100)
	mean.plot(label='mean')
	pyplot.fill_between(df.index, mean-error, mean+error,
	alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

	pyplot.title("Impact de la densité de population sur la durée de l'épidémie")
	pyplot.xlabel('Samples')
	pyplot.ylabel("Durée de l'épidémie")
	pyplot.legend()
	pyplot.show()

except Exception as e:
	raise e




data = pd.read_csv('duree_epidemie_en_fonction_duree_contagiosite.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:

	df[0].plot(label='Durée contagiosité= '+str(contagion_periods[0]))
	df[1].plot(label='Durée contagiosité= '+str(contagion_periods[1]))
	df[2].plot(label='Durée contagiosité= '+str(contagion_periods[2]))
	df[3].plot(label='Durée contagiosité= '+str(contagion_periods[3]))
	
	mean = df.mean(1)
	error = df.std(1) / sqrt(nb_simulations)
	mean.plot(label='mean')
	pyplot.fill_between(df.index, mean-error, mean+error,
	alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

	pyplot.title("Impact de la durée de contagiosité sur la durée de l'épidémie")
	pyplot.xlabel('Samples')
	pyplot.ylabel("Durée de l'épidémie")
	pyplot.legend()
	pyplot.show()

except Exception as e:
	raise e



data = pd.read_csv('duree_epidemie_en_fonction_duree_immunite.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:

	df[0].plot(label='Durée immunité= '+str(immune_periods[0]))
	df[1].plot(label='Durée immunité= '+str(immune_periods[1]))
	df[2].plot(label='Durée immunité= '+str(immune_periods[2]))
	df[3].plot(label='Durée immunité= '+str(immune_periods[3]))
	
	mean = df.mean(1)
	error = df.std(1) / sqrt(nb_simulations)
	mean.plot(label='mean')
	pyplot.fill_between(df.index, mean-error, mean+error,
	alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

	pyplot.title("Impact de la durée d'immunité sur la durée de l'épidémie")
	pyplot.xlabel('Samples')
	pyplot.ylabel("Durée de l'épidémie")
	pyplot.legend()
	pyplot.show()

except Exception as e:
	raise e



data = pd.read_csv('duree_epidemie_en_fonction_duree_infection.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:

	df[0].plot(label='Durée infection= '+str(duree_infection[0]))
	df[1].plot(label='Durée infection= '+str(duree_infection[1]))
	df[2].plot(label='Durée infection= '+str(duree_infection[2]))
	df[3].plot(label='Durée infection= '+str(duree_infection[3]))
	
	
	mean = df.mean(1)
	error = df.std(1) / sqrt(nb_simulations)
	mean.plot(label='mean')
	pyplot.fill_between(df.index, mean-error, mean+error,
	alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

	pyplot.title("Impact de la durée d'infection sur la durée de l'épidémie")
	pyplot.xlabel('Samples')
	pyplot.ylabel("Durée de l'épidémie")
	pyplot.legend()
	pyplot.show()

except Exception as e:
	raise e


data = pd.read_csv('duree_epidemie_en_fonction_nb_initial_infectes.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:

	df[0].plot(label='Initialement infectés= '+str(nb_infected[0]))
	df[1].plot(label='Initialement infectés= '+str(nb_infected[1]))
	df[2].plot(label='Initialement infectés= '+str(nb_infected[2]))
	df[3].plot(label='Initialement infectés= '+str(nb_infected[3]))
	
	mean = df.mean(1)
	error = df.std(1) / sqrt(nb_simulations)
	mean.plot(label='mean')
	pyplot.fill_between(df.index, mean-error, mean+error,
	alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

	pyplot.title("Impact du nombre initial d'infectés sur la durée de l'épidémie")
	pyplot.xlabel('Samples')
	pyplot.ylabel("Durée de l'épidémie")
	pyplot.legend()
	pyplot.show()

except Exception as e:
	raise e



data = pd.read_csv('duree_epidemie_en_fonction_rayon_mobilité.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:

	df[0].plot(label='Rayon de mobilité= '+str(travel_distances[0]))
	df[1].plot(label='Rayon de mobilité= '+str(travel_distances[1]))
	df[2].plot(label='Rayon de mobilité= '+str(travel_distances[2]))
	df[3].plot(label='Rayon de mobilité= '+str(travel_distances[3]))
	
	mean = df.mean(1)
	error = df.std(1) / sqrt(nb_simulations)
	mean.plot(label='mean')
	pyplot.fill_between(df.index, mean-error, mean+error,
	alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

	pyplot.title("Impact du rayon de mobilité sur la durée de l'épidémie")
	pyplot.xlabel('Samples')
	pyplot.ylabel("Durée de l'épidémie")
	pyplot.legend()
	pyplot.show()

except Exception as e:
	raise e


##################################################################################################################



data = pd.read_csv('multi_infectes_en_fonction_densité_population.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:

	pyplot.hist([df[0],df[1],df[2],df[3]],label=['Densité= '+str(PopDensities[0]),'Densité= '+str(PopDensities[1]),'Densité= '+str(PopDensities[2]),'Densité= '+str(PopDensities[3])],bins=40)
	pyplot.axvline(x=df[0].mean(),linestyle='--',label='Mean at Densité= '+str(PopDensities[0]))
	pyplot.axvline(x=df[1].mean(),color='orange',linestyle='--',label='Mean at Densité= '+str(PopDensities[1]))
	pyplot.axvline(x=df[2].mean(),color='g',linestyle='--',label='Mean at Densité= '+str(PopDensities[2]))
	pyplot.axvline(x=df[3].mean(),color='r',linestyle='--',label='Mean at Densité= '+str(PopDensities[3]))
	pyplot.title("Impact de la densité de population sur la distribution des multi-infectés")
	pyplot.xlabel('Nombre de multi infection')
	pyplot.ylabel("Fréquence")
	pyplot.xticks(np.arange(0, 121, 10))
	pyplot.legend()
	pyplot.show()

except Exception as e:
	raise e

data = pd.read_csv('multi_infectes_en_fonction_duree_contagiosite.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:
        pyplot.hist([df[0],df[1],df[2],df[3]],label=['Durée contagiosité= '+str(contagion_periods[0]),'Durée contagiosité= '+str(contagion_periods[1]),'Durée contagiosité= '+str(contagion_periods[2]),'Durée contagiosité= '+str(contagion_periods[3])],bins=20)
        pyplot.axvline(x=df[0].mean(),linestyle='--',label='Mean at Durée contagiosité= '+str(contagion_periods[0]))
        pyplot.axvline(x=df[1].mean(),color='orange',linestyle='--',label='Mean at Durée contagiosité= '+str(contagion_periods[1]))
        pyplot.axvline(x=df[2].mean(),color='g',linestyle='--',label='Mean at Durée contagiosité= '+str(contagion_periods[2]))
        pyplot.axvline(x=df[3].mean(),color='r',linestyle='--',label='Mean at Durée contagiosité= '+str(contagion_periods[3]))
        pyplot.title("Impact de la durée de contagiosité sur la distribution des multi-infectés")
        pyplot.xlabel('Nombre de multi infection')
        pyplot.ylabel("Fréquence")
        pyplot.legend()
        pyplot.show()

except Exception as e:
	raise e



data = pd.read_csv('multi_infectes_en_fonction_duree_immunite.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:
        pyplot.hist([df[0],df[1],df[2],df[3]],label=['Durée immunité= '+str(immune_periods[0]),'Durée immunité= '+str(immune_periods[1]),'Durée immunité= '+str(immune_periods[2]),'Durée immunité= '+str(immune_periods[3])],bins=20)
        pyplot.axvline(x=df[0].mean(),linestyle='--',label='Mean at Durée immunité= '+str(immune_periods[0]))
        pyplot.axvline(x=df[1].mean(),color='orange',linestyle='--',label='Mean at Durée immunité= '+str(immune_periods[1]))
        pyplot.axvline(x=df[2].mean(),color='g',linestyle='--',label='Mean at Durée immunité= '+str(immune_periods[2]))
        pyplot.axvline(x=df[3].mean(),color='r',linestyle='--',label='Mean at Durée immunité= '+str(immune_periods[3]))
        pyplot.title("Impact de la durée d'immunité sur la distribution des multi-infectés")
        pyplot.xlabel('Nombre de multi infection')
        pyplot.ylabel("Fréquence")
        pyplot.legend()
        pyplot.show()

except Exception as e:
	raise e


data = pd.read_csv('multi_infectes_en_fonction_duree_infection.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:
        pyplot.hist([df[0],df[1],df[2],df[3]],label=['Durée infection= '+str(duree_infection[0]),'Durée infection= '+str(duree_infection[1]),'Durée infection= '+str(duree_infection[2]),'Durée infection= '+str(duree_infection[3])],bins=20)
        pyplot.axvline(x=df[0].mean(),linestyle='--',label='Mean at Durée infection= '+str(duree_infection[0]))
        pyplot.axvline(x=df[1].mean(),color='orange',linestyle='--',label='Mean at Durée infection= '+str(duree_infection[1]))
        pyplot.axvline(x=df[2].mean(),color='g',linestyle='--',label='Mean at Durée infection= '+str(duree_infection[2]))
        pyplot.axvline(x=df[3].mean(),color='r',linestyle='--',label='Mean at Durée infection= '+str(duree_infection[3]))
        pyplot.title("Impact de la durée d'infection sur la distribution des multi-infectés")
        pyplot.xlabel('Nombre de multi infection')
        pyplot.ylabel("Fréquence")
        pyplot.legend()
        pyplot.show()

except Exception as e:
	raise e


data = pd.read_csv('multi_infectes_en_fonction_nb_initial_infectes.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:

	pyplot.hist([df[0],df[1],df[2],df[3]],label=['Initialement infectés= '+str(nb_infected[0]),'Initialement infectés= '+str(nb_infected[1]),'Initialement infectés= '+str(nb_infected[2]),'Initialement infectés= '+str(nb_infected[3])],bins=20)
	pyplot.axvline(x=df[0].mean(),linestyle='--',label='Mean at Initialement infectés= '+str(nb_infected[0]))
	pyplot.axvline(x=df[1].mean(),color='orange',linestyle='--',label='Mean at Initialement infectés= '+str(nb_infected[1]))
	pyplot.axvline(x=df[2].mean(),color='g',linestyle='--',label='Mean at Initialement infectés= '+str(nb_infected[2]))
	pyplot.axvline(x=df[3].mean(),color='r',linestyle='--',label='Mean at Initialement infectés= '+str(nb_infected[3]))
	pyplot.title("Impact du nombre initial d'infectés sur la distribution des multi-infectés")
	pyplot.xlabel('Nombre de multi infection')
	pyplot.ylabel("Fréquence")
	pyplot.legend()
	pyplot.show()

except Exception as e:
	raise e


data = pd.read_csv('multi_infectes_en_fonction_rayon_mobilité.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:
        pyplot.hist([df[0],df[1],df[2],df[3]],label=['Rayon de mobilité= '+str(travel_distances[0]),'Rayon de mobilité= '+str(travel_distances[1]),'Rayon de mobilité= '+str(travel_distances[2]),'Rayon de mobilité= '+str(travel_distances[3])],bins=20)
        pyplot.axvline(x=df[0].mean(),linestyle='--',label='Mean at Rayon de mobilité= '+str(travel_distances[0]))
        pyplot.axvline(x=df[1].mean(),color='orange',linestyle='--',label='Mean at Rayon de mobilité= '+str(travel_distances[1]))
        pyplot.axvline(x=df[2].mean(),color='g',linestyle='--',label='Mean at Rayon de mobilité= '+str(travel_distances[2]))
        pyplot.axvline(x=df[3].mean(),color='r',linestyle='--',label='Mean at Rayon de mobilité= '+str(travel_distances[3]))
        pyplot.title("Impact du rayon de mobilité sur la distribution des multi-infectés")
        pyplot.xlabel('Nombre de multi infection')
        pyplot.ylabel("Fréquence")
        pyplot.legend()
        pyplot.show()

except Exception as e:
	raise e

#################################################################################################################
data = pd.read_csv('prop_infectes_en_fonction_densité_population.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:
        
	df[0].plot(label='Densité= '+str(PopDensities[0]))
	df[1].plot(label='Densité= '+str(PopDensities[1]))
	df[2].plot(label='Densité= '+str(PopDensities[2]))
	df[3].plot(label='Densité= '+str(PopDensities[3]))
	
	
	mean = df.mean(1)
	error = df.std(1) / sqrt(100)
	mean.plot(label='mean')
	pyplot.fill_between(df.index, mean-error, mean+error,
	alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

	pyplot.title("Impact de la densité de population sur la proportion de la population infectée ")
	pyplot.xlabel('Samples')
	pyplot.ylabel("Proportion de la population infectée")
	pyplot.legend()
	pyplot.show()

except Exception as e:
	raise e


data = pd.read_csv('prop_infectes_en_fonction_duree_contagiosite.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:

	df[0].plot(label='Durée contagiosité= '+str(contagion_periods[0]))
	df[1].plot(label='Durée contagiosité= '+str(contagion_periods[1]))
	df[2].plot(label='Durée contagiosité= '+str(contagion_periods[2]))
	df[3].plot(label='Durée contagiosité= '+str(contagion_periods[3]))
	mean = df.mean(1)
	error = df.std(1) / sqrt(nb_simulations)
	mean.plot(label='mean')
	pyplot.fill_between(df.index, mean-error, mean+error,
	alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

	pyplot.title("Impact de la durée de contagiosité sur la proportion de la population infectée")
	pyplot.xlabel('Samples')
	pyplot.ylabel("Proportion de la population infectée")
	pyplot.legend()
	pyplot.show()

except Exception as e:
	raise e



data = pd.read_csv('prop_infectes_en_fonction_duree_immunite.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:

	df[0].plot(label='Durée immunité= '+str(immune_periods[0]))
	df[1].plot(label='Durée immunité= '+str(immune_periods[1]))
	df[2].plot(label='Durée immunité= '+str(immune_periods[2]))
	df[3].plot(label='Durée immunité= '+str(immune_periods[3]))
	mean = df.mean(1)
	error = df.std(1) / sqrt(nb_simulations)
	mean.plot(label='mean')
	pyplot.fill_between(df.index, mean-error, mean+error,
	alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

	pyplot.title("Impact de la durée d'immunité sur la proportion de la population infectée")
	pyplot.xlabel('Samples')
	pyplot.ylabel("Proportion de la population infectée")
	pyplot.legend()
	pyplot.show()

except Exception as e:
	raise e



data = pd.read_csv('prop_infectes_en_fonction_duree_infection.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:

	df[0].plot(label='Durée infection= '+str(duree_infection[0]))
	df[1].plot(label='Durée infection= '+str(duree_infection[1]))
	df[2].plot(label='Durée infection= '+str(duree_infection[2]))
	df[3].plot(label='Durée infection= '+str(duree_infection[3]))
	mean = df.mean(1)
	error = df.std(1) / sqrt(nb_simulations)
	mean.plot(label='mean')
	pyplot.fill_between(df.index, mean-error, mean+error,
	alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

	pyplot.title("Impact de la durée d'infection sur la proportion de la population infectée")
	pyplot.xlabel('Samples')
	pyplot.ylabel("Proportion de la population infectée")
	pyplot.legend()
	pyplot.show()

except Exception as e:
	raise e



data = pd.read_csv('prop_infectes_en_fonction_nb_initial_infectes.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:

	df[0].plot(label='Initialement infectés= '+str(nb_infected[0]))
	df[1].plot(label='Initialement infectés= '+str(nb_infected[1]))
	df[2].plot(label='Initialement infectés= '+str(nb_infected[2]))
	df[3].plot(label='Initialement infectés= '+str(nb_infected[3]))
	mean = df.mean(1)
	error = df.std(1) / sqrt(nb_simulations)
	mean.plot(label='mean')
	pyplot.fill_between(df.index, mean-error, mean+error,
	alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

	pyplot.title("Impact du nombre initial d'infectés sur la proportion de la population infectée")
	pyplot.xlabel('Samples')
	pyplot.ylabel("Proportion de la population infectée")
	pyplot.legend()
	pyplot.show()

except Exception as e:
	raise e



data = pd.read_csv('prop_infectes_en_fonction_rayon_mobilité.txt', header = None, sep=' ') ##charger un fichier
df=DataFrame(data)


try:

	df[0].plot(label='Rayon de mobilité= '+str(travel_distances[0]))
	df[1].plot(label='Rayon de mobilité= '+str(travel_distances[1]))
	df[2].plot(label='Rayon de mobilité= '+str(travel_distances[2]))
	df[3].plot(label='Rayon de mobilité= '+str(travel_distances[3]))
	mean = df.mean(1)
	error = df.std(1) / sqrt(nb_simulations)
	mean.plot(label='mean')
	pyplot.fill_between(df.index, mean-error, mean+error,
	alpha=0.5, edgecolor='#CC4F1B', facecolor='#FF9848')

	pyplot.title("Impact du rayon de mobilité sur la proportion de la population infectée")
	pyplot.xlabel('Samples')
	pyplot.ylabel("Proportion de la population infectée")
	pyplot.legend()
	pyplot.show()

except Exception as e:
	raise e


# data = pd.read_csv('multi_infectes_en_fonction_duree_infection.txt', header = None, sep=' ') ##charger un fichier
# df=DataFrame(data)

# pyplot.pcolor(df)
# pyplot.show()




