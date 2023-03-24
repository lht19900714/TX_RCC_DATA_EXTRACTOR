'''
@File   :  gas_disposition_file_oil_parser.py
@Author :  Haitao Lu
@Date   :  25-Mar-2023 3:09 AM
'''

from pathlib import Path
import pandas as pd
from util.util import yield_blocks, parse_record
from layouts.gas_disposition_file_oil import GAS_DISPOSITION_OIL_LAYOUT


def gas_disposition_file_oil_parser(source_file_path, dest_folder_path='', block_size=200, limiting_counter=False,
                                    check_stop=100):
	'''
	Extract data from the oil ledger files based on layout in gas_disposition_file_oil.py
	Saves the data to a csv file

	:param source_file_path: path to the gas_disposition_file_oil file
	:param dest_folder_path: folder path to save the csv file
	:param block_size: block size for each record in the file
	:param limiting_counter: limit the number of records to be parsed
	:param check_stop: number of records to be parsed
	:return: None
	'''

	print('opening', source_file_path, '...')
	file = open(source_file_path, 'rb')  # Opens the .ebc file and reads it as bytes

	count = 0  # counter for number of records

	# Loop section for all records or partial set
	res = []

	for block in yield_blocks(file, block_size):  # for each block in file

		##For testing script
		if limiting_counter and count > check_stop:  # Stops the loop once a set number of record has been complete
			break

		parsed_vals = parse_record(block, GAS_DISPOSITION_OIL_LAYOUT)  # formats the record and returns a formated {dict}

		temp_df = pd.DataFrame([parsed_vals], columns=parsed_vals.keys())  ##convert {dict} to dataframe

		res.append(temp_df)
		count += 1

	print(f'Number of records: {count}')

	# generate output file
	if dest_folder_path == '':
		dest_folder_path = f'../out/'

	res = pd.concat(res, ignore_index=True)
	dest_file_path = f'{dest_folder_path}{Path(source_file_path).stem}.csv'
	res.to_csv(dest_file_path, index=False)
	file.close()


if __name__ == '__main__':
	file_path = r'/Volumes/haitao_folder/rrc/PR_Gas_Disposition/olf102.ebc'
	gas_disposition_file_oil_parser(file_path)
