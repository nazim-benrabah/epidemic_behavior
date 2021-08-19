
import numpy as np
from subprocess import run
import pandas as pd
from pandas import *
from numpy import *


nb_noeuds=60
nb_snapshots=100
nb_simulations=100
period_snapshot=10
width=500
height=500



###varier les parametres 
nb_infected=[2,8,16,40]	#varier le parametre de nombre d'infectés initialement
duree_infection=[60,70,90,120]  #varier le parametre de la durée d'infection
travel_distances=[210,240,270,280]  #varier le parametre du rayon de mobilité
contagion_periods=[210,240,270,280]#Varier la durée de contamination
immune_periods=[310,320,380,470] #varier la periode d'immunité
number_of_nodes=[60,70,90,120] # varier la densité de population en faisant varier le nombre de noeuds

PopDensities=[n/(height*width) for n in number_of_nodes]

print("\nProcessing...")


def duree_epidemie(filename,nb_noeuds,nb_snapshots,nb_simulations,period_snapshot):

	data = pd.read_csv(filename, header = None, sep=' ') ##charger un fichier
	d=DataFrame(data) ## creer dataframe
	del d[nb_noeuds] ## supprimer la derniere colonnes car elle affiche toujours un NAN (correspond à un 'espace')
	j=0
	duree_epidemie=[] ## initialiser une liste qui contient les durée de l'épidémie pour chaque simulation

	for j in range(0,len(d),nb_snapshots):
		k=0

		for i in range(j,nb_snapshots+j):
			k=k+1
			if list(d.loc[i]) ==[0]*nb_noeuds:
				#print("l'epidémie s'est arretée à la ligne ",(i+1)-j,' de la simulation ',int(j/nb_snapshots+1),' Elle a duré ',((i+1)-j)*period_snapshot,' time unit')
				duree_epidemie.append(((i+1)-j)*period_snapshot)
				break
			else:
				if k==nb_snapshots:
					duree_epidemie.append(np.nan)
					break

	return duree_epidemie


def proportion_infectes(filename,nb_noeuds,nb_snapshots,nb_simulations):

	data=pd.read_csv(filename,header=None,sep=' ')
	d=pd.DataFrame(data)
	del d[nb_noeuds]

	sim=[]

	for i in range(nb_simulations):

	     list_infected=[]

	     for j in range(nb_noeuds):
	       if d.loc[nb_snapshots*i:nb_snapshots*i+nb_snapshots-1,j].isin([1]).any():
	           if j not in list_infected:
	              list_infected.append(j)

	     sim.append((len(list_infected)/nb_noeuds)*100)

	return sim


def multi_infection(filename,nb_noeuds,nb_snapshots,nb_simulations):

	data=pd.read_csv(filename,header=None,sep=' ')
	d=pd.DataFrame(data)
	del d[nb_noeuds]       
	sim=[]
	for i in range(nb_simulations):
	     list_infected=[]
	     for j in range(nb_noeuds):
	       multiple=None
	       for k in list(d.loc[nb_snapshots*i:nb_snapshots*i+nb_snapshots-1,j].isin([1])):
	          if k and multiple is None:
	             multiple=0
	          elif k==False and multiple==0:
	             multiple=1
	          elif k and multiple==1:
	             multiple=2
	       if multiple==2:
	          list_infected.append(j)
	     sim.append(len(list_infected))
	return sim



############################################################# Impact de la durée de contagiosité #################################################

durée_épidémie=[]
for c in contagion_periods:

	durée_épidémie.append(duree_epidemie('res_ContagionPeriod='+str(c)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations,period_snapshot))


df_contagion_period_duree = pd.DataFrame({contagion_periods[0]: durée_épidémie[0],
									contagion_periods[1]: durée_épidémie[1],
									contagion_periods[2]: durée_épidémie[2],
									contagion_periods[3]: durée_épidémie[3],})

df_contagion_period_duree.to_csv('duree_epidemie_en_fonction_duree_contagiosite.txt', header=None, index=None, sep=' ', mode='a')
print("\n ######### Impact de durée de contagiosité sur la durée de l'épidémie ############\n")
print(df_contagion_period_duree)



