'''
@File   :  oil_ledger_parser.py
@Author :  Haitao Lu
@Date   :  16-Mar-2023 5:37 AM

Extract data from the oil ledger files based on layout in oil_ledger_layout.py

'''

from pathlib import Path
import pandas as pd
from util.util import yield_blocks, parse_record
from layouts.oil_ledger_layout import oil_ledger_layout
from ebcdic_formats.ebcdic_formats import pic_generic


def oil_ledger_parser(source_file_path, dest_folder_path='', block_size=1200, limiting_counter=False, check_stop=100):
	'''
	Extract data from the oil ledger files based on layout in oil_ledger_layout.py
	Saves the data to a csv file

	:param source_file_path: path to the oil ledger file
	:param dest_folder_path: folder path to save the csv file
	:param block_size: block size for each record in the file
	:param limiting_counter: limit the number of records to be parsed
	:param check_stop: number of records to be parsed
	:return: None
	'''

	print('opening', source_file_path, '...')
	file = open(source_file_path, 'rb')  ##Opens the .ebc file and reads it as bytes

	count = 0  ##counter for number of records
	oil_field_count = 0  ##counter for number of oil fields
	oil_lease_count = 0  ##counter for number of oil leases
	oil_multi_well_count = 0  ##counter for number of oil multi wells
	oil_well_count = 0  ##counter for number of oil wells

	# Loop section for all records or partial set
	res_oil_field, res_oil_lease, res_oil_multi_well, res_oil_well = [], [], [], []

	for block in yield_blocks(file, block_size):  ##for each block in file

		##For testing script
		if limiting_counter and count > check_stop:  ##Stops the loop once a set number of record has been complete
			break

		start_value = pic_generic(block[0:1])  ## first two characters of a block

		# Selecting layout based on leading start value and parsing record based on the selected layout

		layout = oil_ledger_layout(start_value)['layout']  # identifies layout based on record start values
		parsed_vals = parse_record(block, layout)  # formats the record and returns a formated {dict}

		temp_df = pd.DataFrame([parsed_vals], columns=parsed_vals.keys())  ##convert {dict} to dataframe

		if start_value == '1':
			oil_field_count += 1
			res_oil_field.append(temp_df)
		elif start_value == '3':
			oil_lease_count += 1
			res_oil_lease.append(temp_df)
		elif start_value == '4':
			oil_multi_well_count += 1
			res_oil_multi_well.append(temp_df)
		elif start_value == '5':
			oil_well_count += 1
			res_oil_well.append(temp_df)
		else:
			print('Error: Unknown record type')
			print('Record start value:', start_value)
			break

		count += 1
	print(f'Number of records: {count}')
	print(f'Oil field records: {oil_field_count}')
	print(f'Oil lease records: {oil_lease_count}')
	print(f'Multi well records: {oil_multi_well_count}')
	print(f'Oil well records: {oil_well_count}')

	res_oil_field = pd.concat(res_oil_field)
	res_oil_lease = pd.concat(res_oil_lease)
	res_oil_multi_well = pd.concat(res_oil_multi_well)
	res_oil_well = pd.concat(res_oil_well)

	if dest_folder_path == '':
		dest_folder_path = f'../out/'

	oil_field_file_path = f'{dest_folder_path}{Path(source_file_path).stem}_oil_field.csv'
	oil_lease_file_path = f'{dest_folder_path}{Path(source_file_path).stem}_oil_lease.csv'
	oil_multi_well_file_path = f'{dest_folder_path}{Path(source_file_path).stem}_oil_multi_well.csv'
	oil_well_file_path = f'{dest_folder_path}{Path(source_file_path).stem}_oil_well.csv'

	res_oil_field.to_csv(oil_field_file_path, index=False)
	res_oil_lease.to_csv(oil_lease_file_path, index=False)
	res_oil_multi_well.to_csv(oil_multi_well_file_path, index=False)
	res_oil_well.to_csv(oil_well_file_path, index=False)

	print('Oil field file saved to', oil_field_file_path)
	print('Oil lease file saved to', oil_lease_file_path)
	print('Oil multi well file saved to', oil_multi_well_file_path)
	print('Oil well file saved to', oil_well_file_path)

	file.close()


if __name__ == '__main__':
	file_path = r'/Volumes/haitao_folder/rrc/Oil_Ledger_Dist /olf001l.ebc'
	oil_ledger_parser(file_path)
