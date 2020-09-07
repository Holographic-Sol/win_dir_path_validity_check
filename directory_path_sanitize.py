import os

while True:
	valid_len_bool = False
	valid_drive_bool = False
	valid_non_win_res_nm_bool = False
	valid_char_bool = False

	try:
		# 1 Enter String
		dest_path_entered = input('Enter Directory Path: ')

		# 2 Continue Only If Length Of String Is < 255 Characters
		str_len = len(dest_path_entered)
		if str_len < 255:
			valid_len_bool = True
		elif str_len >= 255:
			valid_len_bool = False

		# 3 Determine Valid Drive Letter
		if valid_len_bool is True:
			char_var0 = dest_path_entered[0]
			char_var1 = dest_path_entered[1]
			char_var2 = dest_path_entered[2]
			char_var3 = str(char_var0 + char_var1 + char_var2)
			if os.path.exists(char_var3) and char_var0.isalpha() and char_var1 is ':' and char_var2 is '\\':
				valid_drive_bool = True
			else:
				valid_drive_bool = False

		# 4 Check For Forbidden Chars
		valid_char = []
		if valid_len_bool is True and valid_drive_bool is True:
			invalid_char = '<>:"/|?*.'
			i = 0
			for dest_path_entereds in dest_path_entered:
				if not i is 1:
					print('-- checking character:', dest_path_entered[i])
					if dest_path_entered[i].strip() in invalid_char:
						valid_char.append(False)
				elif i is 1:
					print('-- skipping known colon:', dest_path_entered[i])
				i += 1
			if not False in valid_char:
				valid_char_bool = True

		# 5 Determine If The String Matches Windows Reserved Names
		if valid_len_bool is True and valid_drive_bool is True and valid_char_bool is True:
			valid_var = []
			win_res_nm = ['CON', 'PRN', 'AUX', 'NUL',
					'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9',
					'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9']
			i = 0
			for win_res_nms in win_res_nm:
				if str('\\' + win_res_nm[i] + '\\') in dest_path_entered:
					valid_var.append(False)
				elif dest_path_entered.endswith(win_res_nm[i]):
					valid_var.append(False)
				elif str(win_res_nm[i] + '.') in dest_path_entered:
					valid_var.append(False)
				i += 1
			if not False in valid_var:
				valid_non_win_res_nm_bool = True

		# Print Results
		print('\nResutls:')
		print('String Length:', valid_len_bool)
		print('Drive Letter:', valid_drive_bool)
		print('Valid Characters:', valid_char_bool)
		print('Does Not Contain System Reserved Names:', valid_non_win_res_nm_bool, '\n')

	except (KeyboardInterrupt, SystemExit):
		print('quit')