prop_max=[]

for c in contagion_periods:

	prop_max.append(proportion_infectes('res_ContagionPeriod='+str(c)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations))


df_contagion_period_prop = pd.DataFrame({contagion_periods[0]: prop_max[0],
									contagion_periods[1]: prop_max[1],
									contagion_periods[2]: prop_max[2],
									contagion_periods[3]: prop_max[3],})

df_contagion_period_prop.to_csv('prop_infectes_en_fonction_duree_contagiosite.txt', header=None, index=None, sep=' ')
print("\n ######### Impact de durée de contagiosité sur la proportion de la population infectée ############\n")
print(df_contagion_period_prop)





multiinfection=[]
for c in contagion_periods:

	multiinfection.append(multi_infection('res_ContagionPeriod='+str(c)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations))


df_contagion_period_multi = pd.DataFrame({contagion_periods[0]: multiinfection[0],
									contagion_periods[1]: multiinfection[1],
									contagion_periods[2]: multiinfection[2],
									contagion_periods[3]: multiinfection[3],})


df_contagion_period_multi.to_csv('multi_infectes_en_fonction_duree_contagiosite.txt', header=None, index=None, sep=' ')
print("\n ######### Impact de durée de contagiosité sur la distribution des multi-infections ############\n")
print(df_contagion_period_multi)

############################################################# Impact du nombre initial d'infectés #################################################


durée_épidémie=[]
for ni in nb_infected:

	durée_épidémie.append(duree_epidemie('res_nb_infected='+str(ni)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations,period_snapshot))


df_nb_infected_duree = pd.DataFrame({nb_infected[0]: durée_épidémie[0],
									nb_infected[1]: durée_épidémie[1],
									nb_infected[2]: durée_épidémie[2],
									nb_infected[3]: durée_épidémie[3],})

df_nb_infected_duree.to_csv('duree_epidemie_en_fonction_nb_initial_infectes.txt', header=None, index=None, sep=' ')
print("\n ######### Impact du nombre initial d'infecté sur la durée de l'épidémie ############\n")
print(df_nb_infected_duree)



prop_max=[]

for ni in nb_infected:

	prop_max.append(proportion_infectes('res_nb_infected='+str(ni)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations))


df_nb_infected_prop = pd.DataFrame({nb_infected[0]: prop_max[0],
										nb_infected[1]: prop_max[1],
										nb_infected[2]: prop_max[2],
										nb_infected[3]: prop_max[3],})

df_nb_infected_prop.to_csv('prop_infectes_en_fonction_nb_initial_infectes.txt', header=None, index=None, sep=' ')
print("\n ######### Impact du nombre initial d'infecté sur la proportion de la population infectée ############\n")
print(df_nb_infected_prop)





multiinfection=[]
for ni in nb_infected:

	multiinfection.append(multi_infection('res_nb_infected='+str(ni)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations))


df_nb_infected_multi = pd.DataFrame({nb_infected[0]: multiinfection[0],
									nb_infected[1]: multiinfection[1],
									nb_infected[2]: multiinfection[2],
									nb_infected[3]: multiinfection[3],})


df_nb_infected_multi.to_csv('multi_infectes_en_fonction_nb_initial_infectes.txt', header=None, index=None, sep=' ')
print("\n ######### Impact du nombre initial d'infecté sur la distribution des multi-infections ############\n")
print(df_nb_infected_multi)

# ############################################################# Impact de la duree d'infection #################################################


durée_épidémie=[]
for di in duree_infection:

	durée_épidémie.append(duree_epidemie('res_InfectionPeriod='+str(di)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations,period_snapshot))


df_InfectionPeriod_duree = pd.DataFrame({duree_infection[0]: durée_épidémie[0],
									duree_infection[1]: durée_épidémie[1],
									duree_infection[2]: durée_épidémie[2],
									duree_infection[3]: durée_épidémie[3],})

