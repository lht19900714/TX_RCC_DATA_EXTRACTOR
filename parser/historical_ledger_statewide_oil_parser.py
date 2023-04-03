'''
@File   :  historical_ledger_statewide_oil_parser.py
@Author :  Haitao Lu
@Date   :  02-Apr-2023 4:03 PM
'''

from pathlib import Path
import pandas as pd
from util.util import yield_blocks, parse_record, save_to_csv
from layouts.historical_ledger_statewide_oil import historical_ledger_statewide_oil_layout
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
	source_file = open(source_file_path, 'rb')

	count = 0  # counter for number of records
	ldroot_count = 0  # counter for number of LDROOT
	ldoldata_count = 0  # counter for number of LDGSDATA
	ldoildsp_count = 0  # counter for number of LDGASDSP
	ldocshds_count = 0  # counter for number of LDGCONDS

	# Loop section for all records or partial set
	# results for each record type
	res_ldroot, res_ldoldata, res_ldoildsp, res_ldocshds = [], [], [], []

	# destination file path
	if dest_folder_path == '':
		dest_folder_path = f'../out'

	ldroot_dest_file_name = f'{Path(source_file_path).stem}_ldroot.csv'
	ldoldata_dest_file_name = f'{Path(source_file_path).stem}_ldoldata.csv'
	ldoildsp_dest_file_name = f'{Path(source_file_path).stem}_ldoildsp.csv'
	ldocshds_dest_file_name = f'{Path(source_file_path).stem}_ldocshds.csv'

	# Loop section for all records or partial set
	for block in yield_blocks(source_file, block_size):  # for each block in file
		if limiting_counter and count > check_stop:  ##Stops the loop once a set number of record has been complete
			if len(res_ldroot) > 0 and ldroot_count == len(res_ldroot):
				save_to_csv(pd.concat(res_ldroot), dest_folder_path, ldroot_dest_file_name)
			else:
				save_to_csv(pd.concat(res_ldroot), dest_folder_path, ldroot_dest_file_name, append=True)

			if len(res_ldoldata) > 0 and ldoldata_count == len(res_ldoldata):
				save_to_csv(pd.concat(res_ldoldata), dest_folder_path, ldoldata_dest_file_name)
			else:
				save_to_csv(pd.concat(res_ldoldata), dest_folder_path, ldoldata_dest_file_name, append=True)

			if len(res_ldoildsp) > 0 and ldoildsp_count == len(res_ldoildsp):
				save_to_csv(pd.concat(res_ldoildsp), dest_folder_path, ldoildsp_dest_file_name)
			else:
				save_to_csv(pd.concat(res_ldoildsp), dest_folder_path, ldoildsp_dest_file_name, append=True)
			if len(res_ldocshds) > 0 and ldocshds_count == len(res_ldocshds):
				save_to_csv(pd.concat(res_ldocshds), dest_folder_path, ldocshds_dest_file_name)
			else:
				save_to_csv(pd.concat(res_ldocshds), dest_folder_path, ldocshds_dest_file_name, append=True)
			source_file.close()
			break

		start_value = pic_generic(block[0:2])  ## first two characters of a block

		layout = historical_ledger_statewide_oil_layout(start_value)[
			'layout']  # identifies layout based on record start values
		parsed_vals = parse_record(block, layout)  # formats the record and returns a formated {dict}

		temp_df = pd.DataFrame([parsed_vals], columns=parsed_vals.keys())  ##convert {dict} to dataframe

		if start_value == '01':
			ldroot_count += 1
			res_ldroot.append(temp_df)
		elif start_value == '06':
			ldoldata_count += 1
			res_ldoldata.append(temp_df)
		elif start_value == '07':
			ldoildsp_count += 1
			res_ldoildsp.append(temp_df)
		elif start_value == '08':
			ldocshds_count += 1
			res_ldocshds.append(temp_df)
		else:
			print('Error: start value not found')
			print('Record start value:', start_value)
			source_file.close()
			return
		count += 1

		# if result is over predefined number, and then save to csv file
		if len(res_ldroot) > 10000:
			if ldroot_count == len(res_ldroot):
				print('saving ldroot to csv file...')
				ldroot_df = pd.concat(res_ldroot)
				save_to_csv(ldroot_df, dest_folder_path, ldroot_dest_file_name)
				res_ldroot = []
			else:
				print('appending ldroot to csv file...')
				ldroot_df = pd.concat(res_ldroot)
				save_to_csv(ldroot_df, dest_folder_path, ldroot_dest_file_name, append=True)
				res_ldroot = []
		if len(res_ldoldata) > 10000:
			if ldoldata_count == len(res_ldoldata):
				print('saving ldoldata to csv file...')
				ldoldata_df = pd.concat(res_ldoldata)
				save_to_csv(ldoldata_df, dest_folder_path, ldoldata_dest_file_name)
				res_ldoldata = []
			else:
				print('appending ldoldata to csv file...')
				ldoldata_df = pd.concat(res_ldoldata)
				save_to_csv(ldoldata_df, dest_folder_path, ldoldata_dest_file_name, append=True)
				res_ldoldata = []
		if len(res_ldoildsp) > 10000:
			if ldoildsp_count == len(res_ldoildsp):
				print('saving ldoildsp to csv file...')
				ldoildsp_df = pd.concat(res_ldoildsp)
				save_to_csv(ldoildsp_df, dest_folder_path, ldoildsp_dest_file_name)
				res_ldoildsp = []
			else:
				print('appending ldoildsp to csv file...')
				ldoildsp_df = pd.concat(res_ldoildsp)
				save_to_csv(ldoildsp_df, dest_folder_path, ldoildsp_dest_file_name, append=True)
				res_ldoildsp = []
		if len(res_ldocshds) > 10000:
			if ldocshds_count == len(res_ldocshds):
				print('saving ldocshds to csv file...')
				ldocshds_df = pd.concat(res_ldocshds)
				save_to_csv(ldocshds_df, dest_folder_path, ldocshds_dest_file_name)
				res_ldocshds = []
			else:
				print('appending ldocshds to csv file...')
				ldocshds_df = pd.concat(res_ldocshds)
				save_to_csv(ldocshds_df, dest_folder_path, ldocshds_dest_file_name, append=True)
				res_ldocshds = []

	print(f'Number of records: {count}')
	print(f'Number of ldroot records: {ldroot_count}')
	print(f'Number of ldoldata records: {ldoldata_count}')
	print(f'Number of ldoildsp records: {ldoildsp_count}')
	print(f'Number of ldocshds records: {ldocshds_count}')

	print(f'ldroot saved to: {dest_folder_path}/{ldroot_dest_file_name}')
	print(f'ldoldata saved to: {dest_folder_path}/{ldoldata_dest_file_name}')
	print(f'ldoildsp saved to: {dest_folder_path}/{ldoildsp_dest_file_name}')
	print(f'ldocshds saved to: {dest_folder_path}/{ldocshds_dest_file_name}')

	source_file.close()


if __name__ == "__main__":
	file_path = r'/Volumes/haitao_folder/rrc/Historical_Ledger_Statewide_Oil/S.LDF900OL.D.ebc'
	historical_ledger_statewide_gas_parser(file_path, block_size=160, limiting_counter=True, check_stop=500000)
