from subprocess import run




##################################################################### EXERCICE 1 ##############################################################################



FileName='Virus_old.jar' ### Il y'a deux versions du fichier .jar  (Virus.jar ou Virus_old.jar)

nb_simulation=100 #nombre de simulations

nb_snapshots=100 #nombre de snapshots par simulation

nodes=60 #Nombre de noeuds

height=500

width=500

stop_all_sane=0


nb_infected=[2,4,8,16,20,30,40,45]	#varier le parametre de nombre d'infectés initialement
duree_infection=range(60,140,10)  #varier le parametre de la durée d'infection
travel_distances=[210,220,230,240,250,260,270,280]  #varier le parametre du rayon de mobilité
contagion_periods=[210,220,230,240,250,260,270,280] #Varier la durée de contamination
immune_periods=[310,320,340,360,380,390,430,470] #varier la periode d'immunité
nb_nodes=range(60,140,10) # varier la densité de population en faisant varier le nombre de noeuds



import time
start_time = time.time()

print('Running with \n',nb_simulation,' simulations with ',nb_snapshots,' snapshots per simulation \n height and width= ',height, width,'\n stop_all_sane= ',stop_all_sane)


# ###### Question 1 ####### Exectuer le simulateur nb_simulation fois avec des parametres fixes (par défaut), stocker le resultat dans un fichier txt unique


with open('res_fixed_parameter_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulation)+'.txt','w') as f:
	for i in range (nb_simulation):
		res =run(['java','-jar', FileName,'-gui=0','-nb_snapshots='+str(nb_snapshots),'-show_parameters=0','-nb_nodes='+str(nodes),'-stop_all_sane='+str(stop_all_sane),'-height='+str(height),'-width='+str(width),'-printout=2'], capture_output=True)
		f.write(res.stdout.decode('utf-8'))

	print("--- %s seconds ---" % (time.time() - start_time)) ## pour voir en combien de temps le fichier est généré

##### Question 2.1 ###### Exectuer le simulateur nb_simulation fois en faisant varier le parametre nb_infected, stocker le resultat dans un fichier txt




for nb in nb_infected:
	with open('res_nb_infected='+str(nb)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulation)+'.txt','w') as f:
		for i in range (nb_simulation):
			res2 =run(['java','-jar', FileName,'-gui=0','-nb_snapshots='+str(nb_snapshots),'-show_parameters=0','-nb_infected='+str(nb),'-nb_nodes='+str(nodes),'-stop_all_sane='+str(stop_all_sane),'-height='+str(height),'-width='+str(width),'-printout=2'], capture_output=True)

			f.write(res2.stdout.decode('utf-8'))
		print("--- %s seconds ---" % (time.time() - start_time))


# ###### Question 2.2 ###### Exectuer le simulateur nb_simulation fois en faisant varier le parametre infection_period, stocker le resultat dans un fichier txt




for d in duree_infection:
	with open('res_InfectionPeriod='+str(d)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulation)+'.txt','w') as f:
		for i in range (nb_simulation):
			res3 =run(['java','-jar', FileName,'-gui=0','-nb_snapshots='+str(nb_snapshots),'-show_parameters=0','-infection_period='+str(d),'-nb_nodes='+str(nodes),'-stop_all_sane='+str(stop_all_sane),'-height='+str(height),'-width='+str(width),'-printout=2'], capture_output=True)

			f.write(res3.stdout.decode('utf-8'))
		print("--- %s seconds ---" % (time.time() - start_time))


###### Question 2.3 ###### Exectuer le simulateur nb_simulation fois en faisant varier le parametre travel_distance, stocker le resultat dans un fichier txt




for td in travel_distances:
	with open('res_TravelDistance='+str(td)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulation)+'.txt','w') as f:
		for i in range (nb_simulation):
			res4 =run(['java','-jar', FileName,'-gui=0','-nb_snapshots='+str(nb_snapshots),'-show_parameters=0','-travel_distance='+str(td),'-nb_nodes='+str(nodes),'-stop_all_sane='+str(stop_all_sane),'-height='+str(height),'-width='+str(width),'-printout=2'], capture_output=True)

			f.write(res4.stdout.decode('utf-8'))
		print("--- %s seconds ---" % (time.time() - start_time))



###### Question 2.4 ###### Exectuer le simulateur nb_simulation fois en faisant varier le parametre contagion_period, stocker le resultat dans un fichier txt



for cp in contagion_periods:
	with open('res_ContagionPeriod='+str(cp)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulation)+'.txt','w') as f:
		for i in range (nb_simulation):
			res5 =run(['java','-jar', FileName,'-gui=0','-nb_snapshots='+str(nb_snapshots),'-show_parameters=0','-contagion_period='+str(cp),'-nb_nodes='+str(nodes),'-stop_all_sane='+str(stop_all_sane),'-height='+str(height),'-width='+str(width),'-printout=2'], capture_output=True)

			f.write(res5.stdout.decode('utf-8'))
	print('done')
	print("--- %s seconds ---" % (time.time() - start_time))



###### Question 2.5 ###### Exectuer le simulateur nb_simulation fois en faisant varier le parametre immune_period, stocker le resultat dans un fichier txt



for ip in immune_periods:
	with open('res_ImmunePeriod='+str(ip)+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulation)+'.txt','w') as f:
		for i in range (nb_simulation):
			res6 =run(['java','-jar', FileName,'-gui=0','-nb_snapshots='+str(nb_snapshots),'-show_parameters=0','-immune_period='+str(ip),'-nb_nodes='+str(nodes),'-stop_all_sane='+str(stop_all_sane),'-height='+str(height),'-width='+str(width),'-printout=2'], capture_output=True)

			f.write(res6.stdout.decode('utf-8'))
	print('done')
	print("--- %s seconds ---" % (time.time() - start_time))


###### Question 2.6 ###### Exectuer le simulateur nb_simulation fois en faisant varier le parametre nb_nodes, stocker le resultat dans un fichier txt



for n in nb_nodes:
	with open('res_PopDensity='+str(n/(width*height))+'_nbSnapshots='+str(nb_snapshots)+'_nbSimulations='+str(nb_simulation)+'.txt','w') as f:
		for i in range (nb_simulation):
			res7 =run(['java','-jar', FileName,'-gui=0','-nb_snapshots='+str(nb_snapshots),'-show_parameters=0','-nb_nodes='+str(n),'-stop_all_sane='+str(stop_all_sane),'-height='+str(height),'-width='+str(width),'-printout=2'], capture_output=True)

			f.write(res7.stdout.decode('utf-8'))
	print('done')


	print("--- %s seconds ---" % (time.time() - start_time))