df_InfectionPeriod_duree.to_csv('duree_epidemie_en_fonction_duree_infection.txt', header=None, index=None, sep=' ')
print("\n ######### Impact de la durée d'infection sur la durée de l'épidémie ############\n")
print(df_InfectionPeriod_duree)



prop_max=[]

for di in duree_infection:

	prop_max.append(proportion_infectes('res_InfectionPeriod='+str(di)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations))


df_InfectionPeriod_prop = pd.DataFrame({duree_infection[0]: prop_max[0],
										duree_infection[1]: prop_max[1],
										duree_infection[2]: prop_max[2],
										duree_infection[3]: prop_max[3],})

df_InfectionPeriod_prop.to_csv('prop_infectes_en_fonction_duree_infection.txt', header=None, index=None, sep=' ')
print("\n ######### Impact de la durée d'infection sur la proportion de la population infectée ############\n")
print(df_InfectionPeriod_prop)




multiinfection=[]
for di in duree_infection:

	multiinfection.append(multi_infection('res_InfectionPeriod='+str(di)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations))


df_InfectionPeriod_multi = pd.DataFrame({duree_infection[0]: multiinfection[0],
									duree_infection[1]: multiinfection[1],
									duree_infection[2]: multiinfection[2],
									duree_infection[3]: multiinfection[3],})


df_InfectionPeriod_multi.to_csv('multi_infectes_en_fonction_duree_infection.txt', header=None, index=None, sep=' ')
print("\n ######### Impact de la durée d'infection sur la distribution des multiinfections ############\n")
print(df_InfectionPeriod_multi)


# ############################################################# Impact du rayon de mobilité #################################################


durée_épidémie=[]
for td in travel_distances:

	durée_épidémie.append(duree_epidemie('res_TravelDistance='+str(td)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations,period_snapshot))


df_TravelDistance_duree = pd.DataFrame({travel_distances[0]: durée_épidémie[0],
									travel_distances[1]: durée_épidémie[1],
									travel_distances[2]: durée_épidémie[2],
									travel_distances[3]: durée_épidémie[3],})

df_TravelDistance_duree.to_csv('duree_epidemie_en_fonction_rayon_mobilité.txt', header=None, index=None, sep=' ')
print("\n ######### Impact du rayon de mobilité sur la durée de l'épidémie ############\n")
print(df_TravelDistance_duree)



prop_max=[]

for td in travel_distances:

	prop_max.append(proportion_infectes('res_TravelDistance='+str(td)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations))


df_TravelDistance_prop = pd.DataFrame({travel_distances[0]: prop_max[0],
										travel_distances[1]: prop_max[1],
										travel_distances[2]: prop_max[2],
										travel_distances[3]: prop_max[3],})

df_TravelDistance_prop.to_csv('prop_infectes_en_fonction_rayon_mobilité.txt', header=None, index=None, sep=' ')
print("\n ######### Impact du rayon de mobilité sur la proportion de la population infectée ############\n")
print(df_TravelDistance_prop)




multiinfection=[]
for td in travel_distances:

	multiinfection.append(multi_infection('res_TravelDistance='+str(td)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations))


df_TravelDistance_multi = pd.DataFrame({travel_distances[0]: multiinfection[0],
									travel_distances[1]: multiinfection[1],
									travel_distances[2]: multiinfection[2],
									travel_distances[3]: multiinfection[3],})


df_TravelDistance_multi.to_csv('multi_infectes_en_fonction_rayon_mobilité.txt', header=None, index=None, sep=' ')
print("\n ######### Impact du rayon de mobilité sur la distribution des multi-infections ############\n")
print(df_TravelDistance_multi)


############################################################# Impact de la duree d'immunité #################################################


durée_épidémie=[]
for ip in immune_periods:

	durée_épidémie.append(duree_epidemie('res_ImmunePeriod='+str(ip)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations,period_snapshot))


