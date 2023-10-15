import pickle
global data
data = {'devise': 'P'}

with open('data.pkl', 'wb') as file:
    pickle.dump(data, file)
    data['devise'] = 'P'
    print('OK')