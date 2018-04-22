#!/usr/bin/python
import pickle

game_data = {
    "position":"N2 E3",
    "pocket": ["key", "knife"],
    "money": 160
}

#写文件
save_file = open("save.dat", "wb")
pickle.dump(game_data, save_file)
save_file.close();
#读文件
load_file = open("save.dat", "rb")
load_game_data=pickle.load(load_file)
load_file.close()
print load_game_data
