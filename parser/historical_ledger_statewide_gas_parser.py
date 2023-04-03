'''
@File   :  historical_ledger_statewide_gas_parser.py
@Author :  Haitao Lu
@Date   :  01-Apr-2023 2:11 PM
'''

from pathlib import Path
import pandas as pd
from util.util import yield_blocks, parse_record
from layouts.historical_ledger_statewide_gas import historical_ledger_statewide_gas_layout
from ebcdic_formats.ebcdic_formats import pic_generic


def historical_ledger_statewide_gas_parser(source_file_path, dest_folder_path='', block_size=200,
                                           limiting_counter=False, check_stop=100):
	'''

	:param source_file_path: path to the historical_ledger_statewide_gas file
	:param dest_folder_path: folder path to save the csv file
	:param block_size: block size for each record in the file
	:param limiting_counter: limit the number of records to be parsed
	:param check_stop: number of records to be parsed
	:return: None
	'''

	print('opening', source_file_path, '...')
	file = open(source_file_path, 'rb')

	count = 0  # counter for number of records
	ldroot_count = 0  # counter for number of LDROOT
	ldgsdata_count = 0  # counter for number of LDGSDATA
	ldgasdsp_count = 0  # counter for number of LDGASDSP
	ldgconds_count = 0  # counter for number of LDGCONDS
	ldgstat_count = 0  # counter for number of LDGSTAT

	# results for each record type
	res_ldroot, res_ldgsdata, res_ldgasdsp, res_ldgconds, res_ldgstat = [], [], [], [], []

	# Loop section for all records or partial set
	for block in yield_blocks(file, block_size):  # for each block in file

		##For testing script
		if limiting_counter and count > check_stop:# Stops the loop once a set number of record has been complete
			break

		start_value = pic_generic(block[0:2])  ## first two characters of a block

		# Selecting layout based on leading start value and parsing record based on the selected layout

		layout = historical_ledger_statewide_gas_layout(start_value)[
			'layout']  # identifies layout based on record start values
		parsed_vals = parse_record(block, layout)  # formats the record and returns a formated {dict}

		temp_df = pd.DataFrame([parsed_vals], columns=parsed_vals.keys())  ##convert {dict} to dataframe

		if start_value == '01':
			ldroot_count += 1
			res_ldroot.append(temp_df)
		elif start_value == '02':
			ldgsdata_count += 1
			res_ldgsdata.append(temp_df)
		elif start_value == '03':
			ldgasdsp_count += 1
			res_ldgasdsp.append(temp_df)
		elif start_value == '04':
			ldgconds_count += 1
			res_ldgconds.append(temp_df)
		elif start_value == '05':
			ldgstat_count += 1
			res_ldgstat.append(temp_df)
		else:
			print('Error: start value not found')
			print('Record start value:', start_value)
			file.close()
			return
		count += 1

	print(f'Number of records: {count}')
	print(f'Number of LDROOT: {ldroot_count}')
	print(f'Number of LDGSDATA: {ldgsdata_count}')
	print(f'Number of LDGASDSP: {ldgasdsp_count}')
	print(f'Number of LDGCONDS: {ldgconds_count}')
	print(f'Number of LDGSTAT: {ldgstat_count}')

	# Concatenate all dataframes into one
	if len(res_ldroot) > 0:
		res_ldroot = pd.concat(res_ldroot)
	if len(res_ldgsdata) > 0:
		res_ldgsdata = pd.concat(res_ldgsdata)
	if len(res_ldgasdsp) > 0:
		res_ldgasdsp = pd.concat(res_ldgasdsp)
	if len(res_ldgconds) > 0:
		res_ldgconds = pd.concat(res_ldgconds)
	if len(res_ldgstat) > 0:
		res_ldgstat = pd.concat(res_ldgstat)


	if dest_folder_path == '':
		dest_folder_path = f'../out/'

	ldroot_file_path = f'{dest_folder_path}{Path(source_file_path).stem}_ldroot.csv'
	ldgsdata_file_path = f'{dest_folder_path}{Path(source_file_path).stem}_ldgsdata.csv'
	ldgasdsp_file_path = f'{dest_folder_path}{Path(source_file_path).stem}_ldgasdsp.csv'
	ldgconds_file_path = f'{dest_folder_path}{Path(source_file_path).stem}_ldgconds.csv'
	ldgstat_file_path = f'{dest_folder_path}{Path(source_file_path).stem}_ldgstat.csv'

	if len(res_ldroot) > 0:
		res_ldroot.to_csv(ldroot_file_path, index=False)
	if len(res_ldgsdata) > 0:
		res_ldgsdata.to_csv(ldgsdata_file_path, index=False)
	if len(res_ldgasdsp) > 0:
		res_ldgasdsp.to_csv(ldgasdsp_file_path, index=False)
	if len(res_ldgconds) > 0:
		res_ldgconds.to_csv(ldgconds_file_path, index=False)
	if len(res_ldgstat) > 0:
		res_ldgstat.to_csv(ldgstat_file_path, index=False)

	print(f'LDROOT file saved to {ldroot_file_path}')
	print(f'LDGSDATA file saved to {ldgsdata_file_path}')
	print(f'LDGASDSP file saved to {ldgasdsp_file_path}')
	print(f'LDGCONDS file saved to {ldgconds_file_path}')
	print(f'LDGSTAT file saved to {ldgstat_file_path}')

	file.close()

if __name__ == '__main__':
	file_path = r'/Volumes/haitao_folder/rrc/Historical_Ledger_Statewide_Gas/S.LDF900GS.D.ebc'
	historical_ledger_statewide_gas_parser(file_path,block_size=160,limiting_counter=True,check_stop=50000)



