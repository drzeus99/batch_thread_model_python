if __name__ == "__main__":
	from stats import prob_thread_locking_on_batch
	#from pylab import *
	threads = range(2,17)
	batches = range(50, 151, 4)

	results = {}
	for thread in threads:
		results[thread] = []
#62 min 22.1 sec pbo
#66 min 24.4 sec pbo modded
#68 min 7.5 sec pbo
	from multiprocessing import Pool
	p = Pool(24)

	for thread in threads:
		for batch in batches:
			results[thread].append(p.apply_async(prob_thread_locking_on_batch, (batch, thread)))
	for thread in threads:
		for i in range(len(results[thread])):
			print ("retrieving thread", thread, "batch", batches[i])
			results[thread][i] = results[thread][i].get() * 100.0

	#for i in range(0, len(threads)/2):
         #       semilogy(batches, results[threads[i]], label=str(threads[i]) + " threads")
	#xlabel("number of batches")
	#ylabel("percent chance of thread blocking")
	#legend(loc=1)
	#grid(True, which='both')
	#savefig("threading_model_low.pdf")
	#figure()


	#for i in range(len(threads)/2, len(threads)):
	 #       semilogy(batches, results[threads[i]], label=str(threads[i]) + " threads")
	#xlabel("number of batches")
	#ylabel("percent chance of thread blocking")
	#legend(loc=1)
	#grid(True, which='both')
	#columns=('number of batches', str(thread))
	#table_values=[]
	#for i in range(len(batches)):
	#	row = [batches[i]]
	#	row.append(results[2][i])
	#	table_values.append(row)
	#table(cellText=table_values, cellLoc='center', colLabels=columns)
	#savefig("threading_model_high.pdf")
	#show()
