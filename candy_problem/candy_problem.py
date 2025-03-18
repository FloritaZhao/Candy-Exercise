def get_friends_favorite_candy_count(friend_favorites):
    candy_count = {}
    for name, candy_list in friend_favorites:
        for candy in candy_list:
            candy_count[candy] = candy_count.get(candy, 0) +1
    return candy_count
            

def create_new_candy_data_structure(friend_favorites):
    new_structure = {}
    for name, candy_list in friend_favorites:
        for candy in candy_list:
            if not candy in new_structure.keys():
                new_structure[candy] = [name]
            else: 
                new_structure[candy].append(name)
    return new_structure

def get_friends_who_like_specific_candy(friend_favorites, candy_name):
    candy_data = create_new_candy_data_structure(friend_favorites)
    return candy_data[candy_name]


def create_candy_set(friend_favorites):
    candy_data = create_new_candy_data_structure(friend_favorites)
    candy_set = set(candy_data.keys())
    return candy_set
