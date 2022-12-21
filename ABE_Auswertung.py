from google.colab import drive
drive.mount('/content/drive')
# constants
BATTLE_RESULTS = {'WON': 'battle_win', 'LOST': 'battle_lost', 'DRAW': 'battle_draw'}
RESULT_FORMAT = { # the information sequence for the battlelogger result line for each version
  'vanilla': ['AK_var_fnc_battlelogger_typeEAST', 'east_veh_survivors', 'AK_var_fnc_battlelogger_typeINDEP', 'indep_veh_survivors'],
  '1.01': [
    "AKBL Result: ",
    'AK_var_fnc_battlelogger_Version',
    'AK_var_fnc_battlelogger_typeEAST',
    'east_veh_survivors',
    'AK_var_fnc_battlelogger_typeINDEP',
    'indep_veh_survivors',
    'AK_var_fnc_battlelogger_numberOfStartingVehicles',
    'worldName',
    'AK_var_fnc_automatedBattleEngine_location',
    'AK_var_fnc_battlelogger_engagementDistance',
    'AK_var_fnc_battlelogger_vehSpacing',
    'AK_var_fnc_battlelogger_breiteGefStr',
    'AK_var_fnc_battlelogger_platoonSize',
    'AK_var_fnc_battlelogger_startTime',
    'systemTime',
    'sunOrMoon',
    'moonIntensity'
  ]
}

def ABE_auswertung( \
  folderpath='/content/drive/MyDrive/ArmA 3/Homebrew/Automated Battle Engine/Results_1', \
  source_file_path='/incoming',\
  source_file_type='.rpt',\
  version='1.01'):
  """
  extracts and splits Automated Battle Engine results from Arma 3 rpt files located in source_file_path to different files
  Example:
    ABE_auswertung("/content/drive/MyDrive/ArmA 3/Homebrew/Automated Battle Engine/Results_1")
  ENHANCE use regex
  """
  from os import listdir, makedirs
  from os.path import isfile, join, exists
  import shutil

  # check for source_file_type files in source_file_path folder
  file_list = [f for f in listdir(folderpath + source_file_path) if isfile(join(folderpath + source_file_path, f))]
  if len(file_list) > 0: 
    skipped_files = 0
    akbl_results = []
    for file in file_list:
      if file[-4:] == source_file_type:
        with open((folderpath + source_file_path + '/' + file), 'r') as datei:
          step1 = datei.readlines()
        step2 = []
        for line in step1:
          if 'AKBL' in line: # check if it's an AKBL line
            if RESULT_FORMAT[version][0] in line: # check if it's result line
              akbl_results.append(line)
            step2.append(line)
        #create folders if necessary
        newpath = folderpath + '/archive' 
        if not exists(newpath):
            makedirs(newpath)
        newpath = folderpath + '/archive/AKBL_archive' 
        if not exists(newpath):
            makedirs(newpath)
        # create filtered AKBL files
        try:
          with open(folderpath + '/archive/AKBL_archive/' + file[:-4] + '.txt', 'x') as datei:
            datei.writelines(step2)
          # archive source_file_type file
          shutil.move (folderpath + source_file_path + '/' + file, folderpath + '/archive/' + file)
        except FileExistsError:
          print(f"WARNING: {folderpath + '/archive/AKBL_archive/' + file[:-4] + '.txt'} already exists, which means most likely that the corresponding {source_file_type} has already been processed.")
          skipped_files += 1
        del step1, step2
      else:
        skipped_files += 1
    # update the permanent file
    if len(akbl_results) > 0:
      with open(folderpath + '/AKBL_collected_results.txt', 'a') as file:
        file.writelines(akbl_results)
    # print status
    print(f'{len(file_list) - skipped_files} files have been processed. {skipped_files} files have been skipped.')
    del akbl_results, file_list, skipped_files
  else:
    print(f'No {source_file_type} files in {source_file_path}')


