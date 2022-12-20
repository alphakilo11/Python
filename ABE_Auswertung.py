from google.colab import drive
drive.mount('/content/drive')

BATTLE_RESULTS = {'WON': 'battle_win', 'LOST': 'battle_lost', 'DRAW': 'battle_draw'}
def ABE_auswertung(folderpath='/content/drive/MyDrive/ArmA 3/Homebrew/Automated Battle Engine/Results_1', source_file_path='/incoming', source_file_type='.rpt'):
  """
  extracts and splits Automated Battle Engine results from Arma 3 rpt files located in source_file_path to different files
  Example:
    print(ABE_auswertung("/content/drive/MyDrive/ArmA 3/Homebrew/Automated Battle Engine/Results_1"))
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
          if 'AKBL' in line:
            if 'AKBL Result: ' in line:
              date = file[-23:-13] + ' ' # convert filename to timestamp
              akbl_results.append(date + line)
              del date 
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

def break_apart_vanilla(folderpath='/content/drive/MyDrive/ArmA 3/Homebrew/Automated Battle Engine/Results_1'):
  """
  extracts Automated Battle Engine (Vanilla Version) results and collects them in lists
  Example:
    break_apart_vanilla("/content/drive/MyDrive/ArmA 3/Homebrew/Automated Battle Engine/Results_1")
  ENHANCE use regex
  """
  # break apart Result Lines
  with open(folderpath + '/AKBL_collected_results.txt', 'r') as file:
    step2 = file.readlines()
  step3 = []
  skipped_lines = 0
  for line in step2:
    if 'Survivors: ' in line: # 'Survivors: ' means that it's a version without Version number
      step3.append(line.split('Survivors: ')[1])
    else:
      skipped_lines += 1

  del step2
  # break apart further
  step4 = []
  for line in step3:
    step4.append((line.split('.')[0].split(';')))
  del step3

  if skipped_lines > 0:
    print(skipped_lines, 'lines skipped. Reason: incompatibility. Use a more recent version of the auswertung.')

  return step4


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


def create_result_DataFrame(data, starting_vehicles=10):
  """
  Create a Pandas DataFrame with following entries: ['battle_win', 'battle_lost', 'battle_draw', 'kills', 'losses', 'score', 'number_of_battles', 'torverhaeltnis', 'kill-death-ratio']
  Requires input from ABE_auswertung (like this: [['csa38_cromwell_DCS', '3', 'LIB_UK_DR_M4A3_75_DLV', '10'], ['csa38_cromwell_245camo2', '10', 'CSA38_pzbfwIamb_DE', '0']])
  Example:
    create_result_DataFrame(ABE_auswertung()).sort_values('score')
  """

  import pandas as pd

  result = {}
  for line in data:
    home_type = line[0]
    home_score = int(line[1])
    away_type = line[2]
    away_score = int(line[3])
    #create dictionary entries for each type
    result.setdefault(home_type, {BATTLE_RESULTS['WON']: 0, BATTLE_RESULTS['LOST']: 0, BATTLE_RESULTS['DRAW']: 0, 'kills': 0, 'losses': 0})
    result.setdefault(away_type, {BATTLE_RESULTS['WON']: 0, BATTLE_RESULTS['LOST']: 0, BATTLE_RESULTS['DRAW']: 0, 'kills': 0, 'losses': 0})
    # increase the corresponding value
    if home_score > away_score:
      result[home_type][BATTLE_RESULTS['WON']] += 1
      result[away_type][BATTLE_RESULTS['LOST']] += 1
    elif home_score < away_score:
      result[home_type][BATTLE_RESULTS['LOST']] += 1
      result[away_type][BATTLE_RESULTS['WON']] += 1
    else:
      result[home_type][BATTLE_RESULTS['DRAW']] += 1
      result[away_type][BATTLE_RESULTS['DRAW']] += 1
    #set kills and lossess
    result[home_type]['kills'] += (starting_vehicles - away_score)
    result[home_type]['losses'] += (starting_vehicles - home_score)
    result[away_type]['kills'] += (starting_vehicles - home_score)
    result[away_type]['losses'] += (starting_vehicles - away_score)

  #convert to Pandas DataFrame
  result = pd.DataFrame.from_dict(result, orient='index')
  # add derived data
  result['score'] = result.apply(lambda row: row.battle_win * 3 + row.battle_draw, axis=1)
  result['number_of_battles'] = result.apply(lambda row: row.battle_win + row.battle_lost + row.battle_draw, axis=1)
  result['torverhaeltnis'] = result.apply(lambda row: row.kills - row.losses, axis=1)
  result['kill-death-ratio'] = result.apply(lambda row: (row.kills / row.losses) if (row.losses > 0) else (row.kills / 0.4), axis=1) # I assigned some value 0 < x < 1 to types with 0 losses

  return result
