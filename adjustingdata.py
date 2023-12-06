import pandas as pd 

data=pd.read_csv("sources/players_22.csv",low_memory=False)



useless_prop=["sofifa_id","player_url","long_name","dob","height_cm","weight_kg","club_team_id",
 
 
"league_level",
"club_position",
"club_jersey_number",
"club_loaned_from",
"club_joined",
 
"nationality_id",
 
"nation_team_id",
"nation_position",
"nation_jersey_number",
 
"weak_foot",
"skill_moves",
"international_reputation",
"work_rate",
"body_type",
"real_face",
"release_clause_eur",
"player_tags",
"player_traits",
"ls",
"st",
"rs",
"lw",
"lf",
"cf",
"rf",
"rw",
"lam",
"cam",
"ram",
"lm",
"lcm",
"cm",
"rcm",
"rm",
"lwb",
"ldm",
"cdm",
"rdm",
"rwb",
"lb",
"lcb",
"cb",
"rcb",
"rb",
"gk",
"player_face_url",
"club_logo_url",
"club_flag_url",
"nation_logo_url",
"nation_flag_url"]

data=data.drop(useless_prop,axis=1)


for column in data:
    print(column)


data.to_csv("fifa22.csv")

 