def break_apart(folderpath='/content/drive/MyDrive/ArmA 3/Homebrew/Automated Battle Engine/Results_1', version='1.01'):
  """
  extracts Automated Battle Engine results and collects them in dictionaries
  vanilla results have a length of 4
  Example:
    break_apart("/content/drive/MyDrive/ArmA 3/Homebrew/Automated Battle Engine/Results_1")
  ENHANCE use regex
  """
  import ast
  with open(folderpath + '/AKBL_collected_results.txt', 'r') as file:
    result_lines = file.readlines()
  compendium = []
  for line in result_lines:
    if 'Survivors: ' in line: # check if it is vanilla
      keys = RESULT_FORMAT['vanilla']
      values = line.split('Survivors: ')[1].split('.')[0].split(';')
      values[1] = int(values[1])
      values[3] = int(values[3])
      compendium.append(dict(zip(keys,values)))
    else:
      keys = RESULT_FORMAT[version][1:] # strip the first entry is it contains no relevant information
      values = ast.literal_eval("[" + line.split(RESULT_FORMAT[version][0])[1][2:])
      compendium.append(dict(zip(keys,values)))
  return compendium


def create_result_DataFrame(data, starting_vehicles=10, version='1.01'):
  """
  Create a Pandas DataFrame with following entries: ['battle_win', 'battle_lost', 'battle_draw', 'kills', 'losses', 'score', 'number_of_battles', 'torverhaeltnis', 'kill-death-ratio']
  Requires input as dictionaries obeying RESULT_FORMAT
  Example:
    create_result_DataFrame(break_apart()).sort_values('score')
  """
  
  import pandas as pd

  result = {}
  for line in data:

    #create dictionary entries for each type
    result.setdefault(line['AK_var_fnc_battlelogger_typeEAST'], {BATTLE_RESULTS['WON']: 0, BATTLE_RESULTS['LOST']: 0, BATTLE_RESULTS['DRAW']: 0, 'kills': 0, 'losses': 0})
    result.setdefault(line['AK_var_fnc_battlelogger_typeINDEP'], {BATTLE_RESULTS['WON']: 0, BATTLE_RESULTS['LOST']: 0, BATTLE_RESULTS['DRAW']: 0, 'kills': 0, 'losses': 0})
    # increase the corresponding value
    if line['east_veh_survivors'] > line['indep_veh_survivors']:
      result[line['AK_var_fnc_battlelogger_typeEAST']][BATTLE_RESULTS['WON']] += 1
      result[line['AK_var_fnc_battlelogger_typeINDEP']][BATTLE_RESULTS['LOST']] += 1
    elif line['east_veh_survivors'] < line['indep_veh_survivors']:
      result[line['AK_var_fnc_battlelogger_typeEAST']][BATTLE_RESULTS['LOST']] += 1
      result[line['AK_var_fnc_battlelogger_typeINDEP']][BATTLE_RESULTS['WON']] += 1
    else:
      result[line['AK_var_fnc_battlelogger_typeEAST']][BATTLE_RESULTS['DRAW']] += 1
      result[line['AK_var_fnc_battlelogger_typeINDEP']][BATTLE_RESULTS['DRAW']] += 1
    #set kills and lossess
    result[line['AK_var_fnc_battlelogger_typeEAST']]['kills'] += (starting_vehicles - line['indep_veh_survivors'])
    result[line['AK_var_fnc_battlelogger_typeEAST']]['losses'] += (starting_vehicles - line['east_veh_survivors'])
    result[line['AK_var_fnc_battlelogger_typeINDEP']]['kills'] += (starting_vehicles - line['east_veh_survivors'])
    result[line['AK_var_fnc_battlelogger_typeINDEP']]['losses'] += (starting_vehicles - line['indep_veh_survivors'])

  #convert to Pandas DataFrame
  result = pd.DataFrame.from_dict(result, orient='index')
  # add derived data
  result['score'] = result.apply(lambda row: row.battle_win * 3 + row.battle_draw, axis=1)
  result['number_of_battles'] = result.apply(lambda row: row.battle_win + row.battle_lost + row.battle_draw, axis=1)
  result['torverhaeltnis'] = result.apply(lambda row: row.kills - row.losses, axis=1)
  result['kill-death-ratio'] = result.apply(lambda row: (row.kills / row.losses) if (row.losses > 0) else (row.kills / 0.4), axis=1) # I assigned some value 0 < x < 1 to types with 0 losses

  return result


def create_matrix(data):
  """
  WIP
  Create a matrix
  Example:
    NIL
  """
  entries = []
  for line in data:
    entries.append(line[0])
    entries.append(line[2])
  return sorted(set(entries)) # collect all