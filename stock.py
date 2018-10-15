import pandas as pd
import tushare as ts

def get_average(k, time, name):
    time -= 1
    out = pd.DataFrame(columns=[name+"-open", name+"-close", name+"-high", name+"-low", name+"-volume"])
    index = 0
    while index < time:
        out.loc[index] = {name+"-open":0, name+"-close":0, name+"-high":0, name+"-low":0, name+"-volume":0}
        index+=1

    for index in k.index:
        if index < time:
            continue
        sum = k.iloc[index-time:index+1,1:6].sum()
        out.loc[index] = {name + "-open":sum[0]/(time+1), name + "-close":sum[1]/(time+1),
                name + "-high":sum[2]/(time+1), name + "-low":sum[3]/(time+1), name + "-volume":sum[4]/(time+1)}
    out['date'] = k['date']
    return out

def main ():
    k = ts.get_k_data('600385')
    print(k)
    average = get_average(k, 8, "8day")
    print(average)
    k1 = pd.merge(k, average, on='date')
    print(k1)

if __name__ == '__main__':
    main()