df_ImmunePeriod_duree = pd.DataFrame({immune_periods[0]: durée_épidémie[0],
									immune_periods[1]: durée_épidémie[1],
									immune_periods[2]: durée_épidémie[2],
									immune_periods[3]: durée_épidémie[3],})

df_ImmunePeriod_duree.to_csv('duree_epidemie_en_fonction_duree_immunite.txt', header=None, index=None, sep=' ')
print("\n ######### Impact de la durée d'immunité sur la durée de l'épidémie ############\n")
print(df_ImmunePeriod_duree)



prop_max=[]

for ip in immune_periods:

	prop_max.append(proportion_infectes('res_ImmunePeriod='+str(ip)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations))


df_ImmunePeriod_prop = pd.DataFrame({immune_periods[0]: prop_max[0],
										immune_periods[1]: prop_max[1],
										immune_periods[2]: prop_max[2],
										immune_periods[3]: prop_max[3],})

df_ImmunePeriod_prop.to_csv('prop_infectes_en_fonction_duree_immunite.txt', header=None, index=None, sep=' ')
print("\n ######### Impact de la durée d'immunité sur la proportion de la population infectée ############\n")
print(df_ImmunePeriod_prop)




multiinfection=[]
for ip in immune_periods:

	multiinfection.append(multi_infection('res_ImmunePeriod='+str(ip)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',nb_noeuds,nb_snapshots,nb_simulations))


df_ImmunePeriod_multi = pd.DataFrame({immune_periods[0]: multiinfection[0],
									immune_periods[1]: multiinfection[1],
									immune_periods[2]: multiinfection[2],
									immune_periods[3]: multiinfection[3],})


df_ImmunePeriod_multi.to_csv('multi_infectes_en_fonction_duree_immunite.txt', header=None, index=None, sep=' ')
print("\n ######### Impact de la durée d'immunité sur la distribution des multi-infections ############\n")
print(df_ImmunePeriod_multi)



# ############################################################# Impact de la densité de population #################################################


durée_épidémie=[]

for n in number_of_nodes:
	durée_épidémie.append(duree_epidemie('res_PopDensity='+str(n/(height*width))+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',n,nb_snapshots,nb_simulations,period_snapshot))


df_PopDensity_duree = pd.DataFrame({PopDensities[0]: durée_épidémie[0],
									PopDensities[1]: durée_épidémie[1],
									PopDensities[2]: durée_épidémie[2],
									PopDensities[3]: durée_épidémie[3]})

df_PopDensity_duree.to_csv('duree_epidemie_en_fonction_densité_population.txt', header=None, index=None, sep=' ')
print("\n ######### Impact de la densitée de population sur la durée de l'épidémie ############\n")
print(df_PopDensity_duree)



prop_max=[]

for n in number_of_nodes:

	prop_max.append(proportion_infectes('res_PopDensity='+str(n/(height*width))+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',n,nb_snapshots,nb_simulations))


df_PopDensity_prop = pd.DataFrame({PopDensities[0]: prop_max[0],
										PopDensities[1]: prop_max[1],
										PopDensities[2]: prop_max[2],
										PopDensities[3]: prop_max[3],})

df_PopDensity_prop.to_csv('prop_infectes_en_fonction_densité_population.txt', header=None, index=None, sep=' ')
print("\n ######### Impact de la densitée de population sur la proportion de la population infectées ############\n")
print(df_PopDensity_prop)




multiinfection=[]
for n in number_of_nodes:

	multiinfection.append(multi_infection('res_PopDensity='+str(n/(height*width))+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulations)+'.txt',n,nb_snapshots,nb_simulations))


df_PopDensity_multi = pd.DataFrame({PopDensities[0]: multiinfection[0],
									PopDensities[1]: multiinfection[1],
									PopDensities[2]: multiinfection[2],
									PopDensities[3]: multiinfection[3],})


df_PopDensity_multi.to_csv('multi_infectes_en_fonction_densité_population.txt', header=None, index=None, sep=' ')
print("\n ######### Impact de la densitée de population sur la distribution des multi-infections ############\n")
print(df_PopDensity_multi)

