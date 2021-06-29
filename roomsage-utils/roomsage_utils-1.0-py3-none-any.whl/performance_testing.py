import pandas as pd
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from collections import defaultdict


if __name__ == "__main__":

	df = pd.DataFrame({'col_name': np.random.randint(low=0, high=100, size=1000)})
	columns = list(df.columns)
	alpha = 0.01
	timer_dict = defaultdict(list)

	for i in range(0, len(df)-180):
		
		start_time = timer()
		data = df.iloc[i:180+i, :].copy()
		timer_dict['code_1'].append(timer() - start_time)
		
		start_time = timer()
		data.reset_index(inplace=True, drop=True)
		timer_dict['code_2'].append(timer() - start_time)

		for column in columns:
			smoothed_column = column + ".smoothed"
			
			start_time = timer()
			vec = np.zeros([data.shape[0]])
			timer_dict['code_3'].append(timer() - start_time)
			
			start_time = timer()
			vec[0] = data[column].values[0]
			timer_dict['code_4'].append(timer() - start_time)

			start_time = timer()
			original = data[column].values
			timer_dict['code_5'].append(timer() - start_time)

			start_time = timer()
			for idx in range(1, len(vec)):
				vec[idx] = alpha * original[idx] + (1 - alpha) * vec[idx - 1]
			timer_dict['code_6'].append(timer() - start_time)

			start_time = timer()
			data[smoothed_column] = vec
			timer_dict['code_7'].append(timer() - start_time)

	print("Finish!")

	plot_df = pd.DataFrame(timer_dict)

	plot_df.plot(subplots=True, figsize=(15, 10))

	plt.show()

	# plt.savefig("result.png", bbox_inches='tight')
	# plt.close()
